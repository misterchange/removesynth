// Read-only inspection of image metadata: AI provenance markers and privacy-sensitive fields.
import exifr from 'exifr';
import { unzlibSync } from 'fflate';
import { concat, indexOf, latin1, u16be } from './binary';
import {
  detectFormat,
  jpegSegments,
  pngChunks,
  pngText,
  webpChunks,
  XMP_HEADER,
  type Format,
} from './containers';

export interface Finding {
  label: string;
  value: string;
  /** 'ai' marks generative-AI provenance; 'camera' marks a declared camera capture. */
  tone?: 'ai' | 'camera';
}

export interface Report {
  format: Format;
  c2pa: { present: boolean; generator?: string; sourceType?: string };
  ai: Finding[];
  privacy: Finding[];
  otherFields: number;
}

export const SOURCE_TYPES: Record<string, { text: string; tone: 'ai' | 'camera' }> = {
  trainedAlgorithmicMedia: { text: 'Created with generative AI', tone: 'ai' },
  compositeWithTrainedAlgorithmicMedia: { text: 'Edited with generative AI', tone: 'ai' },
  algorithmicMedia: { text: 'Created by an algorithm', tone: 'ai' },
  compositeSynthetic: { text: 'Contains synthetic elements', tone: 'ai' },
  digitalCapture: { text: 'Captured with a digital camera', tone: 'camera' },
  computationalCapture: { text: 'Captured with computational photography', tone: 'camera' },
};

const AI_NAMES =
  /(made with google ai|edited with google ai|imagined with ai|midjourney|dall[·\-\s]?e|openai|chatgpt|gpt-?4o|firefly|stable diffusion|stablediffusion|sdxl|comfyui|automatic1111|invokeai|novelai|imagen|gemini|meta ai|leonardo\.ai|ideogram|flux|bing image creator|microsoft designer|grok|aurora|runway|kling|veo|nano banana)/i;

// PNG text keywords written by local image generators.
const PNG_AI_KEYS: Record<string, string> = {
  parameters: 'Stable Diffusion parameters (A1111 / Forge)',
  prompt: 'ComfyUI prompt',
  workflow: 'ComfyUI workflow',
  invokeai_metadata: 'InvokeAI metadata',
  'sd-metadata': 'Stable Diffusion metadata',
  dream: 'Stable Diffusion (Dream) prompt',
};

const short = (s: string, n = 140) => (s.length > n ? `${s.slice(0, n).trim()}…` : s.trim());

/** Read a CBOR text string at offset p. Returns undefined if p isn't a text string. */
function cborText(b: Uint8Array, p: number): string | undefined {
  const h = b[p];
  if (h >> 5 !== 3) return undefined;
  let len = h & 31;
  let start = p + 1;
  if (len === 24) [len, start] = [b[p + 1], p + 2];
  else if (len === 25) [len, start] = [u16be(b, p + 1), p + 3];
  else if (len > 25) return undefined;
  return new TextDecoder().decode(b.subarray(start, start + len));
}

function readC2pa(m: Uint8Array): Report['c2pa'] {
  if (indexOf(m, 'c2pa') < 0) return { present: false };
  let generator: string | undefined;
  // v2 manifests: claim_generator_info: [{ name: "..." }]
  const info = indexOf(m, '\x74claim_generator_info');
  if (info >= 0) {
    const name = indexOf(m, '\x64name', info);
    if (name >= 0 && name - info < 64) generator = cborText(m, name + 5);
  }
  // v1 manifests: claim_generator: "Name/1.0 ..."
  if (!generator) {
    const g = indexOf(m, '\x6fclaim_generator');
    if (g >= 0) generator = cborText(m, g + 16);
  }
  const text = latin1(m);
  const st = Object.keys(SOURCE_TYPES).find((k) => text.includes(`digitalsourcetype/${k}`));
  return { present: true, generator: generator?.trim() || undefined, sourceType: st };
}

