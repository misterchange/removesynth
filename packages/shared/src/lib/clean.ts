// Privacy cleaner: removes personal metadata (location, device, dates, names, previews) from
// JPEG, PNG and WebP files without re-encoding the image. AI-provenance markers are kept on
// purpose: Content Credentials (C2PA), the IPTC digital source type, AI credit lines and
// local-generator parameters stay in the file.
import { ascii, concat, crc32, latin1 } from './binary';
import {
  detectFormat,
  jpegSegments,
  pngChunks,
  pngText,
  tiffHasGps,
  tiffOrientation,
  webpChunks,
  EXIF_HEADER,
  XMP_HEADER,
} from './containers';
import { unzlibSync, zipSync } from 'fflate';

export function downloadBlob(blob: Blob, name: string): void {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = name;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  setTimeout(() => URL.revokeObjectURL(url), 2000);
}

export async function downloadZip(files: { name: string; blob: Blob }[], zipName = 'clean-files.zip'): Promise<void> {
  const zipData: Record<string, Uint8Array> = {};
  for (const f of files) {
    zipData[f.name] = new Uint8Array(await f.blob.arrayBuffer());
  }
  const zipped = zipSync(zipData);
  const zipBlob = new Blob([zipped], { type: 'application/zip' });
  downloadBlob(zipBlob, zipName);
}

export interface CleanResult {
  bytes: Uint8Array;
  removed: string[];
  kept: string[];
}

export class UnsupportedFormat extends Error {}

const enc = (s: string) => new TextEncoder().encode(s);
const bin = (s: string) => Uint8Array.from(s, (c) => c.charCodeAt(0));

/** A big-endian TIFF block whose only entry is Orientation, so photos still display upright. */
export function orientationTiff(orientation: number): Uint8Array {
  return Uint8Array.from([
    0x4d, 0x4d, 0x00, 0x2a, 0x00, 0x00, 0x00, 0x08, // header, IFD0 at 8
    0x00, 0x01, // 1 entry
    0x01, 0x12, 0x00, 0x03, 0x00, 0x00, 0x00, 0x01, orientation >> 8, orientation & 0xff, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, // no next IFD
  ]);
}

/** Pull out the AI-provenance values worth keeping from an XMP packet. */
export function provenanceFromXmp(xmp: string): { sourceType?: string; credit?: string } {
  const pick = (name: string) => {
    const re = new RegExp(`${name}\\s*=\\s*"([^"]*)"|${name}>\\s*(?:<rdf:(?:Alt|Seq|Bag)>\\s*<rdf:li[^>]*>)?([^<]+)<`, 'i');
    const m = xmp.match(re);
    return (m?.[1] ?? m?.[2])?.trim() || undefined;
  };
  const sourceType = pick('Iptc4xmpExt:DigitalSourceType');
  const credit = pick('photoshop:Credit');
  return { sourceType, credit: credit && /\bAI\b/i.test(credit) ? credit : undefined };
}

