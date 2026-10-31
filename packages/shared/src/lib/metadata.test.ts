import { describe, expect, it } from 'vitest';
import exifr from 'exifr';
import { concat, crc32, indexOf, latin1 } from './binary';
import { jpegSegments, pngChunks, webpChunks } from './containers';
import { cleanImage, UnsupportedFormat } from './clean';
import { hasAiProvenance, inspect } from './inspect';

const bin = (s: string) => Uint8Array.from(s, (c) => c.charCodeAt(0));
const enc = (s: string) => new TextEncoder().encode(s);
const has = (b: Uint8Array, s: string) => indexOf(b, s) >= 0;

// ---------- fixture builders ----------

type Entry = { tag: number; type: 3 | 2 | 4 | 5; values: number[] | string };

/** Big-endian TIFF with IFD0 entries and an optional GPS IFD. */
function tiff(ifd0: Entry[], gps?: Entry[]): Uint8Array {
  const size = (e: Entry) =>
    e.type === 2 ? (e.values as string).length + 1 : e.type === 3 ? 2 * (e.values as number[]).length : e.type === 4 ? 4 * (e.values as number[]).length : 8 * ((e.values as number[]).length / 2);
  const all = gps ? [...ifd0, { tag: 0x8825, type: 4, values: [0] } as Entry] : ifd0;
  const buf = new Uint8Array(4096);
  const dv = new DataView(buf.buffer);
  buf.set(bin('MM\0*'));
  dv.setUint32(4, 8);
  let heap = 1024;
  const writeIfd = (at: number, entries: Entry[]) => {
    dv.setUint16(at, entries.length);
    entries.forEach((e, i) => {
      const p = at + 2 + i * 12;
      const vals = e.type === 2 ? [...bin(e.values as string), 0] : (e.values as number[]);
      const count = e.type === 5 ? vals.length / 2 : vals.length;
      dv.setUint16(p, e.tag);
      dv.setUint16(p + 2, e.type);
      dv.setUint32(p + 4, count);
      const n = size(e);
      const target = n <= 4 ? p + 8 : heap;
      if (n > 4) {
        dv.setUint32(p + 8, heap);
        heap += n + (n & 1);
      }
      vals.forEach((v, j) => {
        if (e.type === 2) buf[target + j] = v;
        else if (e.type === 3) dv.setUint16(target + 2 * j, v);
        else dv.setUint32(target + 4 * j, v);
      });
    });
    dv.setUint32(at + 2 + entries.length * 12, 0);
  };
  writeIfd(8, all);
  if (gps) {
    const gpsAt = 512;
    const ptr = 8 + 2 + (all.length - 1) * 12 + 8;
    dv.setUint32(ptr, gpsAt);
    writeIfd(gpsAt, gps);
  }
  return buf.subarray(0, heap);
}

const GPS: Entry[] = [
  { tag: 0x0001, type: 2, values: 'N' },
  { tag: 0x0002, type: 5, values: [48, 1, 51, 1, 30, 1] },
  { tag: 0x0003, type: 2, values: 'E' },
  { tag: 0x0004, type: 5, values: [2, 1, 17, 1, 40, 1] },
];

const C2PA_MANIFEST = concat([
  bin('\0\0\0\x20jumb\0\0\0\x18jumdc2pa\0'),
  bin('\x74claim_generator_info\x81\xa1\x64name\x6dAdobe Firefly'),
  bin('http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia'),
]);

const XMP_FULL =
  '<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">' +
  '<rdf:Description rdf:about="" xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/" xmlns:dc="http://purl.org/dc/elements/1.1/" ' +
  'Iptc4xmpExt:DigitalSourceType="http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia">' +
  '<dc:creator><rdf:Seq><rdf:li>Jane Private</rdf:li></rdf:Seq></dc:creator></rdf:Description></rdf:RDF></x:xmpmeta>';

const seg = (marker: number, payload: Uint8Array) =>
  concat([Uint8Array.from([0xff, marker, (payload.length + 2) >> 8, (payload.length + 2) & 0xff]), payload]);

const SCAN = concat([seg(0xda, Uint8Array.from([1, 1, 0, 0, 0x3f, 0])), Uint8Array.from([0x12, 0xff, 0x00, 0x34]), Uint8Array.from([0xff, 0xd9])]);

