content = """// Content for /platforms/[slug]/ and /generators/[slug]/. Keep claims to what the companies have
// publicly said; platform rules change, so wording stays general where details shift often.
import type { FaqItem } from '../lib/faq';

export interface Platform {
  slug: string;
  name: string;
  owner: string;
  label: string; // what the AI label is called on the platform
  title: string;
  description: string;
  intro: string;
  signals: string[]; // what the platform reads to apply labels
  rules: string; // creator disclosure rules, in plain words
  wrongLabel: string[]; // what to do when a label looks wrong
  faqs: FaqItem[];
}

export interface Generator {
  slug: string;
  name: string;
  maker: string;
  title: string;
  description: string;
  intro: string;
  markers: { kind: string; detail: string }[];
  notes: string;
  faqs: FaqItem[];
}

const checkFirst = 'Run the file through the AI metadata checker to see exactly which labels and private details it carries.';

export const PLATFORMS: Platform[] = [
  {
    slug: 'instagram',
    name: 'Instagram',
    owner: 'Meta',
    label: 'AI info',
    title: 'Instagram AI info Label: What Triggers It and How to Check',
    description:
      'Why Instagram shows AI info labels on photos, which C2PA & IPTC metadata it inspects, creator disclosure rules, and how to inspect files before posting.',
    intro:
      'Instagram shows an "AI info" label on posts that were made or edited with AI. Meta applies it in two ways: from industry-standard metadata inside the file, and when creators label a post themselves.',
    signals: [
      'Content Credentials (C2PA) manifests that say an image was created or edited with AI.',
      'The IPTC digital source type tag, which AI tools such as those from Google, OpenAI, Microsoft and Adobe can write.',
      'Visible and invisible markers on images made with Meta AI.',
      'The "AI label" setting creators turn on when they post.',
    ],
    rules:
      'Meta asks people to disclose photorealistic video and realistic-sounding audio that was digitally created or altered, and may add a label itself if it finds AI signals. For content that was only edited with AI, the label usually sits in the post menu instead of on the post.',
    wrongLabel: [
      'Check the original file with the AI metadata checker. Editing a real photo with an AI feature, such as generative fill, often adds "edited with AI" metadata.',
      'If you used an AI feature, the label is accurate: it tells viewers an AI tool was involved, not that the whole photo is fake.',
      'If no AI tool was used and the label still appears, report it through Instagram help center.',
    ],
    faqs: [
      {
        q: 'Why does my real photo say "AI info" on Instagram?',
        a: 'Usually because an AI editing feature added metadata to the file, for example an AI eraser or generative fill. The label means AI was used somewhere in editing.',
      },
      {
        q: 'Does Instagram detect SynthID?',
        a: 'Meta has not said it reads SynthID. Its labels are based on C2PA and IPTC metadata, its own markers for Meta AI images, and self-disclosure.',
      },
      {
        q: 'Do I have to label AI content on Instagram?',
        a: 'Meta requires disclosure for photorealistic video and realistic audio that was digitally created or altered. Labelling other AI images is encouraged.',
      },
    ],
  },
  {
    slug: 'facebook',
    name: 'Facebook',
    owner: 'Meta',
    label: 'AI info',
    title: 'Facebook "AI info" Label: How Facebook Detects AI Images',
    description:
      'How Facebook decides when to show the AI info label, the C2PA and IPTC metadata tags it reads, and what creators can do if an image is labelled by mistake.',
    intro:
      'Facebook uses the same "AI info" system as Instagram and Threads. Labels come from metadata inside the file, from Meta own markers on Meta AI images, and from creators who disclose AI use.',
    signals: [
      'Content Credentials (C2PA) that declare AI creation or AI editing.',
      'The IPTC digital source type tag written by many AI tools.',
      'Visible and invisible markers on Meta AI images.',
      'Creator self-disclosure when posting.',
    ],
    rules:
      'Meta requires people to disclose realistic video and audio that was digitally created or altered. Content that could seriously mislead the public on important matters may get a more prominent label.',
    wrongLabel: [
      'Check the original file with the AI metadata checker to see what triggered the label.',
      'AI editing features in apps like Photoshop or phone galleries can add "edited with AI" metadata to otherwise real photos.',
      'If you believe the label is wrong, use Facebook help center to report it.',
    ],
    faqs: [
      {
        q: 'Is the Facebook AI label the same as Instagram?',
        a: 'Yes. Both are run by Meta and use the same "AI info" label and detection signals.',
      },
      {
        q: 'Does a screenshot avoid the label?',
        a: 'A screenshot drops metadata, but Meta may still use other signals, and AI content you post should still be disclosed when the rules require it.',
      },
    ],
  },
  {
    slug: 'tiktok',
    name: 'TikTok',
    owner: 'ByteDance',
    label: 'AI-generated',
    title: 'TikTok AI Label: How TikTok Detects and Flags AI Media',
    description:
      'How TikTok labels AI-generated content, why it reads Content Credentials (C2PA) on uploads, and what creators must disclose. Free tool with zero uploads.',
    intro:
      'TikTok shows an "AI-generated" label on videos and photos made with AI. Creators can add it themselves, and TikTok adds it automatically when an upload carries Content Credentials that say it was made with AI.',
    signals: [
      'Content Credentials (C2PA) attached by AI tools and other platforms.',
      'TikTok own AI effects, which are labelled automatically.',
      'The "AI-generated content" setting creators turn on before posting.',
    ],
    rules:
      'TikTok requires creators to label AI-generated content that shows realistic scenes or people. Unlabelled realistic AI content can be removed or restricted.',
    wrongLabel: [
      'Check the original file with the AI metadata checker to see whether it carries Content Credentials.',
      'Clips edited in apps with AI features can pick up AI metadata even if most of the footage is real.',
      'If the label is wrong, you can appeal it in the app.',
    ],
    faqs: [
      {
        q: 'How does TikTok know my video was made with AI?',
        a: 'Mainly from Content Credentials (C2PA) in the file, from TikTok own AI effects, and from the AI-generated content setting.',
      },
      {
        q: 'Do I have to label AI videos on TikTok?',
        a: 'Yes, if they show realistic scenes or people. TikTok community guidelines require it.',
      },
    ],
  },
  {
    slug: 'youtube',
    name: 'YouTube',
    owner: 'Google',
    label: 'Altered or synthetic content',
    title: 'YouTube "Altered or Synthetic Content" Label Explained',
    description:
      'When YouTube requires you to disclose AI, how the Altered or synthetic content label appears, and how C2PA and SynthID fit in. Free tool with zero uploads.',
    intro:
      'YouTube asks creators to disclose realistic content that was made or meaningfully changed with AI. Viewers then see an "Altered or synthetic content" label in the description, or on the video itself for sensitive topics.',
    signals: [
      'The disclosure question creators answer in YouTube Studio when uploading.',
      'Content made with YouTube own AI tools, such as Veo in Shorts, which is labelled and carries SynthID.',
      'Content Credentials (C2PA), which YouTube can also use to show a "Captured with a camera" label for authentic footage.',
    ],
    rules:
      'Disclosure is required for realistic content: making a real person appear to say or do something, altering footage of real events or places, or generating realistic scenes. It is not required for clearly unrealistic content, beauty filters or minor edits.',
    wrongLabel: [
      'If you disclosed by mistake, you can change the setting in YouTube Studio.',
      'YouTube may add a label itself if content could mislead viewers, even when the creator did not disclose.',
    ],
    faqs: [
      {
        q: 'Does YouTube detect AI automatically?',
        a: 'It relies mainly on creator disclosure, labels its own AI tools automatically, and may add labels when content could mislead viewers.',
      },
      {
        q: 'Do AI thumbnails need disclosure?',
        a: 'YouTube disclosure setting is about the video content. Check YouTube help center for the latest rules on thumbnails and other assets.',
      },
    ],
  },
  {
    slug: 'pinterest',
    name: 'Pinterest',
    owner: 'Pinterest',
    label: 'AI modified',
    title: 'Pinterest "AI Modified" Label: How Pinterest Detects AI Pins',
    description:
      'How Pinterest labels AI-generated and AI-edited Pins, the IPTC metadata and classifiers it uses, and how to appeal a label. Free tool with zero uploads.',
    intro:
      'Pinterest labels image Pins that were made or edited with AI. The label appears when you open a Pin, and comes from metadata in the image as well as Pinterest own detection.',
    signals: [
      'The IPTC digital source type and other AI metadata in the image file.',
      'Pinterest own classifiers, which can label images even without metadata.',
    ],
    rules:
      'Pinterest labels AI content to help people tell what is real. Users can also choose to see fewer AI Pins in some categories.',
    wrongLabel: [
      'Check the original image with the AI metadata checker to see which AI metadata it carries.',
      'If you think a Pin was labelled by mistake, Pinterest lets you appeal the label.',
    ],
    faqs: [
      {
        q: 'Why was my Pin labelled AI modified?',
        a: 'Either the image file contains AI metadata, often from an AI editing tool, or Pinterest classifier flagged it.',
      },
    ],
  },
  {
    slug: 'linkedin',
    name: 'LinkedIn',
    owner: 'Microsoft',
    label: 'Content Credentials (CR)',
    title: 'LinkedIn Content Credentials: What the "CR" Icon Means',
    description:
      'Why some LinkedIn images show a CR Content Credentials icon, what it reveals about AI use, and how to check your file before posting. Free in-browser tool.',
    intro:
      'LinkedIn shows a small "CR" icon on images and videos that carry Content Credentials (C2PA). Clicking it reveals details such as whether the content was made with AI and which tool made it.',
    signals: ['Content Credentials (C2PA) embedded in the uploaded image or video.'],
    rules:
      'LinkedIn uses Content Credentials to give viewers context rather than to block content. Its professional community policies still apply to misleading AI content.',
    wrongLabel: [
      'Check the file with the AI metadata checker to see what its Content Credentials say.',
      'Credentials describe how the file was made. If you used an AI feature, it is accurate.',
    ],
    faqs: [
      {
        q: 'What is the CR icon on LinkedIn?',
        a: 'It stands for Content Credentials. It appears when an image or video carries a C2PA manifest describing how it was made.',
      },
    ],
  },
  {
    slug: 'x',
    name: 'X (Twitter)',
    owner: 'X Corp.',
    label: 'Manipulated media',
    title: 'Does X Label AI Images? Synthetic Media Rules Explained',
    description:
      'How X handles AI-generated and manipulated media, when posts get labelled, and what metadata does and does not do there. Free tool with zero server uploads.',
    intro:
      'X has a synthetic and manipulated media policy. Rather than labelling every AI image automatically from metadata, it focuses on media that could mislead people or cause harm.',
    signals: [
      'Reviews under its synthetic and manipulated media policy.',
      'Community Notes, where contributors can add context that an image is AI-generated.',
    ],
    rules:
      'Misleading synthetic media that could cause harm can be labelled, have its reach reduced or be removed.',
    wrongLabel: [
      'If a Community Note or label seems wrong, you can rate notes or appeal through X help center.',
    ],
    faqs: [
      {
        q: 'Does X read C2PA metadata?',
        a: 'X has not announced automatic labels based on Content Credentials. Its approach centers on its manipulated media policy and Community Notes.',
      },
    ],
  },
];

export const GENERATORS: Generator[] = [
  {
    slug: 'chatgpt-image',
    name: 'ChatGPT images',
    maker: 'OpenAI',
    title: 'ChatGPT Image Metadata: Does ChatGPT Add C2PA Credentials?',
    description:
      'What metadata ChatGPT and DALL-E images carry, including C2PA Content Credentials, and how to check a ChatGPT image yourself. Free tool with zero uploads.',
    intro:
      'OpenAI adds Content Credentials (C2PA) to images created with ChatGPT and its image models, including DALL-E. The credentials say the image was made by an OpenAI tool.',
    markers: [
      { kind: 'Content Credentials (C2PA)', detail: 'A signed manifest naming OpenAI as the tool that made the image.' },
      { kind: 'Invisible watermark', detail: 'OpenAI has not said it uses SynthID. SynthID is Google technology.' },
    ],
    notes:
      'Content Credentials are stored in metadata, so they can be lost when an image is screenshotted or re-saved by some apps. Platforms such as TikTok, LinkedIn and Instagram read them on upload.',
    faqs: [
      {
        q: 'Do ChatGPT images have SynthID?',
        a: 'No. SynthID is Google watermark. ChatGPT images carry OpenAI Content Credentials instead.',
      },
      { q: 'How can I check a ChatGPT image?', a: checkFirst },
    ],
  },
  {
    slug: 'adobe-firefly',
    name: 'Adobe Firefly',
    maker: 'Adobe',
    title: 'Adobe Firefly Metadata: C2PA Content Credentials Explained',
    description:
      'Adobe Firefly attaches Content Credentials (C2PA) to everything it generates. Here is what they say and how Photoshop generative fill is safely cleaned.',
    intro:
      'Adobe co-founded the Content Authenticity Initiative, and Firefly attaches Content Credentials to the images it generates. Photoshop generative features can record AI edits the same way.',
    markers: [
      { kind: 'Content Credentials (C2PA)', detail: 'Names Adobe Firefly and declares the content as created or edited with generative AI.' },
      { kind: 'IPTC digital source type', detail: 'Marks the image as "trained algorithmic media" (created with generative AI) or a composite with AI.' },
    ],
    notes:
      'Because Adobe tools also record generative fill and similar edits, real photos edited with these features can carry "edited with AI" credentials.',
    faqs: [
      { q: 'Does Photoshop generative fill add AI metadata?', a: 'It can. Adobe records generative AI edits in Content Credentials, which some platforms read on upload.' },
      { q: 'How can I check a Firefly image?', a: checkFirst },
    ],
  },
  {
    slug: 'gemini',
    name: 'Gemini & Imagen',
    maker: 'Google',
    title: 'Gemini and Imagen Images: SynthID, Watermarks and Metadata',
    description:
      'What marks Google Gemini and Imagen add to AI images, including the invisible SynthID watermark, and how to check a Gemini image. Free in-browser tool.',
    intro:
      'Images created or edited with Google Gemini app and Imagen carry SynthID, Google DeepMind invisible watermark. Depending on the product, Google can also add metadata and a visible mark.',
    markers: [
      { kind: 'SynthID', detail: 'An invisible watermark in the pixels. Not visible in metadata; checked with Google SynthID Detector or Gemini.' },
      { kind: 'Visible mark', detail: 'Some Gemini app images include a small visible Gemini mark.' },
      { kind: 'Metadata', detail: 'Some Google products also add IPTC or C2PA metadata. Run your file through the checker to see what yours has.' },
    ],
    notes: 'SynthID is designed to survive cropping, compression and screenshots, unlike metadata.',
    faqs: [
      { q: 'Can a metadata checker find SynthID?', a: 'No. SynthID is in the pixels. Use Google SynthID Detector, or see our SynthID detector guide.' },
      { q: 'How can I check a Gemini image metadata?', a: checkFirst },
    ],
  },
  {
    slug: 'meta-ai',
    name: 'Meta AI',
    maker: 'Meta',
    title: 'Meta AI Images: Imagined With AI Labels and Metadata Guide',
    description:
      'What marks Meta AI adds to the images it generates: a visible label, invisible watermarks and IPTC metadata, and how to check a file. Free in-browser tool.',
    intro:
      'Images made with Meta AI carry several markers so they can be recognised across Meta apps and beyond: a visible label, invisible watermarks and IPTC metadata.',
    markers: [
      { kind: 'Visible label', detail: 'An "Imagined with AI" style mark on the image.' },
      { kind: 'Invisible watermark', detail: 'A watermark embedded in the image that Meta can detect.' },
      { kind: 'IPTC metadata', detail: 'Industry-standard metadata declaring the image as AI-generated.' },
    ],
    notes: 'These markers are why Meta AI images get the "AI info" label on Instagram, Facebook and Threads.',
    faqs: [{ q: 'How can I check a Meta AI image?', a: checkFirst }],
  },
  {
    slug: 'midjourney',
    name: 'Midjourney',
    maker: 'Midjourney',
    title: 'Midjourney Image Metadata: What Midjourney Files Contain',
    description:
      'What metadata Midjourney images can carry, such as the prompt and job details, and how to check a Midjourney file before you share it. Free in-browser tool.',
    intro:
      'Midjourney files can carry text metadata such as the prompt and job details, depending on how they were downloaded. Meta has named Midjourney among the companies whose AI metadata it reads.',
    markers: [
      { kind: 'Text metadata', detail: 'Prompt and job information can be saved in the file description fields.' },
      { kind: 'AI metadata', detail: 'Whether IPTC or C2PA markers are present depends on the version and export. The checker shows what your file has.' },
    ],
    notes: 'If you do not want your prompt to travel with the image, check the file before sharing it.',
    faqs: [{ q: 'How can I check a Midjourney image?', a: checkFirst }],
  },
  {
    slug: 'stable-diffusion',
    name: 'Stable Diffusion',
    maker: 'Stability AI and the open-source community',
    title: 'Stable Diffusion PNG Metadata: Prompts & Parameters Guide',
    description:
      'Stable Diffusion apps like Automatic1111, Forge and ComfyUI save prompts and parameters inside PNG files. Here is what is stored and how to check them.',
    intro:
      'Local Stable Diffusion apps save generation details right inside the PNG file. Anyone who opens the file in a metadata viewer can read your prompt, seed, model and settings.',
    markers: [
      { kind: 'PNG "parameters" text', detail: 'Automatic1111 and Forge store the prompt, negative prompt, seed, sampler and model.' },
      { kind: 'PNG "prompt" and "workflow"', detail: 'ComfyUI stores the full node graph, which can be loaded back into ComfyUI.' },
      { kind: 'Invisible watermark', detail: 'Some pipelines add an invisible watermark; many local setups do not.' },
    ],
    notes:
      'The parameters identify the image as AI-generated. Our photo metadata remover keeps them for that reason; if you do not want to share your prompt, export without metadata from your app.',
    faqs: [
      { q: 'Can people see my Stable Diffusion prompt?', a: 'Yes, if the PNG still contains its parameters. Check the file with the AI metadata checker.' },
    ],
  },
  {
    slug: 'flux',
    name: 'FLUX',
    maker: 'Black Forest Labs',
    title: 'FLUX Image Metadata: What FLUX Images Contain',
    description:
      'What metadata FLUX images carry depends on the app you use, from ComfyUI workflows to hosted services. Learn what to look for and how to inspect them.',
    intro:
      'FLUX models run in many places: ComfyUI and other local apps, and hosted services. The metadata in the file comes from the app, not the model.',
    markers: [
      { kind: 'ComfyUI workflow', detail: 'Local ComfyUI saves the prompt and workflow in PNG text chunks.' },
      { kind: 'Service metadata', detail: 'Hosted apps may add their own metadata or Content Credentials, or none at all.' },
    ],
    notes: 'Because it varies so much, checking the actual file is the only reliable way to know.',
    faqs: [{ q: 'How can I check a FLUX image?', a: checkFirst }],
  },
  {
    slug: 'bing-image-creator',
    name: 'Bing Image Creator & Microsoft Designer',
    maker: 'Microsoft',
    title: 'Bing Image Creator & Designer: C2PA Metadata Explained',
    description:
      'Microsoft adds Content Credentials (C2PA) to images from Bing Image Creator and Microsoft Designer. Discover what they contain and how to inspect them.',
    intro:
      'Microsoft attaches Content Credentials to images made with Bing Image Creator and Microsoft Designer, stating that the image was AI-generated and when.',
    markers: [
      { kind: 'Content Credentials (C2PA)', detail: 'A signed manifest identifying Microsoft AI tool and the creation date.' },
    ],
    notes: 'LinkedIn, also owned by Microsoft, shows these credentials with its "CR" icon.',
    faqs: [{ q: 'How can I check a Bing Image Creator image?', a: checkFirst }],
  },
  {
    slug: 'higgsfield',
    name: 'Higgsfield AI',
    maker: 'Higgsfield AI',
    title: 'Higgsfield AI Video Metadata & Watermarks Explained',
    description:
      'Higgsfield AI videos embed generation stamps, container atoms, and C2PA credentials. Learn how to check and clean them for social sharing. Free in-browser tool.',
    intro:
      'Higgsfield AI creates cinematic video motion. Its exported MP4 containers contain model identifiers and provenance metadata that social platforms inspect.',
    markers: [
      { kind: 'MP4 Container Metadata', detail: 'udta and moov box tags identifying Higgsfield rendering software.' },
      { kind: 'Content Credentials (C2PA)', detail: 'Provenance manifests flagging AI video synthesis.' },
    ],
    notes: 'Our lossless video container cleaner wipes these atoms without re-encoding your video.',
    faqs: [
      { q: 'Can I remove the Higgsfield watermark from my video?', a: 'Yes. Our in-browser MP4 cleaner scrubs container tags in seconds.' },
    ],
  },
  {
    slug: 'seedance',
    name: 'Seedance (ByteDance)',
    maker: 'ByteDance',
    title: 'Seedance 2.0, 2.1 & 2.2 Video Metadata & Watermarks Guide',
    description:
      'ByteDance Seedance AI videos embed model versions and C2PA credentials. How to sanitize Seedance 2.0, 2.1, and 2.2 files losslessly with zero server uploads.',
    intro:
      'Seedance AI video models (2.0, 2.1, and 2.2) by ByteDance generate viral motion clips with embedded MP4 container tags.',
    markers: [
      { kind: 'ByteDance Container Atoms', detail: 'MP4 moov and udta markers identifying Seedance engine versions.' },
      { kind: 'C2PA Manifests', detail: 'Provenance metadata scanned by TikTok and Reels.' },
    ],
    notes: 'Clean Seedance videos before uploading to social media to avoid automated AI badges.',
    faqs: [
      { q: 'Does this support Seedance 2.0, 2.1, and 2.2?', a: 'Yes. All Seedance version containers are fully supported.' },
    ],
  },
];
"""

with open('packages/shared/src/data/explainers.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("explainers.ts cleanly regenerated!")
