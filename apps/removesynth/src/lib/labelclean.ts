// LabelSynth cleaner: strips AI provenance and metadata from image files without re-encoding
// the pixels. Removes C2PA Content Credentials, XMP, EXIF, IPTC and PNG text chunks from
// JPEG, PNG and WebP. Colour profiles and display-critical blocks are kept.
import { ascii, concat, latin1 } from '@removesynth/shared/lib/binary';
import {
  detectFormat,
  jpegSegments,
  pngChunks,
  webpChunks,
  EXIF_HEADER,
  XMP_HEADER,
} from '@removesynth/shared/lib/containers';

export interface StripResult {
  bytes: Uint8Array;
  removed: string[];
  format: string;
}

export class UnsupportedFormat extends Error {}

const bin = (s: string) => Uint8Array.from(s, (c) => c.charCodeAt(0));

function stripJpeg(b: Uint8Array): StripResult {
  const { segments, trailing } = jpegSegments(b);
  const removed = new Set<string>();
  const out: Uint8Array[] = [];

  for (const s of segments) {
    const raw = b.subarray(s.start, s.end);
    const head = latin1(s.data.subarray(0, 40));
    const isApp = s.marker >= 0xe0 && s.marker <= 0xef;

    if (s.marker === 0xe1 && head.startsWith(EXIF_HEADER)) {
      removed.add('EXIF (camera, dates, GPS)');
      continue;
    }
    if (s.marker === 0xe1 && head.startsWith(XMP_HEADER)) {
      removed.add('XMP (prompts, editing history)');
      continue;
    }
    if (s.marker === 0xeb) {
      removed.add('C2PA Content Credentials');
      continue;
    }
    if (s.marker === 0xe0 && head.startsWith('JFIF')) {
      out.push(raw);
      continue;
    }
    if (s.marker === 0xe2 && head.startsWith('ICC_PROFILE')) {
      out.push(raw);
      continue;
    }
    if (s.marker === 0xee && head.startsWith('Adobe')) {
      out.push(raw);
      continue;
    }
    if (s.marker === 0xed) {
      removed.add('IPTC (captions, credits)');
      continue;
    }
    if (s.marker === 0xfe) {
      removed.add('Comments');
      continue;
    }
    if (isApp) {
      removed.add('Maker note and app data');
      continue;
    }
    out.push(raw);
  }

  if (trailing.length > 0) removed.add('Embedded preview images');
  return { bytes: concat(out), removed: [...removed], format: 'jpeg' };
}

const PNG_KEEP = new Set([
  'IHDR', 'PLTE', 'IDAT', 'IEND', 'tRNS', 'gAMA', 'cHRM', 'sRGB', 'iCCP', 'sBIT',
  'pHYs', 'bKGD', 'acTL', 'fcTL', 'fdAT', 'cICP', 'mDCv', 'cLLi',
]);

function stripPng(b: Uint8Array): StripResult {
  const removed = new Set<string>();
  const out: Uint8Array[] = [b.subarray(0, 8)];

  for (const c of pngChunks(b)) {
    const raw = b.subarray(c.start, c.end);
    if (PNG_KEEP.has(c.type)) {
      out.push(raw);
      continue;
    }
    if (c.type === 'caBX') {
      removed.add('C2PA Content Credentials');
      continue;
    }
    if (c.type === 'eXIf') {
      removed.add('EXIF (camera, dates, GPS)');
      continue;
    }
    if (c.type === 'tIME') {
      removed.add('Modification time');
      continue;
    }
    if (c.type === 'tEXt' || c.type === 'zTXt' || c.type === 'iTXt') {
      removed.add('PNG text (prompts, workflow, names)');
      continue;
    }
    removed.add(`Extra data (${c.type})`);
  }
  return { bytes: concat(out), removed: [...removed], format: 'png' };
}

function stripWebp(b: Uint8Array): StripResult {
  const removed = new Set<string>();
  const body: Uint8Array[] = [];

  for (const c of webpChunks(b)) {
    if (c.type === 'EXIF') {
      removed.add('EXIF (camera, dates, GPS)');
      continue;
    }
    if (c.type === 'XMP ') {
      removed.add('XMP (prompts, editing history)');
      continue;
    }
    if (c.type === 'C2PA') {
      removed.add('C2PA Content Credentials');
      continue;
    }
    body.push(b.subarray(c.start, c.end));
  }

  // Clear the EXIF/XMP feature bits in the VP8X header so players don't look for missing chunks.
  const parts = body.map((raw) => {
    if (ascii(raw, 0, 4) !== 'VP8X') return raw;
    const copy = raw.slice();
    copy[8] = copy[8] & ~0x0c;
    return copy;
  });

  const payload = concat([bin('WEBP'), ...parts]);
  const size = payload.length;
  const header = concat([bin('RIFF'), Uint8Array.from([size & 0xff, (size >> 8) & 0xff, (size >> 16) & 0xff, size >>> 24])]);
  return { bytes: concat([header, payload]), removed: [...removed], format: 'webp' };
}

/** True when at least one metadata block was found and removed. */
export function stripLabels(b: Uint8Array): StripResult {
  const format = detectFormat(b);
  if (format === 'jpeg') return stripJpeg(b);
  if (format === 'png') return stripPng(b);
  if (format === 'webp') return stripWebp(b);
  throw new UnsupportedFormat(format);
}
