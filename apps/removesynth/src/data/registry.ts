import pagesJson from './pages.json';

export type Block =
  | { type: 'h1' | 'h2' | 'h3' | 'h4'; text: string }
  | { type: 'p'; text: string }
  | { type: 'ul'; items: string[] };

export interface Doc {
  path: string;
  title: string;
  description: string;
  blocks: Block[];
}

export const PAGES = pagesJson as Record<string, Doc>;

export type Kind =
  | 'cleaner'
  | 'checker'
  | 'platform'
  | 'generator'
  | 'hub'
  | 'glossary'
  | 'legal'
  | 'converter';

export const CLEANER_SLUGS = [
  'ai-metadata-remover',
  'metadata-remover',
  'c2pa-remover',
  'exif-cleaner',
  'xmp-remover',
  'png-ai-metadata-remover',
  'ai-only-metadata-remover',
  'heic-metadata-remover',
  'remove-gps-from-photo',
  'pdf-metadata-remover',
  'video-metadata-remover',
  'remove-ai-detection-from-image',
];

export const CHECKER_SLUGS = [
  'ai-metadata-checker',
  'ai-image-checker',
  'c2pa-checker',
  'ai-watermark-checker',
  'image-privacy-analyzer',
  'calculate-metadata',
  'tell-me-my-metadata',
];

export interface LinkItem {
  slug: string;
  name: string;
}
export interface LinkGroup {
  heading: string;
  items: LinkItem[];
}

export const PLATFORM_GROUPS: LinkGroup[] = [
  {
    heading: 'Social networks',
    items: [
      { slug: 'instagram', name: 'Instagram' },
      { slug: 'tiktok', name: 'TikTok' },
      { slug: 'facebook', name: 'Facebook' },
      { slug: 'threads', name: 'Threads' },
      { slug: 'twitter', name: 'X (Twitter)' },
      { slug: 'youtube', name: 'YouTube' },
      { slug: 'snapchat', name: 'Snapchat' },
      { slug: 'pinterest', name: 'Pinterest' },
    ],
  },
  { heading: 'Shops', items: [{ slug: 'etsy', name: 'Etsy' }] },
  {
    heading: 'Communities',
    items: [
      { slug: 'reddit', name: 'Reddit' },
      { slug: 'discord', name: 'Discord' },
      { slug: 'bluesky', name: 'Bluesky' },
      { slug: 'behance', name: 'Behance' },
      { slug: 'linkedin', name: 'LinkedIn' },
      { slug: 'xiaohongshu', name: 'Xiaohongshu' },
    ],
  },
];

export const GENERATOR_GROUPS: LinkGroup[] = [
  {
    heading: 'Image generators',
    items: [
      { slug: 'gemini', name: 'Google Gemini' },
      { slug: 'chatgpt-image', name: 'ChatGPT Image' },
      { slug: 'dalle', name: 'DALL·E' },
      { slug: 'midjourney', name: 'Midjourney' },
      { slug: 'flux', name: 'Flux' },
      { slug: 'leonardo', name: 'Leonardo' },
      { slug: 'krea', name: 'Krea' },
      { slug: 'recraft', name: 'Recraft' },
      { slug: 'novelai', name: 'NovelAI' },
      { slug: 'ideogram', name: 'Ideogram' },
      { slug: 'grok', name: 'Grok' },
      { slug: 'firefly', name: 'Adobe Firefly' },
      { slug: 'bing-image-creator', name: 'Bing Image Creator' },
      { slug: 'nightcafe', name: 'NightCafe' },
      { slug: 'playground-ai', name: 'Playground AI' },
      { slug: 'starryai', name: 'StarryAI' },
      { slug: 'artbreeder', name: 'Artbreeder' },
      { slug: 'craiyon', name: 'Craiyon' },
      { slug: 'prodia', name: 'Prodia' },
      { slug: 'replicate', name: 'Replicate' },
      { slug: 'fooocus', name: 'Fooocus' },
      { slug: 'stable-diffusion', name: 'Stable Diffusion' },
    ],
  },
  {
    heading: 'Video stills',
    items: [
      { slug: 'kling', name: 'Kling' },
      { slug: 'veo', name: 'Veo' },
      { slug: 'sora', name: 'Sora' },
      { slug: 'runway', name: 'Runway' },
      { slug: 'pika', name: 'Pika' },
    ],
  },
  {
    heading: 'Editors & photo apps',
    items: [
      { slug: 'canva', name: 'Canva' },
      { slug: 'adobe-express', name: 'Adobe Express' },
      { slug: 'photoshop', name: 'Photoshop' },
      { slug: 'lightroom', name: 'Lightroom' },
      { slug: 'capcut', name: 'CapCut' },
      { slug: 'clipdrop', name: 'Clipdrop' },
    ],
  },
  {
    heading: 'Mobile apps',
    items: [
      { slug: 'meta-ai', name: 'Meta AI' },
      { slug: 'meitu', name: 'Meitu' },
      { slug: 'jimeng', name: 'Jimeng' },
    ],
  },
];

export const PLATFORM_SLUGS = PLATFORM_GROUPS.flatMap((g) => g.items.map((i) => i.slug));
export const GENERATOR_SLUGS = GENERATOR_GROUPS.flatMap((g) => g.items.map((i) => i.slug));

export const HUB_SLUGS = ['platforms', 'exports'];
export const GLOSSARY_SLUGS = ['glossary'];
export const LEGAL_SLUGS = ['about', 'contact', 'disclaimer', 'privacy', 'terms'];
export const CONVERTER_SLUGS = ['heic-to-jpg'];

const kindMap = new Map<string, Kind>();
CLEANER_SLUGS.forEach((s) => kindMap.set(s, 'cleaner'));
CHECKER_SLUGS.forEach((s) => kindMap.set(s, 'checker'));
PLATFORM_SLUGS.forEach((s) => kindMap.set(s, 'platform'));
GENERATOR_SLUGS.forEach((s) => kindMap.set(s, 'generator'));
HUB_SLUGS.forEach((s) => kindMap.set(s, 'hub'));
GLOSSARY_SLUGS.forEach((s) => kindMap.set(s, 'glossary'));
LEGAL_SLUGS.forEach((s) => kindMap.set(s, 'legal'));

export function kindOf(slug: string): Kind | undefined {
  return kindMap.get(slug);
}

/** Every path this site owns, as a bare slug (home is ''). */
export const ALL_SLUGS: string[] = [
  ...CLEANER_SLUGS,
  ...CHECKER_SLUGS,
  ...PLATFORM_SLUGS,
  ...GENERATOR_SLUGS,
  ...HUB_SLUGS,
  ...GLOSSARY_SLUGS,
  ...LEGAL_SLUGS,
  ...CONVERTER_SLUGS,
];

export const SLUG_SET = new Set(ALL_SLUGS);
