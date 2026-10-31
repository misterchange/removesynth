// Browser-side image decode / encode for the compressor and converter. Everything runs locally.
import { fitToSize } from '@removesynth/shared/lib/fit';

export type OutFormat = 'jpg' | 'png' | 'webp';

export const OUT_MIME: Record<OutFormat, string> = {
  jpg: 'image/jpeg',
  png: 'image/png',
  webp: 'image/webp',
};

const isHeic = (f: File) => /\.(heic|heif)$/i.test(f.name) || /image\/hei[cf]/i.test(f.type);

/** Decode any browser-supported image (plus HEIC via heic2any), applying EXIF orientation. */
export async function decodeImage(file: File): Promise<ImageBitmap> {
  try {
    return await createImageBitmap(file, { imageOrientation: 'from-image' });
  } catch (err) {
    if (!isHeic(file)) throw err;
    // Chrome and Firefox can't decode HEIC; load the converter only when needed.
    const { default: heic2any } = await import('heic2any');
    const out = await heic2any({ blob: file, toType: 'image/png' });
    return createImageBitmap(Array.isArray(out) ? out[0] : out);
  }
}

/** Draw the bitmap at `scale`. JPG has no transparency, so transparent areas become white. */
export function render(bitmap: ImageBitmap, scale: number, opaque: boolean): HTMLCanvasElement {
  const canvas = document.createElement('canvas');
  canvas.width = Math.max(1, Math.round(bitmap.width * scale));
  canvas.height = Math.max(1, Math.round(bitmap.height * scale));
  const ctx = canvas.getContext('2d')!;
  if (opaque) {
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }
  ctx.imageSmoothingEnabled = true;
  ctx.imageSmoothingQuality = 'high';
  ctx.drawImage(bitmap, 0, 0, canvas.width, canvas.height);
  return canvas;
}

export function toBlob(canvas: HTMLCanvasElement, mime: string, quality?: number): Promise<Blob> {
  return new Promise((resolve, reject) =>
    canvas.toBlob((b) => (b ? resolve(b) : reject(new Error('Encoding failed'))), mime, quality),
  );
}

/** True if the browser can actually write this format (Safari can't write WebP everywhere). */
export async function canEncode(format: OutFormat): Promise<boolean> {
  const c = document.createElement('canvas');
  c.width = c.height = 1;
  const b = await toBlob(c, OUT_MIME[format]).catch(() => null);
  return !!b && b.type === OUT_MIME[format];
}

export interface Output {
  blob: Blob;
  width: number;
  height: number;
  quality?: number;
  fits?: boolean;
}

export async function convert(bitmap: ImageBitmap, to: OutFormat, quality = 0.92): Promise<Output> {
  const canvas = render(bitmap, 1, to === 'jpg');
  const blob = await toBlob(canvas, OUT_MIME[to], to === 'png' ? undefined : quality);
  return { blob, width: canvas.width, height: canvas.height, quality: to === 'png' ? undefined : quality };
}

/** Compress to at most `targetBytes`, lowering quality first and then dimensions. */
export async function compressTo(bitmap: ImageBitmap, targetBytes: number, to: 'jpg' | 'webp' = 'jpg'): Promise<Output> {
  const canvases = new Map<number, HTMLCanvasElement>();
  const encode = async (scale: number, quality: number) => {
    let canvas = canvases.get(scale);
    if (!canvas) {
      canvas = render(bitmap, scale, to === 'jpg');
      canvases.set(scale, canvas);
    }
    const blob = await toBlob(canvas, OUT_MIME[to], quality);
    return { size: blob.size, blob, width: canvas.width, height: canvas.height };
  };
  const r = await fitToSize(encode, targetBytes);
  return { blob: r.out.blob, width: r.out.width, height: r.out.height, quality: r.quality, fits: r.fits };
}

/** Sizes on forms are usually checked in units of 1000 bytes; using 1000 keeps us under either reading. */
export const KB = 1000;
export const formatSize = (bytes: number) =>
  bytes >= 1_000_000 ? `${(bytes / 1_000_000).toFixed(2)} MB` : `${(bytes / KB).toFixed(1)} KB`;
