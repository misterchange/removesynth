import type { Block } from '../data/registry';

export interface Hero {
  h1: string;
  lead: Block[];
  rest: Block[];
}

/** Splits a page's blocks into the H1, the lead paragraphs that follow it, and the rest. */
export function splitHero(blocks: Block[], fallbackTitle = ''): Hero {
  let title = fallbackTitle;
  let start = 0;
  const first = blocks[0];
  if (first && (first.type === 'h1' || first.type === 'h2')) {
    title = first.text;
    start = 1;
  }
  const lead: Block[] = [];
  let i = start;
  while (i < blocks.length && blocks[i].type === 'p') {
    lead.push(blocks[i]);
    i++;
  }
  return { h1: title, lead, rest: blocks.slice(i) };
}

export interface FaqPair {
  q: string;
  a: string;
}

export const isFaqHeading = (t: string) => /\b(faq|frequently asked questions?)\b/i.test(t);
export const isLinksHeading = (t: string) =>
  /\b(related reading|related guides|related|other platforms|other ai generators|compare with other)\b/i.test(t);

const INTRO = /(cdn-cgi|\/l\/email-protection|have another question|^\s*contact us)/i;

export function plainText(s: string): string {
  return s.replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, '$1').replace(/\s+/g, ' ').trim();
}

const endsWithQuestion = (s: string) => plainText(s).replace(/["'”’)\]]+$/, '').trim().endsWith('?');

/**
 * FAQ sections on the source site come in two shapes: a question paragraph followed by an answer
 * paragraph, or a single paragraph mixing "Question? Answer…". A leading intro line (contact/email)
 * is dropped first. This returns consistent question/answer pairs for either shape.
 */
export function faqPairs(paragraphs: string[]): FaqPair[] {
  let start = 0;
  while (start < paragraphs.length && INTRO.test(paragraphs[start])) start++;
  const ps = paragraphs.slice(start);
  if (!ps.length) return [];

  const pairStyle = ps.filter(endsWithQuestion).length >= ps.length / 2;
  const out: FaqPair[] = [];
  if (pairStyle) {
    for (let i = 0; i + 1 < ps.length; i += 2) out.push({ q: ps[i], a: ps[i + 1] });
  } else {
    for (const p of ps) {
      const idx = p.indexOf('?');
      if (idx >= 0) out.push({ q: p.slice(0, idx + 1), a: p.slice(idx + 1).trim() });
      else if (out.length) out[out.length - 1].a = `${out[out.length - 1].a} ${p}`.trim();
    }
  }
  return out;
}

/** Collects the paragraph run that follows an "FAQ" heading. */
export function faqParagraphs(blocks: Block[], headingIndex: number): string[] {
  const ps: string[] = [];
  let j = headingIndex + 1;
  while (j < blocks.length && blocks[j].type !== 'h2' && blocks[j].type !== 'h3' && blocks[j].type !== 'h4') {
    const b = blocks[j];
    if (b.type !== 'p') break;
    ps.push(b.text);
    j++;
  }
  return ps;
}

/** Pulls all FAQ pairs from a page, for structured data. */
export function extractFaq(blocks: Block[]): FaqPair[] {
  const pairs: FaqPair[] = [];
  for (let i = 0; i < blocks.length; i++) {
    const b = blocks[i];
    if (b.type === 'h2' && isFaqHeading(b.text)) {
      pairs.push(...faqPairs(faqParagraphs(blocks, i)));
    }
  }
  return pairs.map((p) => ({ q: plainText(p.q), a: plainText(p.a) }));
}