/** Collect the raw XMP, EXIF and C2PA blocks plus PNG text chunks from the container. */
function extract(b: Uint8Array, format: Format) {
  const xmp: string[] = [];
  const pngTexts: { keyword: string; text: string }[] = [];
  let c2pa = new Uint8Array();
  const inflate = (d: Uint8Array) => unzlibSync(d);

  if (format === 'jpeg') {
    const { segments } = jpegSegments(b);
    const app11: Uint8Array[] = [];
    for (const s of segments) {
      const head = latin1(s.data.subarray(0, 40));
      if (s.marker === 0xe1 && head.startsWith(XMP_HEADER)) xmp.push(new TextDecoder().decode(s.data.subarray(XMP_HEADER.length)));
      if (s.marker === 0xeb) app11.push(s.data);
    }
    c2pa = concat(app11);
  } else if (format === 'png') {
    for (const c of pngChunks(b)) {
      if (c.type === 'caBX') c2pa = concat([c2pa, c.data]);
      if (c.type === 'tEXt' || c.type === 'zTXt' || c.type === 'iTXt') {
        const t = pngText(c, inflate);
        if (!t) continue;
        if (t.keyword === 'XML:com.adobe.xmp') xmp.push(t.text);
        else pngTexts.push(t);
      }
    }
  } else if (format === 'webp') {
    for (const c of webpChunks(b)) {
      if (c.type === 'XMP ') xmp.push(new TextDecoder().decode(c.data));
      if (c.type === 'C2PA') c2pa = concat([c2pa, c.data]);
    }
  } else {
    // HEIC/AVIF and anything else: fall back to scanning the whole file.
    const text = latin1(b);
    const start = text.indexOf('<x:xmpmeta');
    const end = text.indexOf('</x:xmpmeta>', start);
    if (start >= 0 && end > start) xmp.push(new TextDecoder().decode(b.subarray(start, end + 12)));
    if (indexOf(b, 'jumb') >= 0) c2pa = b;
  }
  return { xmp: xmp.join('\n'), pngTexts, c2pa };
}

function xmpValue(xmp: string, name: string): string | undefined {
  const re = new RegExp(`${name}\\s*=\\s*"([^"]*)"|${name}>\\s*(?:<rdf:(?:Alt|Seq|Bag)>\\s*<rdf:li[^>]*>)?([^<]+)<`, 'i');
  const m = xmp.match(re);
  return (m?.[1] ?? m?.[2])?.trim() || undefined;
}

const PRIVACY_FIELDS: [string[], string][] = [
  [['Make', 'Model'], 'Camera / phone'],
  [['LensModel'], 'Lens'],
  [['BodySerialNumber', 'SerialNumber', 'LensSerialNumber', 'InternalSerialNumber'], 'Serial number'],
  [['DateTimeOriginal', 'CreateDate'], 'Date taken'],
  [['Artist', 'CameraOwnerName', 'OwnerName', 'Byline', 'creator'], 'Name of creator / owner'],
  [['Copyright', 'CopyrightNotice', 'rights'], 'Copyright'],
  [['City', 'Sublocation', 'State', 'Country', 'ProvinceState'], 'Place name'],
  [['HostComputer'], 'Computer'],
  [['Software', 'CreatorTool'], 'Software'],
];

function fmt(v: unknown): string {
  if (v instanceof Date) return v.toISOString().slice(0, 19).replace('T', ' ');
  if (Array.isArray(v)) return v.map(fmt).join(', ');
  if (v && typeof v === 'object') return 'value' in v ? fmt((v as { value: unknown }).value) : JSON.stringify(v);
  return String(v);
}

