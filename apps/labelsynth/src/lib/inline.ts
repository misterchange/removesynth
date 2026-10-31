import { SLUG_SET } from '../data/registry';
import { POST_SET } from '../data/blog';

const esc = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

/** Rewrites a link from the source site into a local route when we host it. */
export function resolveHref(href: string): string {
  const raw = href.trim();
  if (!raw) return raw;
  if (/^(https?:|mailto:|tel:)/i.test(raw)) return raw;
  if (raw === '/' || raw === '/#tool-upload') return '/#tool-upload';
  if (raw.startsWith('#')) return raw;

  let path = raw.split('#')[0].split('?')[0];
  const hash = raw.includes('#') ? '#' + raw.split('#').slice(1).join('#') : '';
  // Drop a locale prefix like /zh/ or /pt-BR/
  path = path.replace(/^\/[a-z]{2}(-[A-Za-z]{2})?\//, '/');
  path = path.replace(/\/+$/, '');
  const slug = path.replace(/^\//, '');

  if (slug === 'blog') return '/blog/';
  if (slug.startsWith('blog/')) {
    const post = slug.slice('blog/'.length);
    return (POST_SET.has(post) ? `/blog/${post}/` : '/blog/') + hash;
  }
  if (slug === '') return '/' + hash;
  if (slug === 'comfyui') return '/stable-diffusion/' + hash;
  if (SLUG_SET.has(slug)) return `/${slug}/` + hash;
  // Unknown target path: send to the closest hub rather than a dead link.
  if (/^(instagram|tiktok|facebook|threads|twitter|youtube|snapchat|pinterest|etsy|reddit|discord|bluesky|behance|linkedin|xiaohongshu)/.test(slug)) return '/platforms/';
  return '/#tool-upload';
}

/** Renders a content string with [[label|href]] markers into safe HTML. */
export function renderInline(text: string): string {
  let html = '';
  const re = /\[\[([^\]|]+)\|([^\]]+)\]\]/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text))) {
    html += esc(text.slice(last, m.index));
    const label = m[1].replace(/^\[+|\]+$/g, '').trim();
    html += `<a href="${esc(resolveHref(m[2]))}">${esc(label)}</a>`;
    last = m.index + m[0].length;
  }
  html += esc(text.slice(last));
  return html;
}

/** Plain text (no links) for meta descriptions and similar. */
export function plainText(text: string): string {
  return text.replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, '$1').replace(/\s+/g, ' ').trim();
}
