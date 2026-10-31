import { describe, expect, it } from 'vitest';
import { concat, crc32, indexOf, latin1 } from '@removesynth/shared/lib/binary';
import { jpegSegments, pngChunks, webpChunks } from '@removesynth/shared/lib/containers';
import { stripLabels, UnsupportedFormat } from './labelclean';

const bin = (s: string) => Uint8Array.from(s, (c) => c.charCodeAt(0));
const enc = (s: string) => new TextEncoder().encode(s);
const has = (b: Uint8Array, s: string) => indexOf(b, s) >= 0;

type Entry = { tag: number; type: 3 | 2 | 4 | 5; values: number[] | string };

function tiff(ifd0: Entry[]): Uint8Array {
  const size = (e: Entry) =>
    e.type === 2 ? (e.values as string).length + 1 : e.type === 3 ? 2 * (e.values as number[]).length : e.type === 4 ? 4 * (e.values as number[]).length : 8 * ((e.values as number[]).length / 2);
  const buf = new Uint8Array(4096);
  const dv = new DataView(buf.buffer);
  buf.set(bin('MM\0*'));
  dv.setUint32(4, 8);
  let heap = 1024;
  dv.setUint16(8, ifd0.length);
  ifd0.forEach((e, i) => {
    const p = 10 + i * 12;
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
  dv.setUint32(10 + ifd0.length * 12, 0);
  return buf.subarray(0, heap);
}

const C2PA_MANIFEST = concat([
  bin('\0\0\0\x20jumb\0\0\0\x18jumdc2pa\0'),
  bin('\x74claim_generator_info\x81\xa1\x64name\x6dAdobe Firefly'),
  bin('http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia'),
]);

const XMP_FULL =
  '<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF><rdf:Description rdf:about="">' +
  '<Iptc4xmpExt:DigitalSourceType="trainedAlgorithmicMedia"/><dc:creator>Jane Private</dc:creator>' +
  '</rdf:Description></rdf:RDF></x:xmpmeta>';

const seg = (marker: number, payload: Uint8Array) =>
  concat([Uint8Array.from([0xff, marker, (payload.length + 2) >> 8, (payload.length + 2) & 0xff]), payload]);

const SCAN = concat([seg(0xda, Uint8Array.from([1, 1, 0, 0, 0x3f, 0])), Uint8Array.from([0x12, 0xff, 0x00, 0x34]), Uint8Array.from([0xff, 0xd9])]);

function jpeg(): Uint8Array {
  return concat([
    Uint8Array.from([0xff, 0xd8]),
    seg(0xe0, bin('JFIF\0\x01\x01\0\0\x01\0\x01\0\0')),
    seg(0xe1, concat([bin('Exif\0\0'), tiff([{ tag: 0x010f, type: 2, values: 'Canon' }, { tag: 0x0110, type: 2, values: 'EOS R5' }])])),
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
  return concat([Uint8Array.from([len >>> 24, (len >> 16) & 0xff, (len >> 8) & 0xff, len & 0xff]), td, Uint8Array.from([crc >>> 24, (crc >> 16) & 0xff, (crc >> 8) & 0xff, crc & 0xff])]);
}

function png(): Uint8Array {
  return concat([
    bin('\x89PNG\r\n\x1a\n'),
    pngChunk('IHDR', Uint8Array.from([0, 0, 0, 1, 0, 0, 0, 1, 8, 2, 0, 0, 0])),
    pngChunk('tEXt', bin('Author\0Jane Private')),
    pngChunk('tEXt', bin('parameters\0a cat in space, Steps: 20, Model: sdxl')),
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
  const vp8x = Uint8Array.from([0x0c, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
  const body = concat([
    bin('WEBP'),
    webpChunk('VP8X', vp8x),
    webpChunk('VP8L', Uint8Array.from([0x2f, 0, 0, 0, 0])),
    webpChunk('EXIF', tiff([{ tag: 0x010f, type: 2, values: 'Pixel' }])),
    webpChunk('XMP ', enc('<x:xmpmeta><dc:creator>Jane Private</dc:creator></x:xmpmeta>')),
    webpChunk('C2PA', C2PA_MANIFEST),
  ]);
  const n = body.length;
  return concat([bin('RIFF'), Uint8Array.from([n & 0xff, (n >> 8) & 0xff, (n >> 16) & 0xff, n >>> 24]), body]);
}

describe('stripLabels JPEG', () => {
  const src = jpeg();
  const { bytes, removed } = stripLabels(src);

  it('removes EXIF, XMP, IPTC, comments and C2PA', () => {
    for (const s of ['Canon', 'EOS R5', 'Jane', 'shot at home', 'claim_generator_info', 'trainedAlgorithmicMedia', 'ns.adobe.com/xap', 'TRAILING']) {
      expect(has(bytes, s)).toBe(false);
    }
    expect(removed).toEqual(expect.arrayContaining(['EXIF (camera, dates, GPS)', 'XMP (prompts, editing history)', 'IPTC (captions, credits)', 'C2PA Content Credentials', 'Comments']));
  });

  it('keeps the JFIF header and the pixel data', () => {
    const segs = jpegSegments(bytes).segments;
    expect(segs[0].marker).toBe(0xd8);
    expect(segs[1].marker).toBe(0xe0);
    expect(segs.at(-1)!.data).toEqual(jpegSegments(src).segments.at(-1)!.data);
  });
});

describe('stripLabels PNG', () => {
  const { bytes } = stripLabels(png());
  const types = pngChunks(bytes).map((c) => c.type);

  it('drops text, time and C2PA while keeping image chunks', () => {
    expect(has(bytes, 'Jane')).toBe(false);
    expect(has(bytes, 'parameters')).toBe(false);
    expect(has(bytes, 'claim_generator_info')).toBe(false);
    expect(types).not.toContain('tEXt');
    expect(types).not.toContain('iTXt');
    expect(types).not.toContain('tIME');
    expect(types).not.toContain('caBX');
    expect(types).toEqual(expect.arrayContaining(['IHDR', 'IDAT', 'IEND']));
  });
});

describe('stripLabels WebP', () => {
  const { bytes } = stripLabels(webp());
  const chunks = webpChunks(bytes);

  it('removes EXIF/XMP/C2PA and clears the VP8X feature flags', () => {
    expect(chunks.map((c) => c.type)).toEqual(['VP8X', 'VP8L']);
    expect(chunks[0].data[0] & 0x0c).toBe(0);
    expect(has(bytes, 'Pixel') || has(bytes, 'Jane') || has(bytes, 'claim_generator')).toBe(false);
  });

  it('writes a correct RIFF size', () => {
    expect(new DataView(bytes.buffer, bytes.byteOffset).getUint32(4, true)).toBe(bytes.length - 8);
  });
});

describe('stripLabels other', () => {
  it('rejects HEIC', () => {
    const heic = concat([bin('\0\0\0\x18ftypheic'), new Uint8Array(32)]);
    expect(() => stripLabels(heic)).toThrow(UnsupportedFormat);
  });

  it('is a no-op for an already clean JPEG', () => {
    const bare = concat([Uint8Array.from([0xff, 0xd8]), seg(0xdb, new Uint8Array(65)), SCAN]);
    const r = stripLabels(bare);
    expect(latin1(r.bytes)).toBe(latin1(bare));
    expect(r.removed).toEqual([]);
  });
});