export async function inspect(bytes: Uint8Array): Promise<Report> {
  const format = detectFormat(bytes);
  const { xmp, pngTexts, c2pa: manifest } = extract(bytes, format);
  const c2pa = readC2pa(manifest);
  const ai: Finding[] = [];
  const privacy: Finding[] = [];

  let tags: Record<string, unknown> = {};
  try {
    tags =
      (await exifr.parse(bytes, {
        tiff: true,
        exif: true,
        gps: true,
        xmp: true,
        iptc: true,
        icc: false,
        jfif: false,
        ihdr: false,
        interop: false,
        mergeOutput: true,
        translateValues: true,
        reviveValues: true,
      })) ?? {};
  } catch {
    tags = {};
  }
  const get = (k: string) => {
    const key = Object.keys(tags).find((t) => t.toLowerCase() === k.toLowerCase());
    return key ? tags[key] : undefined;
  };

  // --- AI provenance ---
  if (c2pa.present) {
    const st = c2pa.sourceType && SOURCE_TYPES[c2pa.sourceType];
    ai.push({
      label: 'Content Credentials (C2PA)',
      value: [c2pa.generator && `Made with ${c2pa.generator}`, st && st.text].filter(Boolean).join(' · ') || 'Manifest present',
      tone: st?.tone === 'camera' ? 'camera' : 'ai',
    });
  }

  const dst = xmpValue(xmp, 'DigitalSourceType') ?? fmt(get('DigitalSourceType') ?? '');
  const dstKey = Object.keys(SOURCE_TYPES).find((k) => dst.endsWith(`/${k}`) || dst === k);
  if (dstKey) {
    ai.push({ label: 'IPTC digital source type', value: SOURCE_TYPES[dstKey].text, tone: SOURCE_TYPES[dstKey].tone });
  }

  const nameFields: [string, string | undefined][] = [
    ['XMP credit', xmpValue(xmp, 'photoshop:Credit')],
    ['XMP creator tool', xmpValue(xmp, 'xmp:CreatorTool')],
    ['EXIF software', get('Software') ? fmt(get('Software')) : undefined],
    ['EXIF description', get('ImageDescription') ? fmt(get('ImageDescription')) : undefined],
    ['EXIF user comment', get('UserComment') ? fmt(get('UserComment')) : undefined],
  ];
  for (const [label, value] of nameFields) {
    if (value && AI_NAMES.test(value)) ai.push({ label, value: short(value), tone: 'ai' });
  }

  for (const t of pngTexts) {
    const known = PNG_AI_KEYS[t.keyword.toLowerCase()];
    if (known) ai.push({ label: known, value: short(t.text), tone: 'ai' });
    else if (AI_NAMES.test(t.text) || AI_NAMES.test(t.keyword)) ai.push({ label: `PNG text “${t.keyword}”`, value: short(t.text), tone: 'ai' });
  }

  // --- Privacy ---
  const lat = get('latitude');
  const lon = get('longitude');
  if (typeof lat === 'number' && typeof lon === 'number') {
    privacy.push({ label: 'GPS location', value: `${lat.toFixed(5)}, ${lon.toFixed(5)}` });
  }
  for (const [keys, label] of PRIVACY_FIELDS) {
    const values = keys.map(get).filter((v) => v !== undefined && v !== '').map(fmt);
    const unique = [...new Set(values)];
    if (unique.length) privacy.push({ label, value: short(unique.join(' · '), 100) });
  }
  const genericPng = pngTexts.filter((t) => !PNG_AI_KEYS[t.keyword.toLowerCase()]);
  for (const t of genericPng) {
    if (/author|comment|description|title|copyright|source/i.test(t.keyword)) {
      privacy.push({ label: `PNG text “${t.keyword}”`, value: short(t.text, 100) });
    }
  }

  return {
    format,
    c2pa,
    ai,
    privacy,
    otherFields: Object.keys(tags).length + pngTexts.length,
  };
}

/** True if the file declares itself as AI-generated or AI-edited anywhere. */
export const hasAiProvenance = (r: Report) => r.ai.some((f) => f.tone === 'ai');
