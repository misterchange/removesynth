export interface NavToolItem {
  href: string;
  label: string;
  desc: string;
  icon: string;
  badge?: string;
}

export interface NavCategory {
  id: string;
  title: string;
  tagline: string;
  icon: string;
  tools: NavToolItem[];
}

export const TOOL_CATEGORIES: NavCategory[] = [
  {
    id: 'synthid',
    title: 'SynthID Removers',
    tagline: 'Disperse invisible AI watermarks across modalities',
    icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>`,
    tools: [
      {
        href: '/remove-synthid/',
        label: 'Remove SynthID',
        desc: 'Universal detector & watermark cleaner',
        badge: 'Core',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
      },
      {
        href: '/remove-synthid-from-images/',
        label: 'Images Watermark Remover',
        desc: 'Clean Gemini & Imagen pixels',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>`,
      },
      {
        href: '/remove-synthid-from-video/',
        label: 'Video Watermark Remover',
        desc: 'Per-frame frequency dispersal for MP4/WebM',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2"/></svg>`,
      },
      {
        href: '/remove-synthid-from-audio/',
        label: 'Audio Watermark Remover',
        desc: 'Scrub Lyria & MusicLM waveforms losslessly',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>`,
      },
      {
        href: '/remove-synthid-from-text/',
        label: 'Text Watermark Sanitizer',
        desc: 'Disrupt token probability tracking marks',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 7 4 4 20 4 20 7"/><line x1="9" x2="15" y1="20" y2="20"/><line x1="12" x2="12" y1="4" y2="20"/></svg>`,
      },
      {
        href: '/remove-gemini-watermark/',
        label: 'Remove Gemini Watermark',
        desc: 'Nano Banana & Google Imagen cleaner',
        badge: 'Popular',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>`,
      },
    ],
  },
  {
    id: 'ai-label',
    title: 'AI Label & C2PA Cleaners',
    tagline: 'Remove "Made with AI" labels and credentials for social uploads',
    icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2H2v10l9.29 9.29c.94.94 2.48.94 3.42 0l6.58-6.58c.94-.94.94-2.48 0-3.42L12 2Z"/><path d="M7 7h.01"/></svg>`,
    tools: [
      {
        href: '/remove-ai-info-label/',
        label: 'Remove AI Info Label',
        desc: 'Stop Instagram, Facebook & Threads AI labels',
        badge: 'Hot',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>`,
      },
      {
        href: '/ai-metadata-remover/',
        label: 'AI Metadata & Header Remover',
        desc: 'Strip C2PA, XMP & IPTC generative tags',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 4H3a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2z"/><line x1="1" x2="23" y1="10" y2="10"/></svg>`,
      },
      {
        href: '/c2pa-remover/',
        label: 'C2PA Manifest Remover',
        desc: 'Wipe Content Credentials manifests losslessly',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>`,
      },
      {
        href: '/remove-c2pa-from-video/',
        label: 'Remove C2PA from Video',
        desc: 'Sanitize MP4/MOV manifests for Reels & TikTok',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect width="14" height="14" x="1" y="5" rx="2" ry="2"/></svg>`,
      },
      {
        href: '/png-ai-metadata-remover/',
        label: 'PNG AI Metadata Remover',
        desc: 'Strip ComfyUI, WebUI, and generation prompt chunks',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>`,
      },
      {
        href: '/xmp-remover/',
        label: 'XMP Metadata Remover',
        desc: 'Purge Adobe XMP sidecars and embedded RDF packets',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`,
      },
    ],
  },
  {
    id: 'ai-video',
    title: 'AI Video Watermark Cleaners',
    tagline: 'Clean model stamps, container atoms & metadata from AI generators',
    icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>`,
    tools: [
      {
        href: '/sora-ai/',
        label: 'OpenAI Sora Cleaner',
        desc: 'Strip Sora container metadata & C2PA tags',
        badge: 'New',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/></svg>`,
      },
      {
        href: '/veo-ai/',
        label: 'Google Veo 2 Cleaner',
        desc: 'Clean Veo 2 SynthID & container markers',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>`,
      },
      {
        href: '/kling-ai/',
        label: 'Kling AI Video Cleaner',
        desc: 'Wipe Kling 1.0 / 1.5 / 2.0 container atoms',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" x2="4" y1="22" y2="15"/></svg>`,
      },
      {
        href: '/runway-ai/',
        label: 'Runway Gen-3 Cleaner',
        desc: 'Sanitize Gen-3 & Gen-2 MP4 containers losslessly',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m13 2-2 2.5V8l2-2 5 5-2 2h3.5L22 13Z"/><path d="m11 22 2-2.5V16l-2 2-5-5 2-2H4.5L2 11Z"/></svg>`,
      },
      {
        href: '/luma-dream-machine/',
        label: 'Luma Dream Machine Cleaner',
        desc: 'Strip Ray-2 metadata and credentials',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>`,
      },
      {
        href: '/pika-ai/',
        label: 'Pika AI Video Cleaner',
        desc: 'Clean Pika 2.0 animated logo watermarks & tags',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>`,
      },
      {
        href: '/pixverse-ai/',
        label: 'PixVerse AI Cleaner',
        desc: 'Remove PixVerse 4K video tags for Reels',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="m9 8 6 4-6 4Z"/></svg>`,
      },
      {
        href: '/hailuo-ai/',
        label: 'Hailuo MiniMax Cleaner',
        desc: 'Sanitize Video-01 container atoms for Shorts',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/></svg>`,
      },
      {
        href: '/higgsfield/',
        label: 'Higgsfield Cinema Cleaner',
        desc: 'Clean Higgsfield DoP video atoms losslessly',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20"/><path d="M20 12v8H4v-8"/><path d="m4 4 16 16"/></svg>`,
      },
      {
        href: '/seedance/',
        label: 'Seedance AI Video Cleaner',
        desc: 'Sanitize ByteDance Seedance 2.0 / 2.1 / 2.2 MP4s',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"/></svg>`,
      },
      {
        href: '/wan-ai/',
        label: 'Wan 2.1 Video Cleaner',
        desc: 'Sanitize Alibaba Wanx open model tags',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>`,
      },
      {
        href: '/viggle-ai/',
        label: 'Viggle AI Video Cleaner',
        desc: 'Clean character motion & dance video metadata',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="3"/><path d="m9 20 3-6 3 6"/><path d="m6 8 6 2 6-2"/></svg>`,
      },
      {
        href: '/dola-ai/',
        label: 'Dola AI Video Cleaner',
        desc: 'Wipe Dola AI video watermarks & provenance',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/></svg>`,
      },
    ],
  },
  {
    id: 'exif-privacy',
    title: 'EXIF & Privacy Tools',
    tagline: 'Inspect, edit, inject, and wipe camera hardware tags & GPS',
    icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>`,
    tools: [
      {
        href: '/add-camera-exif/',
        label: 'Add Camera EXIF to Photo',
        desc: 'Inject realistic Sony, Canon & iPhone camera tags',
        badge: 'Popular',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>`,
      },
      {
        href: '/exif-viewer/',
        label: 'Visual EXIF Viewer',
        desc: 'Inspect shutter speed, f-stop, ISO & GPS coordinates',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>`,
      },
      {
        href: '/exif-editor/',
        label: 'Online EXIF Editor',
        desc: 'Edit or remove individual EXIF tags tag-by-tag',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/></svg>`,
      },
      {
        href: '/exiftool-online/',
        label: 'ExifTool Online Alternative',
        desc: 'Zero-install browser equivalent of exiftool -all=',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg>`,
      },
      {
        href: '/geotag-photo/',
        label: 'Geotag Photo & GPS Injector',
        desc: 'Add or modify EXIF GPS coordinates via map',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/><circle cx="12" cy="10" r="3"/></svg>`,
      },
      {
        href: '/change-photo-date/',
        label: 'Change Photo Date Taken',
        desc: 'Losslessly rewrite creation and capture timestamps',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>`,
      },
      {
        href: '/photo-metadata-remover/',
        label: 'Photo Privacy Remover',
        desc: 'Scrub GPS, camera serials, and dates from photos',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/><path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/><path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"/><line x1="2" x2="22" y1="2" y2="22"/></svg>`,
      },
      {
        href: '/bulk-metadata-remover/',
        label: 'Bulk Metadata Remover',
        desc: 'Clean up to 50 photos at once with ZIP download',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>`,
      },
      {
        href: '/anonymous-photo-cleaner/',
        label: 'Anonymous Photo Cleaner',
        desc: 'Reddit & safe-share cleaner for whistleblowers',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 15h8"/><circle cx="9" cy="9" r="1"/><circle cx="15" cy="9" r="1"/></svg>`,
      },
      {
        href: '/photoshop-metadata-cleaner/',
        label: 'Photoshop Metadata Cleaner',
        desc: 'Fix DocumentAncestors bloat & shrink file size',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m14 12-8.5 8.5a2.12 2.12 0 1 1-3-3L11 9"/><path d="M15 13 9 7l4-4 6 6h3a8 8 0 0 1-7 7z"/></svg>`,
      },
      {
        href: '/remove-metadata-iphone/',
        label: 'iPhone Metadata Remover',
        desc: 'Mobile-first 1-tap cleaner for iOS Safari',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><line x1="12" x2="12.01" y1="18" y2="18"/></svg>`,
      },
      {
        href: '/remove-metadata-android/',
        label: 'Android Metadata Remover',
        desc: 'Scrub Samsung & Pixel GPS & sensor tags',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2"/><circle cx="12" cy="18" r="1"/></svg>`,
      },
      {
        href: '/video-metadata-remover/',
        label: 'Video & MP4 Metadata Remover',
        desc: 'Losslessly strip GPS tracks & camera atom tags',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect width="14" height="14" x="1" y="5" rx="2" ry="2"/></svg>`,
      },
      {
        href: '/docx-metadata-remover/',
        label: 'Word & DOCX Cleaner',
        desc: 'Scrub author revision history and company tags',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/></svg>`,
      },
      {
        href: '/pdf-resume-metadata-remover/',
        label: 'PDF Resume Metadata Remover',
        desc: 'Blind hiring sanitizer for CVs and applications',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`,
      },
      {
        href: '/audio-metadata-remover/',
        label: 'Audio ID3 Tag Remover',
        desc: 'Remove artist, comments and DAW tags losslessly',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>`,
      },
      {
        href: '/invisible-character-remover/',
        label: 'Invisible Character Remover',
        desc: 'Scrub zero-width spaces (ZWSP) and unicode marks',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg>`,
      },
      {
        href: '/etsy-photo-cleaner/',
        label: 'Etsy & eBay Listing Cleaner',
        desc: 'Scrub AI prompts & serial numbers before listing',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><line x1="3" x2="21" y1="6" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>`,
      },
    ],
  },
  {
    id: 'converters-resizers',
    title: 'Converters & Resizers',
    tagline: 'Lossless format transcoding and aspect ratio optimizations',
    icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"/><line x1="4" x2="21" y1="20" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" x2="21" y1="15" y2="21"/><path d="M4 4l5 5"/></svg>`,
    tools: [
      {
        href: '/image-converter/',
        label: 'Universal Image Converter',
        desc: 'Batch convert between JPG, PNG, WebP, AVIF, HEIC',
        badge: 'Universal',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>`,
      },
      {
        href: '/heic-to-jpg/',
        label: 'HEIC to JPG Converter',
        desc: 'Convert Apple iPhone HEIC photos for Windows & web',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>`,
      },
      {
        href: '/avif-to-jpg/',
        label: 'AVIF to JPG Converter',
        desc: 'Convert modern web AVIF images to universal JPG',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg>`,
      },
      {
        href: '/jpg-to-pdf/',
        label: 'JPG to PDF Converter',
        desc: 'Merge single or multiple photos into one clean PDF',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><text x="8" y="16" fill="currentColor" font-size="6" font-family="sans-serif" font-weight="bold">PDF</text></svg>`,
      },
      {
        href: '/compress-image-to-kb/',
        label: 'Compress Image to KB',
        desc: 'Hit exact 20KB, 50KB, 100KB limits for online forms',
        badge: 'Top',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 14 10 14 10 20"/><polyline points="20 10 14 10 14 4"/><line x1="14" x2="21" y1="10" y2="3"/><line x1="3" x2="10" y1="21" y2="14"/></svg>`,
      },
      {
        href: '/compress-image-for-whatsapp/',
        label: 'Compress Image for WhatsApp',
        desc: 'Scrub location while keeping facial details sharp',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>`,
      },
      {
        href: '/compress-image-for-discord/',
        label: 'Compress Image for Discord',
        desc: 'Fix "file too powerful" for avatars and channel uploads',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="12" r="1.5"/><circle cx="15" cy="12" r="1.5"/><path d="M7.5 7.5c3.5-1 5.5-1 9 0"/><path d="M7 16.5c3.5 1 6.5 1 10 0"/></svg>`,
      },
      {
        href: '/compress-video-for-discord/',
        label: 'Compress Video for Discord',
        desc: 'Compress clips under Discord free 10MB upload ceiling',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect width="14" height="14" x="1" y="5" rx="2" ry="2"/></svg>`,
      },
      {
        href: '/resize-image/',
        label: 'Universal Image Resizer',
        desc: 'Resize images by pixel dimensions or percentages',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-7 7"/><path d="M3 21l7-7"/></svg>`,
      },
      {
        href: '/ai-image-resizer/',
        label: 'AI Aspect Ratio Resizer',
        desc: 'Smart-blur background fitting for Midjourney 1:1 to 16:9',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="12" x="3" y="6" rx="2"/></svg>`,
      },
      {
        href: '/resize-image-for-instagram/',
        label: 'Instagram Photo Resizer',
        desc: 'No-crop 4:5 portrait & 1:1 square canvas creator',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/></svg>`,
      },
      {
        href: '/youtube-thumbnail-resizer/',
        label: 'YouTube Thumbnail Resizer',
        desc: 'Fit artwork to exact 1280x720 canvas dimensions',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>`,
      },
      {
        href: '/social-media-safe-zones/',
        label: 'Social Media Safe Zones',
        desc: 'Interactive UI overlay preview for Reels, TikTok & Shorts',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><line x1="9" x2="9" y1="3" y2="21"/><line x1="15" x2="15" y1="3" y2="21"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="3" x2="21" y1="15" y2="15"/></svg>`,
      },
    ],
  },
  {
    id: 'inspectors',
    title: 'Inspectors & Checkers',
    tagline: 'Audit files for hidden metadata, C2PA chains, and platform strip rules',
    icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/></svg>`,
    tools: [
      {
        href: '/ai-metadata-checker/',
        label: 'AI Metadata Checker',
        desc: 'Inspect C2PA, IPTC and hidden generation markers',
        badge: 'Core',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>`,
      },
      {
        href: '/ai-image-checker/',
        label: 'AI Image Checker',
        desc: 'Detect whether a photo has synthetic generator headers',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/></svg>`,
      },
      {
        href: '/c2pa-checker/',
        label: 'C2PA Manifest Inspector',
        desc: 'Inspect digital signatures, signing orgs and edit chains',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
      },
      {
        href: '/image-privacy-analyzer/',
        label: 'Image Privacy Analyzer',
        desc: 'Scan for embedded GPS coordinates and device fingerprints',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/><circle cx="12" cy="10" r="3"/></svg>`,
      },
      {
        href: '/ai-watermark-checker/',
        label: 'AI Watermark Checker',
        desc: 'Verify if invisible statistical watermarks are detected',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>`,
      },
      {
        href: '/does-it-strip-metadata/',
        label: 'Does It Strip Metadata?',
        desc: 'Privacy comparison matrix across 12 social & messaging apps',
        icon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>`,
      },
    ],
  },
];
