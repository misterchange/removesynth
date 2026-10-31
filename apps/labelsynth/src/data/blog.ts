import blogJson from './blog.json';
import type { Block } from './registry';

export interface Post {
  slug: string;
  title: string;
  description: string;
  published: string;
  blocks: Block[];
}

export const POSTS = blogJson as Post[];
export const POST_SET = new Set(POSTS.map((p) => p.slug));

export function postBySlug(slug: string): Post | undefined {
  return POSTS.find((p) => p.slug === slug);
}

export function postDate(p: Post): string {
  if (!p.published) return '';
  const d = new Date(p.published);
  if (Number.isNaN(d.getTime())) return '';
  return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}
