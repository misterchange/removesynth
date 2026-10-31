// Content for the "compress image to N KB" pages and the "X to Y" converter pages.
import type { FaqItem } from '@removesynth/shared/lib/faq';

export interface SizePage {
  kb: number;
  slug: string; // compress-image-to-<slug>
  label: string; // "50 KB"
  uses: string[];
  dims: string; // rough guide to dimensions that fit
  tips: string[];
  faqs: FaqItem[];
}

const sharedSizeFaqs = (label: string): FaqItem[] => [
  {
    q: `Will the image be exactly ${label}?`,
    a: `It will be at most ${label}, usually just under it. The tool picks the highest quality that stays below your limit, so you don’t lose more detail than you have to.`,
  },
  {
    q: 'Is 1 KB 1000 or 1024 bytes?',
    a: 'Websites use both. We count 1 KB as 1000 bytes, which is the stricter reading, so your file passes either way.',
  },
  {
    q: 'Are my photos uploaded?',
    a: 'No. Compression happens inside your browser and your photos never leave your device.',
  },
  {
    q: 'Can I compress several photos at once?',
    a: 'Yes. Drop up to 30 images and download them one by one or all together as a ZIP.',
  },
];

export const SIZES: SizePage[] = [
  {
    kb: 20,
    slug: '20kb',
    label: '20 KB',
    uses: [
      'Signature uploads on online application forms',
      'Small ID or thumbnail photos where a form sets a strict limit',
      'Very small avatars and icons',
    ],
    dims: 'A clear signature or a small face photo usually fits in 20 KB at around 300–400 pixels wide. Larger photos are scaled down automatically.',
    tips: [
      'Crop to just the face or signature first. Fewer pixels means more quality at 20 KB.',
      'Scan signatures in black ink on white paper; they compress far better than photos.',
      'If the form also sets pixel dimensions, resize to those first, then compress.',
    ],
    faqs: [
      {
        q: 'Why does my 20 KB photo look blurry?',
        a: 'A modern phone photo is often 3–5 MB, so reaching 20 KB means shrinking it a lot. Cropping tightly before compressing keeps the important part sharper.',
      },
      ...sharedSizeFaqs('20 KB'),
    ],
  },
  {
    kb: 50,
    slug: '50kb',
    label: '50 KB',
    uses: [
      'Passport-size photos on online application and exam forms',
      'Profile photos on job portals and government websites',
      'Attachments on sites with small upload limits',
    ],
    dims: 'A passport-style photo looks good in 50 KB at around 400–600 pixels wide. Bigger photos are reduced to fit.',
    tips: [
      'Check whether the form also asks for specific dimensions or a white background.',
      'Use JPG. Almost every form accepts it, and it compresses photos best.',
      'Keep a copy of the original in case you need a different size later.',
    ],
    faqs: [
      {
        q: 'How do I reduce a photo to 50 KB on my phone?',
        a: 'Open this page in your phone’s browser, tap the box to pick the photo, and download the result. No app is needed.',
      },
      ...sharedSizeFaqs('50 KB'),
    ],
  },
  {
    kb: 100,
    slug: '100kb',
    label: '100 KB',
    uses: [
      'Application forms that allow photos up to 100 KB',
      'Profile pictures for social and professional sites',
      'Product photos for listings with upload limits',
    ],
    dims: 'At 100 KB a photo can usually stay around 800–1000 pixels wide with good detail.',
    tips: [
      'If the result looks soft, try WebP output where the site accepts it; it keeps more detail at the same size.',
      'Avoid screenshots of photos. Compress the original file instead.',
    ],
    faqs: [
      {
        q: 'How do I compress a JPG to 100 KB without losing quality?',
        a: 'Some quality loss is unavoidable, but the tool keeps it to the minimum by choosing the highest quality that fits. Starting from the original photo, not a screenshot, helps a lot.',
      },
      ...sharedSizeFaqs('100 KB'),
    ],
  },
  {
    kb: 200,
    slug: '200kb',
    label: '200 KB',
    uses: [
      'Document photos and scans on application portals',
      'Images for email and messaging',
      'Blog and website images that should load fast',
    ],
    dims: 'At 200 KB most photos keep around 1200–1600 pixels wide, enough for sharp viewing on screens.',
    tips: [
      'For scanned documents, make sure the text is still readable after compressing.',
      'For websites, WebP at 200 KB usually looks better than JPG at the same size.',
    ],
    faqs: [...sharedSizeFaqs('200 KB')],
  },
  {
    kb: 500,
    slug: '500kb',
    label: '500 KB',
    uses: [
      'High-quality website and portfolio images',
      'Uploads on portals with a 500 KB limit',
      'Sharing photos without sending huge originals',
    ],
    dims: 'At 500 KB most photos keep close to full HD (around 1920 pixels wide) with very little visible loss.',
    tips: ['Most photos reach 500 KB by lowering quality alone, so the dimensions often stay the same.'],
    faqs: [...sharedSizeFaqs('500 KB')],
  },
  {
    kb: 1000,
    slug: '1mb',
    label: '1 MB',
    uses: [
      'Upload limits on forms, marketplaces and support sites',
      'Email attachments',
      'Sharing full-size photos in less space',
    ],
    dims: 'A 1 MB JPG can keep most phone photos at full resolution, just with smarter compression.',
    tips: ['If your photo is already under 1 MB, it is saved again at the best quality that still fits.'],
    faqs: [...sharedSizeFaqs('1 MB')],
  },
];

