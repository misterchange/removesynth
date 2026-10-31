import { describe, expect, it } from 'vitest';
import { fitToSize } from './fit';

// Fake JPEG-like encoder: size grows with pixels and quality.
const fake = (pixels: number, floor = 600) => {
  const calls: [number, number][] = [];
  const encode = async (scale: number, quality: number) => {
    calls.push([scale, quality]);
    return { size: Math.round(floor + pixels * scale * scale * (0.05 + quality * 0.45)) };
  };
  return { encode, calls };
};

describe('fitToSize', () => {
  it('returns max quality when it already fits', async () => {
    const { encode } = fake(10_000);
    const r = await fitToSize(encode, 1_000_000);
    expect(r).toMatchObject({ fits: true, scale: 1, quality: 0.92 });
  });

  it('finds the highest quality under the target without resizing', async () => {
    const { encode } = fake(1_000_000); // ~350 KB at q=0.6
    const r = await fitToSize(encode, 300_000);
    expect(r.fits).toBe(true);
    expect(r.scale).toBe(1);
    expect(r.out.size).toBeLessThanOrEqual(300_000);
    expect(r.out.size).toBeGreaterThan(300_000 * 0.97); // close to the target, not far under
  });

  it('shrinks the image when even low quality is too big', async () => {
    const { encode } = fake(12_000_000); // a 12 MP photo
    const r = await fitToSize(encode, 20_000);
    expect(r.fits).toBe(true);
    expect(r.scale).toBeLessThan(1);
    expect(r.out.size).toBeLessThanOrEqual(20_000);
  });

  it('reports the smallest attempt when the target is impossible', async () => {
    const { encode } = fake(1_000_000, 5_000); // fixed 5 KB overhead
    const r = await fitToSize(encode, 1_000);
    expect(r.fits).toBe(false);
    expect(r.out.size).toBeGreaterThan(1_000);
  });

  it('stays within a small number of encodes', async () => {
    const { encode, calls } = fake(12_000_000);
    await fitToSize(encode, 50_000);
    expect(calls.length).toBeLessThan(40);
  });
});
