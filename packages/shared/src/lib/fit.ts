// Find the best encoding that fits under a byte budget. Encoder-agnostic so it can be unit-tested:
// the caller supplies `encode(scale, quality)` (canvas in the browser, a fake in tests).

export interface Encoded {
  size: number;
}

export interface FitResult<T extends Encoded> {
  out: T;
  scale: number;
  quality: number;
  fits: boolean;
}

export interface FitOptions {
  minQuality?: number;
  maxQuality?: number;
  /** Binary-search steps per scale. 7 steps resolve quality to ~0.01. */
  steps?: number;
  /** How many times to shrink the image when even the lowest quality is too big. */
  maxRounds?: number;
  /** Never shrink below this fraction of the original dimensions. */
  minScale?: number;
}

export async function fitToSize<T extends Encoded>(
  encode: (scale: number, quality: number) => Promise<T>,
  targetBytes: number,
  { minQuality = 0.3, maxQuality = 0.92, steps = 7, maxRounds = 8, minScale = 0.02 }: FitOptions = {},
): Promise<FitResult<T>> {
  let scale = 1;
  let smallest: FitResult<T> | undefined;

  for (let round = 0; round < maxRounds; round++) {
    const top = await encode(scale, maxQuality);
    if (top.size <= targetBytes) return { out: top, scale, quality: maxQuality, fits: true };

    const bottom = await encode(scale, minQuality);
    if (!smallest || bottom.size < smallest.out.size) smallest = { out: bottom, scale, quality: minQuality, fits: false };

    if (bottom.size <= targetBytes) {
      // Largest quality in [min, max] that still fits.
      let lo = minQuality;
      let hi = maxQuality;
      let best: FitResult<T> = { out: bottom, scale, quality: minQuality, fits: true };
      for (let i = 0; i < steps; i++) {
        const q = (lo + hi) / 2;
        const out = await encode(scale, q);
        if (out.size <= targetBytes) {
          best = { out, scale, quality: q, fits: true };
          lo = q;
        } else {
          hi = q;
        }
      }
      return best;
    }

    if (scale <= minScale) break;
    // File size scales roughly with pixel count, so shrink each side by the square root of the overshoot.
    scale = Math.max(minScale, scale * Math.sqrt(targetBytes / bottom.size) * 0.92);
  }
  return smallest!;
}