export interface Format {
  key: string;
  name: string;
  about: string;
  transparency: boolean;
  animation: boolean;
  compression: string;
  support: string;
}

export const FORMATS: Record<string, Format> = {
  jpg: {
    key: 'jpg',
    name: 'JPG',
    about: 'JPG (or JPEG) is the most widely supported photo format. It uses lossy compression, so files are small, but it has no transparency.',
    transparency: false,
    animation: false,
    compression: 'Lossy',
    support: 'Everywhere',
  },
  png: {
    key: 'png',
    name: 'PNG',
    about: 'PNG is a lossless format that supports transparency. It’s ideal for logos, screenshots and graphics, but photos saved as PNG are large.',
    transparency: true,
    animation: false,
    compression: 'Lossless',
    support: 'Everywhere',
  },
  webp: {
    key: 'webp',
    name: 'WebP',
    about: 'WebP is Google’s web image format. It makes smaller files than JPG and PNG and supports transparency, but some older apps and editors can’t open it.',
    transparency: true,
    animation: true,
    compression: 'Lossy or lossless',
    support: 'All modern browsers; some apps and older software don’t',
  },
  avif: {
    key: 'avif',
    name: 'AVIF',
    about: 'AVIF is a newer format that compresses even better than WebP. Many websites now serve it, but lots of apps, editors and upload forms still don’t accept it.',
    transparency: true,
    animation: true,
    compression: 'Lossy or lossless',
    support: 'Modern browsers; limited in apps and editors',
  },
  heic: {
    key: 'heic',
    name: 'HEIC',
    about: 'HEIC is the default photo format on iPhones. It’s efficient, but Windows, many websites and many apps can’t open it.',
    transparency: false,
    animation: false,
    compression: 'Lossy',
    support: 'Apple devices; limited elsewhere',
  },
};

export interface Pair {
  from: string;
  to: 'jpg' | 'png' | 'webp';
  why: string[];
  note: string;
  faqs: FaqItem[];
}

const pairFaqs = (from: string, to: string): FaqItem[] => [
  {
    q: `Is this ${from} to ${to} converter free?`,
    a: 'Yes. There’s no sign-up, no watermark and no limit on how many times you use it. You can convert up to 30 images at once.',
  },
  {
    q: 'Are my images uploaded?',
    a: 'No. The conversion runs in your browser, so your images never leave your device.',
  },
  {
    q: `Can I convert ${from} to ${to} on my phone?`,
    a: 'Yes. Open this page in your phone’s browser, pick the images and download the converted files.',
  },
];