const xmlEscape = (s: string) => s.replace(/&/g, '\&amp;').replace(/"/g, '\&quot;').replace(/</g, '\&lt;');

export function minimalXmp(p: { sourceType?: string; credit?: string }): string | undefined {
  if (!p.sourceType && !p.credit) return undefined;
  const attrs = [
    p.sourceType && `Iptc4xmpExt:DigitalSourceType=\"${xmlEscape(p.sourceType)}\"`,
    p.credit && `photoshop:Credit=\"${xmlEscape(p.credit)}\"`,
  ].filter(Boolean) as string[];
  return (
    '<?xpacket begin=\"﻿\" id=\"W5M0MpCehiHzreSzNTczkc9d\"?>' +
    '<x:xmpmeta xmlns:x=\"adobe:ns:meta/\">' +
    '<rdf:RDF xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">' +
    `<rdf:Description rdf:about=\"\" xmlns:Iptc4xmpExt=\"http://iptc.org/std/Iptc4xmpExt/2008-02-29/\" xmlns:photoshop=\"http://ns.adobe.com/photoshop/1.0/\" ${attrs.join(' ')}/>` +
    '</rdf:RDF></x:xmpmeta><?xpacket end=\"w\"?>'
  );
}

function jpegSegment(marker: number, payload: Uint8Array): Uint8Array {
  const len = payload.length + 2;
  return concat([Uint8Array.from([0xff, marker, len >> 8, len & 0xff]), payload]);
}

function cleanJpeg(b: Uint8Array): CleanResult {
  const { segments, trailing } = jpegSegments(b);
  const removed = new Set<string>();
  const kept = new Set<string>();
  const out: Uint8Array[] = [];
  let orientation = 1;
  let provenance: ReturnType<typeof provenanceFromXmp> = {};

  for (const s of segments) {
    const head = latin1(s.data.subarray(0, 36));
    const raw = b.subarray(s.start, s.end);
    const isApp = s.marker >= 0xe0 && s.marker <= 0xef;

    if (s.marker === 0xe1 && head.startsWith(EXIF_HEADER)) {
      const tiff = s.data.subarray(EXIF_HEADER.length);
      orientation = tiffOrientation(tiff);
      removed.add('EXIF (camera, settings, dates)');
      if (tiffHasGps(tiff)) removed.add('GPS location');
      continue;
    }
    if (s.marker === 0xe1 && head.startsWith(XMP_HEADER)) {
      provenance = { ...provenance, ...provenanceFromXmp(new TextDecoder().decode(s.data.subarray(XMP_HEADER.length))) };
      removed.add('XMP (editing history, names, tools)');
      continue;
    }
    if (s.marker === 0xe0 && head.startsWith('JFIF')) {
      out.push(raw);
      continue;
    }
    if (s.marker === 0xe2 && head.startsWith('ICC_PROFILE')) {
      out.push(raw);
      kept.add('Color profile');
      continue;
    }
    if (s.marker === 0xeb) {
      out.push(raw);
      kept.add('Content Credentials (C2PA)');
      continue;
    }
    if (s.marker === 0xee && head.startsWith('Adobe')) {
      out.push(raw);
      continue;
    }
    if (s.marker === 0xed) {
      removed.add('IPTC (names, captions, places)');
      continue;
    }
    if (s.marker === 0xfe) {
      removed.add('Comments');
      continue;
    }
    if (isApp) {
      removed.add('Maker and app data');
      continue;
    }
    out.push(raw);
  }

  const extra: Uint8Array[] = [];
  if (orientation !== 1) {
    extra.push(jpegSegment(0xe1, concat([bin(EXIF_HEADER), orientationTiff(orientation)])));
    kept.add('Orientation');
  }
  const xmp = minimalXmp(provenance);
  if (xmp) {
    extra.push(jpegSegment(0xe1, concat([bin(XMP_HEADER), enc(xmp)])));
    if (provenance.sourceType) kept.add('AI source type (IPTC)');
    if (provenance.credit) kept.add('AI credit line');
  }
  const insertAt = out.length > 1 && out[1][1] === 0xe0 ? 2 : 1;
  out.splice(insertAt, 0, ...extra);

  if (trailing.length > 0) removed.add('Embedded extra images (previews, depth or HDR maps)');
  return { bytes: concat(out), removed: [...removed], kept: [...kept] };
}

function pngChunk(type: string, data: Uint8Array): Uint8Array {
  const td = concat([bin(type), data]);
  const crc = crc32(td);
  const len = data.length;
  return concat([
    Uint8Array.from([len >>> 24, (len >>> 16) & 0xff, (len >>> 8) & 0xff, len & 0xff]),
    td,
    Uint8Array.from([crc >>> 24, (crc >>> 16) & 0xff, (crc >>> 8) & 0xff, crc & 0xff]),
  ]);
}

const PNG_KEEP = new Set(['IHDR', 'PLTE', 'IDAT', 'IEND', 'tRNS', 'gAMA', 'cHRM', 'sRGB', 'iCCP', 'sBIT', 'pHYs', 'bKGD', 'acTL', 'fcTL', 'fdAT', 'cICP', 'mDCv', 'cLLi']);
const PNG_AI_TEXT = new Set(['parameters', 'prompt', 'workflow', 'invokeai_metadata', 'sd-metadata', 'dream']);

function cleanPng(b: Uint8Array): CleanResult {
  const removed = new Set<string>();
  const kept = new Set<string>();
  const out: Uint8Array[] = [b.subarray(0, 8)];
  let provenance: ReturnType<typeof provenanceFromXmp> = {};
  let xmpIndex = -1;

  for (const c of pngChunks(b)) {
    const raw = b.subarray(c.start, c.end);
    if (PNG_KEEP.has(c.type)) {
      if (c.type === 'iCCP') kept.add('Color profile');
      if (c.type === 'IDAT' && xmpIndex < 0) xmpIndex = out.length;
      out.push(raw);
      continue;
    }
    if (c.type === 'caBX') {
      out.push(raw);
      kept.add('Content Credentials (C2PA)');
      continue;
    }
    if (c.type === 'tEXt' || c.type === 'zTXt' || c.type === 'iTXt') {
      const t = pngText(c, (d) => unzlibSync(d));
      if (t?.keyword === 'XML:com.adobe.xmp') {
        provenance = { ...provenance, ...provenanceFromXmp(t.text) };
        removed.add('XMP (editing history, names, tools)');
      } else if (t && PNG_AI_TEXT.has(t.keyword.toLowerCase())) {
        out.push(raw);
        kept.add('AI generation parameters');
      } else {
        removed.add('Text fields (author, comments, dates)');
      }
      continue;
    }
    if (c.type === 'eXIf') removed.add('EXIF (camera, settings, dates)');
    else if (c.type === 'tIME') removed.add('Modification time');
    else removed.add(`Other data (${c.type})`);
  }

  const xmp = minimalXmp(provenance);
  if (xmp) {
    const data = concat([bin('XML:com.adobe.xmp'), Uint8Array.from([0, 0, 0, 0, 0]), enc(xmp)]);
    out.splice(xmpIndex < 0 ? 2 : xmpIndex, 0, pngChunk('iTXt', data));
    if (provenance.sourceType) kept.add('AI source type (IPTC)');
    if (provenance.credit) kept.add('AI credit line');
  }
  return { bytes: concat(out), removed: [...removed], kept: [...kept] };
}

function webpChunk(type: string, data: Uint8Array): Uint8Array {
  const len = data.length;
  const pad = len & 1 ? Uint8Array.from([0]) : new Uint8Array();
  return concat([bin(type), Uint8Array.from([len & 0xff, (len >>> 8) & 0xff, (len >>> 16) & 0xff, (len >>> 24) & 0xff]), data, pad]);
}

function cleanWebp(b: Uint8Array): CleanResult {
  const removed = new Set<string>();
  const kept = new Set<string>();
  const chunks = webpChunks(b);
  let orientation = 1;
  let provenance: ReturnType<typeof provenanceFromXmp> = {};
  const body: { type: string; bytes: Uint8Array }[] = [];

  for (const c of chunks) {
    if (c.type === 'EXIF') {
      const tiff = ascii(c.data, 0, 6) === EXIF_HEADER ? c.data.subarray(6) : c.data;
      orientation = tiffOrientation(tiff);
      removed.add('EXIF (camera, settings, dates)');
      if (tiffHasGps(tiff)) removed.add('GPS location');
      continue;
    }
    if (c.type === 'XMP ') {
      provenance = { ...provenance, ...provenanceFromXmp(new TextDecoder().decode(c.data)) };
      removed.add('XMP (editing history, names, tools)');
      continue;
    }
    if (c.type === 'ICCP') kept.add('Color profile');
    if (c.type === 'C2PA') kept.add('Content Credentials (C2PA)');
    body.push({ type: c.type, bytes: b.subarray(c.start, c.end) });
  }

  const tail: Uint8Array[] = [];
  if (orientation !== 1) {
    tail.push(webpChunk('EXIF', orientationTiff(orientation)));
    kept.add('Orientation');
  }
  const xmp = minimalXmp(provenance);
  if (xmp) {
    tail.push(webpChunk('XMP ', enc(xmp)));
    if (provenance.sourceType) kept.add('AI source type (IPTC)');
    if (provenance.credit) kept.add('AI credit line');
  }

  const parts = body.map((c) => {
    if (c.type !== 'VP8X') return c.bytes;
    const copy = c.bytes.slice();
    let flags = copy[8] & ~0x0c;
    if (orientation !== 1) flags |= 0x08;
    if (xmp) flags |= 0x04;
    copy[8] = flags;
    return copy;
  });
  const payload = concat([bin('WEBP'), ...parts, ...tail]);
  const size = payload.length;
  const header = concat([bin('RIFF'), Uint8Array.from([size & 0xff, (size >>> 8) & 0xff, (size >>> 16) & 0xff, (size >>> 24) & 0xff])]);
  return { bytes: concat([header, payload]), removed: [...removed], kept: [...kept] };
}

export function cleanImage(b: Uint8Array): CleanResult {
  const format = detectFormat(b);
  if (format === 'jpeg') return cleanJpeg(b);
  if (format === 'png') return cleanPng(b);
  if (format === 'webp') return cleanWebp(b);
  throw new UnsupportedFormat(format);
}

import { reverseSynthID } from './reverseSynthID';
import { reverseSynthIDText, cleanTextFile } from './reverseSynthIDText';
import { cleanVideoFile } from './reverseSynthIDVideo';
import { cleanAudioFile } from './reverseSynthIDAudio';

export { reverseSynthID, reverseSynthIDText, cleanTextFile, cleanVideoFile, cleanAudioFile };

export interface CleanProgress {
  stripped: string[];
  kept: string[];
}

/** Options for cleaning – all flags default to true (run automatically). */
export interface CleanOptions {
  /** Run pixel‑level SynthID removal on images. */
  removeSynthID?: boolean;
  /** Run text‑level SynthID removal. */
  removeSynthIDText?: boolean;
  /** Run audio SynthID removal. */
  removeSynthIDAudio?: boolean;
  /** Privacy options for image metadata. */
  aiOnly?: boolean;
  stripAll?: boolean;
}

/** Unified entry point – defaults make every supported file type automatically cleaned. */
export async function cleanAnyFile(
  file: File,
  opts: CleanOptions = { removeSynthID: true, removeSynthIDText: true, removeSynthIDAudio: true }
): Promise<{ blob: Blob; progress: CleanProgress }> {
  const mime = (file.type || '').toLowerCase();
  const name = (file.name || '').toLowerCase();
  const isVideo = mime.startsWith('video/') || /\.(mp4|mov|webm|mkv)$/i.test(name);
  const isAudio = mime.startsWith('audio/') || /\.(mp3|wav|ogg|flac|m4a)$/i.test(name);
  const isText = mime.startsWith('text/') || /\.(txt|md|json|csv|log)$/i.test(name);

  if (isVideo) {
    return await cleanVideoFile(file, { removeSynthID: opts.removeSynthID ?? true });
  }
  if (isAudio) {
    return await cleanAudioFile(file, { removeSynthIDAudio: opts.removeSynthIDAudio ?? true });
  }
  if (isText) {
    return await cleanTextFile(file, { removeSynthIDText: opts.removeSynthIDText ?? true });
  }
  // Image pipeline
  return await cleanFile(file, opts);
}

/** Image pipeline – defaults run SynthID filter automatically. */
export async function cleanFile(
  file: File,
  options: CleanOptions = { removeSynthID: true, removeSynthIDText: true, removeSynthIDAudio: true }
): Promise<{ blob: Blob; progress: CleanProgress }> {
  const buf = new Uint8Array(await file.arrayBuffer());
  const res = cleanImage(buf);

  let finalBytes = res.bytes;
  const removed = [...res.removed];
  const kept = [...res.kept];

  if (options.removeSynthID ?? true) {
    finalBytes = await reverseSynthID(res.bytes, 0.85, file.type || 'image/jpeg');
    removed.push('DeepMind SynthID carrier frequency pattern (48x88 grid)');
    removed.push('SynthID pixel steganographic watermark');
  }

  const blob = new Blob([finalBytes], { type: file.type || 'image/jpeg' });
  return {
    blob,
    progress: {
      stripped: removed,
      kept,
    },
  };
}