function jpeg(): Uint8Array {
  return concat([
    Uint8Array.from([0xff, 0xd8]),
    seg(0xe0, bin('JFIF\0\x01\x01\0\0\x01\0\x01\0\0')),
    seg(0xe1, concat([bin('Exif\0\0'), tiff([
      { tag: 0x010f, type: 2, values: 'Canon' },
      { tag: 0x0110, type: 2, values: 'EOS R5' },
      { tag: 0x0112, type: 3, values: [6] },
    ], GPS)])),
    seg(0xe1, concat([bin('http://ns.adobe.com/xap/1.0/\0'), enc(XMP_FULL)])),
    seg(0xed, bin('Photoshop 3.0\08BIM\x04\x04\0\0\0\0\0\x0a\x1c\x02\x50\0\x04Jane')),
    seg(0xfe, bin('shot at home')),
    seg(0xeb, concat([bin('JP\0\x0b\0\0\0\x01'), C2PA_MANIFEST])),
    seg(0xdb, new Uint8Array(65)),
    SCAN,
    bin('TRAILING-PREVIEW-WITH-EXIF Canon'),
  ]);
}

function pngChunk(type: string, data: Uint8Array) {
  const td = concat([bin(type), data]);
  const crc = crc32(td);
  const len = data.length;
  return concat([
    Uint8Array.from([len >>> 24, (len >> 16) & 0xff, (len >> 8) & 0xff, len & 0xff]),
    td,
    Uint8Array.from([crc >>> 24, (crc >> 16) & 0xff, (crc >> 8) & 0xff, crc & 0xff]),
  ]);
}

function png(): Uint8Array {
  return concat([
    bin('\x89PNG\r\n\x1a\n'),
    pngChunk('IHDR', Uint8Array.from([0, 0, 0, 1, 0, 0, 0, 1, 8, 2, 0, 0, 0])),
    pngChunk('tEXt', bin('Author\0Jane Private')),
    pngChunk('tEXt', bin('parameters\0a cat in space, Steps: 20, Sampler: Euler, Model: sdxl')),
    pngChunk('iTXt', concat([bin('XML:com.adobe.xmp\0\0\0\0\0'), enc(XMP_FULL)])),
    pngChunk('tIME', new Uint8Array(7)),
    pngChunk('caBX', C2PA_MANIFEST),
    pngChunk('IDAT', Uint8Array.from([0x78, 0x9c, 0x63, 0, 0, 0, 1, 0, 1])),
    pngChunk('IEND', new Uint8Array()),
  ]);
}

function webpChunk(type: string, data: Uint8Array) {
  const len = data.length;
  return concat([bin(type), Uint8Array.from([len & 0xff, (len >> 8) & 0xff, (len >> 16) & 0xff, len >>> 24]), data, len & 1 ? new Uint8Array(1) : new Uint8Array()]);
}

function webp(): Uint8Array {
  const vp8x = Uint8Array.from([0x0c, 0, 0, 0, 0, 0, 0, 0, 0, 0]); // EXIF + XMP flags
  const body = concat([
    bin('WEBP'),
    webpChunk('VP8X', vp8x),
    webpChunk('VP8L', Uint8Array.from([0x2f, 0, 0, 0, 0])),
    webpChunk('EXIF', tiff([{ tag: 0x010f, type: 2, values: 'Pixel' }], GPS)),
    webpChunk('XMP ', enc('<x:xmpmeta><dc:creator>Jane Private</dc:creator></x:xmpmeta>')),
  ]);
  const n = body.length;
  return concat([bin('RIFF'), Uint8Array.from([n & 0xff, (n >> 8) & 0xff, (n >> 16) & 0xff, n >>> 24]), body]);
}

// ---------- inspect ----------

describe('inspect', () => {
  it('finds AI provenance and privacy fields in a JPEG', async () => {
    const r = await inspect(jpeg());
    expect(r.format).toBe('jpeg');
    expect(r.c2pa).toEqual({ present: true, generator: 'Adobe Firefly', sourceType: 'trainedAlgorithmicMedia' });
    expect(r.ai.map((f) => f.label)).toContain('Content Credentials (C2PA)');
    expect(r.ai.find((f) => f.label === 'IPTC digital source type')?.value).toBe('Created with generative AI');
    expect(hasAiProvenance(r)).toBe(true);
    const privacy = Object.fromEntries(r.privacy.map((f) => [f.label, f.value]));
    expect(privacy['GPS location']).toMatch(/^48\.8\d+, 2\.29\d+$/);
    expect(privacy['Camera / phone']).toContain('Canon');
  });

  it('reads Stable Diffusion parameters and C2PA from a PNG', async () => {
    const r = await inspect(png());
    expect(r.c2pa.present).toBe(true);
    expect(r.ai.map((f) => f.label)).toContain('Stable Diffusion parameters (A1111 / Forge)');
    expect(r.privacy.map((f) => f.label)).toContain('PNG text “Author”');
  });

  it('reports nothing for a file without metadata', async () => {
    const bare = concat([Uint8Array.from([0xff, 0xd8]), seg(0xdb, new Uint8Array(65)), SCAN]);
    const r = await inspect(bare);
    expect(r.ai).toEqual([]);
    expect(r.privacy).toEqual([]);
    expect(hasAiProvenance(r)).toBe(false);
  });
});