export const PAIRS: Pair[] = [
  {
    from: 'webp',
    to: 'jpg',
    why: [
      'Images saved from websites often download as WebP, and many apps, editors and upload forms won’t accept them.',
      'JPG opens everywhere: Windows Photos, older Photoshop versions, Word, email and printing services.',
    ],
    note: 'Transparent areas become white, because JPG doesn’t support transparency. Choose PNG if you need to keep it.',
    faqs: [
      { q: 'Why do images download as WebP?', a: 'Many websites serve WebP because the files are smaller. Your browser saves the file in the format the site sent.' },
      ...pairFaqs('WebP', 'JPG'),
    ],
  },
  {
    from: 'webp',
    to: 'png',
    why: [
      'Keep transparency when an app or editor doesn’t open WebP.',
      'Get a lossless copy for editing, so quality doesn’t drop each time you save.',
    ],
    note: 'PNG is lossless, so the file is usually bigger than the WebP original.',
    faqs: [...pairFaqs('WebP', 'PNG')],
  },
  {
    from: 'avif',
    to: 'jpg',
    why: [
      'AVIF images saved from websites often won’t open in editors, Windows apps or upload forms.',
      'JPG is accepted almost everywhere.',
    ],
    note: 'Transparent areas become white in JPG.',
    faqs: [
      { q: 'How do I open an AVIF file?', a: 'Modern browsers can show AVIF, but many apps can’t. Converting to JPG or PNG is the simplest fix.' },
      ...pairFaqs('AVIF', 'JPG'),
    ],
  },
  {
    from: 'avif',
    to: 'png',
    why: ['Keep transparency from AVIF images in a format every editor opens.', 'Get a lossless copy for editing.'],
    note: 'Expect a bigger file than the AVIF original.',
    faqs: [...pairFaqs('AVIF', 'PNG')],
  },
  {
    from: 'png',
    to: 'jpg',
    why: [
      'Shrink large PNG photos and screenshots so they’re easier to share and upload.',
      'Meet forms that only accept JPG.',
    ],
    note: 'Transparent backgrounds become white. For logos with transparency, keep PNG or use WebP.',
    faqs: [
      { q: 'Does converting PNG to JPG reduce quality?', a: 'JPG is lossy, so there is a small loss. At the default 92% quality it’s hard to see in photos. Use 100% for the best result.' },
      ...pairFaqs('PNG', 'JPG'),
    ],
  },
  {
    from: 'jpg',
    to: 'png',
    why: [
      'Edit an image repeatedly without it losing more quality each time you save.',
      'Some design tools and print services ask for PNG.',
    ],
    note: 'Converting to PNG doesn’t add transparency or remove the background; it only changes the file format. The file usually gets bigger.',
    faqs: [
      { q: 'Will JPG to PNG make the background transparent?', a: 'No. The image stays the same, just saved as PNG. Removing a background is a different tool.' },
      ...pairFaqs('JPG', 'PNG'),
    ],
  },
  {
    from: 'png',
    to: 'webp',
    why: ['Make website images much smaller while keeping transparency.', 'Faster pages help both visitors and search rankings.'],
    note: 'Choose 100% quality for logos and graphics with sharp edges.',
    faqs: [...pairFaqs('PNG', 'WebP')],
  },
  {
    from: 'jpg',
    to: 'webp',
    why: ['Cut photo file sizes for websites, often by a quarter to a third, without visible loss.', 'WebP works in every modern browser.'],
    note: 'Keep the original JPG for apps that don’t open WebP.',
    faqs: [...pairFaqs('JPG', 'WebP')],
  },
  {
    from: 'heic',
    to: 'png',
    why: ['Open iPhone photos on Windows and in apps that don’t support HEIC.', 'Get a lossless copy for editing.'],
    note: 'PNG files from photos are large. Choose JPG if you just want to share or upload.',
    faqs: [...pairFaqs('HEIC', 'PNG')],
  },
];

export const pairSlug = (p: Pair) => `${p.from}-to-${p.to}`;
