// Split image files into their container parts (JPEG segments, PNG chunks, WebP RIFF chunks).
import { ascii, latin1, u16be, u32be, u32le } from './binary';

export type Format = 'jpeg' | 'png' | 'webp' | 'heic' | 'avif' | 'unknown';

export function detectFormat(b: Uint8Array): Format {
  if (b[0] === 0xff && b[1] === 0xd8 && b[2] === 0xff) return 'jpeg';
  if (ascii(b, 0, 8) === '\x89PNG\r\n\x1a\n') return 'png';
  if (ascii(b, 0, 4) === 'RIFF' && ascii(b, 8, 4) === 'WEBP') return 'webp';
  if (ascii(b, 4, 4) === 'ftyp') {
    const brands = ascii(b, 8, Math.min(32, b.length - 8));
    if (/avif|avis/.test(brands)) return 'avif';
    if (/hei[cx]|hevc|mif1|msf1/.test(brands)) return 'heic';
  }
  return 'unknown';
}

export interface JpegSegment {
  marker: number; // second marker byte, e.g. 0xe1 for APP1
  start: number; // offset of the 0xFF marker byte
  end: number; // exclusive
  data: Uint8Array; // payload after the length field (empty for standalone markers)
}

/**
 * Header segments up to and including SOS, followed by one pseudo-segment (marker 0) holding
 * the entropy-coded image data up to and including EOI. Anything after EOI is `trailing`.
 */
export function jpegSegments(b: Uint8Array): { segments: JpegSegment[]; trailing: Uint8Array } {
  const segments: JpegSegment[] = [{ marker: 0xd8, start: 0, end: 2, data: new Uint8Array() }];
  let o = 2;
  while (o < b.length) {
    if (b[o] !== 0xff) throw new Error('Corrupt JPEG: expected a marker.');
    const marker = b[o + 1];
    if (marker === 0xff) {
      o++; // fill byte
      continue;
    }
    if ((marker >= 0xd0 && marker <= 0xd7) || marker === 0x01) {
      segments.push({ marker, start: o, end: o + 2, data: new Uint8Array() });
      o += 2;
      continue;
    }
    const len = u16be(b, o + 2);
    const end = o + 2 + len;
    segments.push({ marker, start: o, end, data: b.subarray(o + 4, end) });
    o = end;
    if (marker === 0xda) break; // start of scan
  }
  // The scan data ends at the first FF D9: inside entropy data 0xFF is always followed by 00 or a
  // restart/marker byte, so FF D9 can only be the real end of image (also for progressive JPEGs).
  let eoi = -1;
  for (let i = o; i < b.length - 1; i++) {
    if (b[i] === 0xff && b[i + 1] === 0xd9) {
      eoi = i + 2;
      break;
    }
  }
  if (eoi === -1) eoi = b.length;
  segments.push({ marker: 0, start: o, end: eoi, data: b.subarray(o, eoi) });
  return { segments, trailing: b.subarray(eoi) };
}

export interface Chunk {
  type: string;
  start: number;
  end: number;
  data: Uint8Array;
}

export function pngChunks(b: Uint8Array): Chunk[] {
  const chunks: Chunk[] = [];
  let o = 8;
  while (o + 12 <= b.length) {
    const len = u32be(b, o);
    const type = ascii(b, o + 4, 4);
    const end = o + 12 + len;
    chunks.push({ type, start: o, end, data: b.subarray(o + 8, o + 8 + len) });
    o = end;
    if (type === 'IEND') break;
  }
  return chunks;
}

export function webpChunks(b: Uint8Array): Chunk[] {
  const chunks: Chunk[] = [];
  const riffEnd = Math.min(b.length, 8 + u32le(b, 4));
  let o = 12;
  while (o + 8 <= riffEnd) {
    const type = ascii(b, o, 4);
    const len = u32le(b, o + 4);
    const end = o + 8 + len + (len & 1);
    chunks.push({ type, start: o, end, data: b.subarray(o + 8, o + 8 + len) });
    o = end;
  }
  return chunks;
}

/** PNG tEXt / zTXt / iTXt → { keyword, text }. Compressed text is inflated with `inflate`. */
export function pngText(c: Chunk, inflate: (d: Uint8Array) => Uint8Array): { keyword: string; text: string } | null {
  const d = c.data;
  const nul = d.indexOf(0);
  if (nul < 0) return null;
  const keyword = ascii(d, 0, nul);
  const dec = (x: Uint8Array, utf: boolean) => (utf ? new TextDecoder().decode(x) : latin1(x));
  try {
    if (c.type === 'tEXt') return { keyword, text: dec(d.subarray(nul + 1), false) };
    if (c.type === 'zTXt') return { keyword, text: dec(inflate(d.subarray(nul + 2)), false) };
    if (c.type === 'iTXt') {
      const compressed = d[nul + 1] === 1;
      let p = nul + 3;
      p = d.indexOf(0, p) + 1; // language tag
      p = d.indexOf(0, p) + 1; // translated keyword
      const body = d.subarray(p);
      return { keyword, text: dec(compressed ? inflate(body) : body, true) };
    }
  } catch {
    return { keyword, text: '' };
  }
  return null;
}

/** Reads the Orientation tag (0x0112) from IFD0 of a TIFF/EXIF block. Returns 1 when absent. */
export function tiffOrientation(tiff: Uint8Array): number {
  if (tiff.length < 8) return 1;
  const le = tiff[0] === 0x49;
  const r16 = (o: number) => (le ? tiff[o] | (tiff[o + 1] << 8) : (tiff[o] << 8) | tiff[o + 1]);
  const r32 = (o: number) => (le ? u32le(tiff, o) : u32be(tiff, o));
  const ifd = r32(4);
  if (ifd + 2 > tiff.length) return 1;
  const count = r16(ifd);
  for (let i = 0; i < count; i++) {
    const e = ifd + 2 + i * 12;
    if (e + 12 > tiff.length) break;
    if (r16(e) === 0x0112) return r16(e + 8) || 1;
  }
  return 1;
}

/** True if IFD0 of a TIFF/EXIF block points to a GPS IFD (tag 0x8825). */
export function tiffHasGps(tiff: Uint8Array): boolean {
  if (tiff.length < 8) return false;
  const le = tiff[0] === 0x49;
  const r16 = (o: number) => (le ? tiff[o] | (tiff[o + 1] << 8) : (tiff[o] << 8) | tiff[o + 1]);
  const ifd = le ? u32le(tiff, 4) : u32be(tiff, 4);
  if (ifd + 2 > tiff.length) return false;
  const count = r16(ifd);
  for (let i = 0; i < count; i++) {
    const e = ifd + 2 + i * 12;
    if (e + 12 > tiff.length) break;
    if (r16(e) === 0x8825) return true;
  }
  return false;
}

export const EXIF_HEADER = 'Exif\0\0';
export const XMP_HEADER = 'http://ns.adobe.com/xap/1.0/\0';
export const XMP_EXT_HEADER = 'http://ns.adobe.com/xmp/extension/\0';