// ---------- clean ----------

describe('cleanImage JPEG', () => {
  const src = jpeg();
  const { bytes, removed, kept } = cleanImage(src);

  it('removes personal metadata and trailing previews', () => {
    for (const s of ['Canon', 'EOS R5', 'Jane', 'shot at home', 'TRAILING']) expect(has(bytes, s)).toBe(false);
    expect(removed).toEqual(
      expect.arrayContaining(['EXIF (camera, settings, dates)', 'GPS location', 'IPTC (names, captions, places)', 'Comments']),
    );
    expect(removed.some((r) => r.startsWith('Embedded extra images'))).toBe(true);
  });

  it('keeps C2PA, AI source type and orientation', async () => {
    expect(has(bytes, 'claim_generator_info')).toBe(true);
    expect(has(bytes, 'trainedAlgorithmicMedia')).toBe(true);
    expect(kept).toEqual(expect.arrayContaining(['Content Credentials (C2PA)', 'AI source type (IPTC)', 'Orientation']));
    const tags = await exifr.parse(bytes, { tiff: true, xmp: false });
    expect(tags.Orientation).toBe('Rotate 90 CW');
  });

  it('leaves the image data untouched and keeps JFIF first', () => {
    const before = jpegSegments(src).segments.at(-1)!.data;
    const after = jpegSegments(bytes).segments;
    expect(after.at(-1)!.data).toEqual(before);
    expect(after[1].marker).toBe(0xe0);
  });

  it('still reads as AI-made but no longer leaks private data', async () => {
    const r = await inspect(bytes);
    expect(hasAiProvenance(r)).toBe(true);
    expect(r.privacy).toEqual([]);
  });
});

describe('cleanImage PNG', () => {
  const { bytes, kept } = cleanImage(png());
  const chunks = pngChunks(bytes);

  it('drops personal text and time, keeps AI parameters and C2PA', () => {
    expect(has(bytes, 'Jane')).toBe(false);
    expect(chunks.map((c) => c.type)).not.toContain('tIME');
    expect(has(bytes, 'parameters')).toBe(true);
    expect(chunks.map((c) => c.type)).toContain('caBX');
    expect(kept).toEqual(expect.arrayContaining(['AI generation parameters', 'Content Credentials (C2PA)', 'AI source type (IPTC)']));
  });

  it('writes valid chunk CRCs and puts XMP before image data', () => {
    for (const c of chunks) {
      const stored = new DataView(bytes.buffer, bytes.byteOffset + c.end - 4, 4).getUint32(0);
      expect(stored).toBe(crc32(bytes.subarray(c.start + 4, c.end - 4)));
    }
    const types = chunks.map((c) => c.type);
    expect(types.indexOf('iTXt')).toBeLessThan(types.indexOf('IDAT'));
  });
});

describe('cleanImage WebP', () => {
  const { bytes, removed } = cleanImage(webp());
  const chunks = webpChunks(bytes);

  it('removes EXIF and XMP and clears their VP8X flags', () => {
    expect(chunks.map((c) => c.type)).toEqual(['VP8X', 'VP8L']);
    expect(chunks[0].data[0] & 0x0c).toBe(0);
    expect(has(bytes, 'Pixel') || has(bytes, 'Jane')).toBe(false);
    expect(removed).toEqual(expect.arrayContaining(['GPS location', 'XMP (editing history, names, tools)']));
  });

  it('writes a correct RIFF size', () => {
    expect(new DataView(bytes.buffer, bytes.byteOffset).getUint32(4, true)).toBe(bytes.length - 8);
  });
});

describe('cleanImage other formats', () => {
  it('rejects HEIC', () => {
    const heic = concat([bin('\0\0\0\x18ftypheic'), new Uint8Array(32)]);
    expect(() => cleanImage(heic)).toThrow(UnsupportedFormat);
  });

  it('is a no-op for already clean images', () => {
    const bare = concat([Uint8Array.from([0xff, 0xd8]), seg(0xdb, new Uint8Array(65)), SCAN]);
    const r = cleanImage(bare);
    expect(latin1(r.bytes)).toBe(latin1(bare));
    expect(r.removed).toEqual([]);
  });
});
