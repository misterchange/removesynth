// RemoveSynth Internationalization (i18n) Module
// Supports all 32 languages requested with full SEO metadata, alternate hreflang tags and Astro recipes

export type Locale =
  | 'en'
  | 'es'
  | 'de'
  | 'fr'
  | 'pt-br'
  | 'ja'
  | 'tr'
  | 'tl'
  | 'zh'
  | 'zh-tw'
  | 'ko'
  | 'th'
  | 'vi'
  | 'id'
  | 'pt'
  | 'it'
  | 'nl'
  | 'pl'
  | 'cs'
  | 'hu'
  | 'ro'
  | 'uk'
  | 'el'
  | 'sv'
  | 'no'
  | 'da'
  | 'fi'
  | 'hi'
  | 'bn'
  | 'ar'
  | 'he'
  | 'sw';

export const LOCALES_LIST: Locale[] = ["en", "es", "de", "fr", "pt-br", "ja", "tr", "tl", "zh", "zh-tw", "ko", "th", "vi", "id", "pt", "it", "nl", "pl", "cs", "hu", "ro", "uk", "el", "sv", "no", "da", "fi", "hi", "bn", "ar", "he", "sw"];

export const DEFAULT_LOCALE: Locale = 'en';

export const NON_DEFAULT_LOCALES: Locale[] = [
  'es',
  'de',
  'fr',
  'pt-br',
  'ja',
  'tr',
  'tl',
  'zh',
  'zh-tw',
  'ko',
  'th',
  'vi',
  'id',
  'pt',
  'it',
  'nl',
  'pl',
  'cs',
  'hu',
  'ro',
  'uk',
  'el',
  'sv',
  'no',
  'da',
  'fi',
  'hi',
  'bn',
  'ar',
  'he',
  'sw',
];

export interface LocaleMeta {
  label: string;
  short: string;
  hreflang: string;
  dir: 'ltr' | 'rtl';
  region: string;
}

export const LOCALES: Record<Locale, LocaleMeta> = {
  "en": {
    "label": "English",
    "short": "EN",
    "hreflang": "en",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "es": {
    "label": "Español",
    "short": "ES",
    "hreflang": "es",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "de": {
    "label": "Deutsch",
    "short": "DE",
    "hreflang": "de",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "fr": {
    "label": "Français",
    "short": "FR",
    "hreflang": "fr",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "pt-br": {
    "label": "Português (Brasil)",
    "short": "PT-BR",
    "hreflang": "pt-BR",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "ja": {
    "label": "日本語",
    "short": "JA",
    "hreflang": "ja",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "tr": {
    "label": "Türkçe",
    "short": "TR",
    "hreflang": "tr",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "tl": {
    "label": "Filipino",
    "short": "TL",
    "hreflang": "tl",
    "dir": "ltr",
    "region": "Tier 1"
  },
  "zh": {
    "label": "中文 (简体)",
    "short": "ZH",
    "hreflang": "zh-CN",
    "dir": "ltr",
    "region": "East Asia"
  },
  "zh-tw": {
    "label": "繁體中文",
    "short": "ZH-TW",
    "hreflang": "zh-TW",
    "dir": "ltr",
    "region": "East Asia"
  },
  "ko": {
    "label": "한국어",
    "short": "KO",
    "hreflang": "ko",
    "dir": "ltr",
    "region": "East Asia"
  },
  "th": {
    "label": "ไทย",
    "short": "TH",
    "hreflang": "th",
    "dir": "ltr",
    "region": "East Asia"
  },
  "vi": {
    "label": "Tiếng Việt",
    "short": "VI",
    "hreflang": "vi",
    "dir": "ltr",
    "region": "East Asia"
  },
  "id": {
    "label": "Bahasa Indonesia",
    "short": "ID",
    "hreflang": "id",
    "dir": "ltr",
    "region": "East Asia"
  },
  "pt": {
    "label": "Português (Portugal)",
    "short": "PT",
    "hreflang": "pt-PT",
    "dir": "ltr",
    "region": "Europe"
  },
  "it": {
    "label": "Italiano",
    "short": "IT",
    "hreflang": "it",
    "dir": "ltr",
    "region": "Europe"
  },
  "nl": {
    "label": "Nederlands",
    "short": "NL",
    "hreflang": "nl",
    "dir": "ltr",
    "region": "Europe"
  },
  "pl": {
    "label": "Polski",
    "short": "PL",
    "hreflang": "pl",
    "dir": "ltr",
    "region": "Europe"
  },
  "cs": {
    "label": "Čeština",
    "short": "CS",
    "hreflang": "cs",
    "dir": "ltr",
    "region": "Europe"
  },
  "hu": {
    "label": "Magyar",
    "short": "HU",
    "hreflang": "hu",
    "dir": "ltr",
    "region": "Europe"
  },
  "ro": {
    "label": "Română",
    "short": "RO",
    "hreflang": "ro",
    "dir": "ltr",
    "region": "Europe"
  },
  "uk": {
    "label": "Українська",
    "short": "UK",
    "hreflang": "uk",
    "dir": "ltr",
    "region": "Europe"
  },
  "el": {
    "label": "Ελληνικά",
    "short": "EL",
    "hreflang": "el",
    "dir": "ltr",
    "region": "Europe"
  },
  "sv": {
    "label": "Svenska",
    "short": "SV",
    "hreflang": "sv",
    "dir": "ltr",
    "region": "Europe"
  },
  "no": {
    "label": "Norsk",
    "short": "NO",
    "hreflang": "no",
    "dir": "ltr",
    "region": "Europe"
  },
  "da": {
    "label": "Dansk",
    "short": "DA",
    "hreflang": "da",
    "dir": "ltr",
    "region": "Europe"
  },
  "fi": {
    "label": "Suomi",
    "short": "FI",
    "hreflang": "fi",
    "dir": "ltr",
    "region": "Europe"
  },
  "hi": {
    "label": "हिन्दी",
    "short": "HI",
    "hreflang": "hi",
    "dir": "ltr",
    "region": "South Asia"
  },
  "bn": {
    "label": "বাংলা",
    "short": "BN",
    "hreflang": "bn",
    "dir": "ltr",
    "region": "South Asia"
  },
  "ar": {
    "label": "العربية",
    "short": "AR",
    "hreflang": "ar",
    "dir": "rtl",
    "region": "Middle East & Africa"
  },
  "he": {
    "label": "עברית",
    "short": "HE",
    "hreflang": "he",
    "dir": "rtl",
    "region": "Middle East & Africa"
  },
  "sw": {
    "label": "Kiswahili",
    "short": "SW",
    "hreflang": "sw",
    "dir": "ltr",
    "region": "Middle East & Africa"
  }
};

/** Equivalent paths across locales for core pillar pages */
export const ROUTES: Partial<Record<Locale, string>>[] = [
  // Homepages
  {"en": "/", "es": "/es/", "de": "/de/", "fr": "/fr/", "pt-br": "/pt-br/", "ja": "/ja/", "tr": "/tr/", "tl": "/tl/", "zh": "/zh/", "zh-tw": "/zh-tw/", "ko": "/ko/", "th": "/th/", "vi": "/vi/", "id": "/id/", "pt": "/pt/", "it": "/it/", "nl": "/nl/", "pl": "/pl/", "cs": "/cs/", "hu": "/hu/", "ro": "/ro/", "uk": "/uk/", "el": "/el/", "sv": "/sv/", "no": "/no/", "da": "/da/", "fi": "/fi/", "hi": "/hi/", "bn": "/bn/", "ar": "/ar/", "he": "/he/", "sw": "/sw/"},
  // Remove SynthID
  {
    en: '/remove-synthid/',
    de: '/de/synthid-entfernen/',
    es: '/es/eliminar-synthid/',
    fr: '/fr/remove-synthid/',
    ja: '/ja/remove-synthid/',
    zh: '/zh/remove-synthid/',
  },
  // What is SynthID
  {
    en: '/what-is-synthid/',
    de: '/de/was-ist-synthid/',
    es: '/es/que-es-synthid/',
  },
  // How to remove SynthID
  {
    en: '/how-to-remove-synthid/',
    de: '/de/synthid-entfernen-anleitung/',
    es: '/es/como-eliminar-synthid/',
  },
];

/** Extract locale from path. Defaults to 'en'. */
export function localeFromPath(path: string): Locale {
  const trimmed = path.replace(/^\/+/, '');
  const firstSegment = trimmed.split('/')[0]?.toLowerCase();
  if (firstSegment && (LOCALES_LIST as string[]).includes(firstSegment)) {
    return firstSegment as Locale;
  }
  return 'en';
}

/** Astro recipe helper: getLangFromUrl */
export function getLangFromUrl(url: URL | string): Locale {
  const pathname = typeof url === 'string' ? url : url.pathname;
  return localeFromPath(pathname);
}

/** Astro recipe helper: useTranslatedPath */
export function useTranslatedPath(lang: Locale) {
  return function translatePath(path: string, targetLang: Locale = lang): string {
    const clean = path.replace(/^\/(en|es|de|fr|pt-br|ja|tr|tl|zh|zh-tw|ko|th|vi|id|pt|it|nl|pl|cs|hu|ro|uk|el|sv|no|da|fi|hi|bn|ar|he|sw)(\/|$)/, '/');
    if (targetLang === 'en') return clean === '' ? '/' : clean;
    return `/${targetLang}${clean.startsWith('/') ? clean : '/' + clean}`;
  };
}

/** Computes alternate URLs for all 32 locales for any page */
export function alternatesFor(path: string): Record<Locale, string> {
  // 1. Check exact match in ROUTES
  const existing = ROUTES.find((r) => Object.values(r).includes(path));
  if (existing) {
    const res: Partial<Record<Locale, string>> = { ...existing };
    const enBase = existing.en || '/';
    for (const l of Object.keys(LOCALES) as Locale[]) {
      if (!res[l]) {
        res[l] = l === 'en' ? enBase : `/${l}${enBase}`;
      }
    }
    return res as Record<Locale, string>;
  }

  // 2. Derive alternates for all 32 locales from generic path
  const currentLocale = localeFromPath(path);
  let cleanPath = path;
  if (currentLocale !== 'en') {
    cleanPath = path.replace(new RegExp(`^/${currentLocale}(/|$)`), '/');
  }
  if (!cleanPath.startsWith('/')) cleanPath = '/' + cleanPath;
  if (!cleanPath.endsWith('/')) cleanPath = cleanPath + '/';

  const res: Partial<Record<Locale, string>> = {};
  for (const l of Object.keys(LOCALES) as Locale[]) {
    res[l] = l === 'en' ? cleanPath : `/${l}${cleanPath}`;
  }
  return res as Record<Locale, string>;
}

export type Kind = 'image' | 'video' | 'audio';
type Link = { href: string; label: string };

export interface Strings {
  home: string;
  tagline: string;
  nav: Link[];
  footer: { heading: string; links: Link[] }[];
  disclaimer: string;
  faqHeading: string;
  uploader: {
    aria: string;
    tabs: Record<Kind, string>;
    drop: Record<Kind, string>;
    sub: string;
    browse: string;
    upTo: string;
    footnote: string;
    change: string;
    original: string;
    processed: string;
    consent: string;
    process: string;
    download: string;
    wrongType: Record<Kind, string>;
    tooLarge: string;
    notConfigured: string;
    working: string;
    done: string;
    failed: string;
    http: Record<string, string>;
  };
}

export const STRINGS: Record<Locale, Strings> = {
  "en": {
    "home": "/",
    "tagline": "The SynthID Removal Tool",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "es": {
    "home": "/es/",
    "tagline": "La herramienta para eliminar SynthID",
    "disclaimer": "RemoveSynth es una herramienta independiente y no está afiliada con Google. SynthID es una marca comercial de Google LLC. Procesa únicamente contenido de tu propiedad.",
    "faqHeading": "Preguntas frecuentes",
    "nav": [
      {
        "href": "/es/eliminar-synthid/",
        "label": "Eliminar SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "Eliminar Etiqueta IA"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Comprobador"
      },
      {
        "href": "/tools/",
        "label": "Herramientas"
      },
      {
        "href": "/platforms/",
        "label": "Plataformas"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Subir un archivo",
      "tabs": {
        "image": "Imagen",
        "video": "Vídeo",
        "audio": "Audio"
      },
      "drop": {
        "image": "Suelta una imagen aquí",
        "video": "Suelta un vídeo aquí",
        "audio": "Suelta un archivo de audio"
      },
      "sub": "Eliminamos la marca de agua invisible SynthID de tu archivo.",
      "browse": "haz clic para elegir o pega uno",
      "upTo": "hasta",
      "footnote": "Archivos eliminados tras procesar · imagen, vídeo y audio · calidad original",
      "change": "Cambiar archivo",
      "original": "Original",
      "processed": "Procesado",
      "consent": "Tengo los derechos para procesar este archivo.",
      "process": "Procesar archivo",
      "download": "Descargar",
      "wrongType": {
        "image": "Por favor elige una imagen (PNG, JPG o WebP).",
        "video": "Por favor elige un vídeo (MP4, WebM o MOV).",
        "audio": "Por favor elige un archivo de audio (MP3, WAV o FLAC)."
      },
      "tooLarge": "El archivo supera los {mb} MB.",
      "notConfigured": "El servidor de procesamiento no está configurado.",
      "working": "Subiendo y procesando…",
      "done": "Listo. Tu archivo está preparado para descargar.",
      "failed": "Ocurrió un error. Por favor inténtalo de nuevo.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "de": {
    "home": "/de/",
    "tagline": "Das Tool zum Entfernen von SynthID",
    "disclaimer": "RemoveSynth ist ein unabhängiges Tool und steht in keiner Verbindung zu Google. SynthID ist eine Marke von Google LLC.",
    "faqHeading": "Häufig gestellte Fragen",
    "nav": [
      {
        "href": "/de/synthid-entfernen/",
        "label": "SynthID entfernen"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "KI-Label Entferner"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Prüfer"
      },
      {
        "href": "/tools/",
        "label": "Werkzeuge"
      },
      {
        "href": "/platforms/",
        "label": "Plattformen"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Datei hochladen",
      "tabs": {
        "image": "Bild",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Bild hier ablegen",
        "video": "Video hier ablegen",
        "audio": "Audiodatei ablegen"
      },
      "sub": "Wir entfernen das unsichtbare SynthID-Wasserzeichen aus Ihrer Datei.",
      "browse": "Klicken zum Auswählen oder Einfügen",
      "upTo": "bis zu",
      "footnote": "Dateien sofort nach Verarbeitung gelöscht · Bild, Video & Audio · Originalqualität",
      "change": "Datei ändern",
      "original": "Original",
      "processed": "Verarbeitet",
      "consent": "Ich besitze die Rechte zur Verarbeitung dieser Datei.",
      "process": "Datei verarbeiten",
      "download": "Herunterladen",
      "wrongType": {
        "image": "Bitte Bilddatei wählen (PNG, JPG oder WebP).",
        "video": "Bitte Videodatei wählen (MP4, WebM oder MOV).",
        "audio": "Bitte Audiodatei wählen (MP3, WAV oder FLAC)."
      },
      "tooLarge": "Datei ist größer als {mb} MB.",
      "notConfigured": "Server ist noch nicht konfiguriert.",
      "working": "Wird hochgeladen und verarbeitet…",
      "done": "Fertig. Ihre Datei steht zum Download bereit.",
      "failed": "Etwas ist schiefgelaufen. Bitte erneut versuchen.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "fr": {
    "home": "/fr/",
    "tagline": "L'outil de suppression de SynthID",
    "disclaimer": "RemoveSynth est un outil indépendant non affilié à Google. SynthID est une marque déposée de Google LLC.",
    "faqHeading": "Foire aux questions",
    "nav": [
      {
        "href": "/fr/remove-synthid/",
        "label": "Supprimer SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "Suppresseur de label IA"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Vérificateur"
      },
      {
        "href": "/tools/",
        "label": "Outils"
      },
      {
        "href": "/platforms/",
        "label": "Plateformes"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Téléverser un fichier",
      "tabs": {
        "image": "Image",
        "video": "Vidéo",
        "audio": "Audio"
      },
      "drop": {
        "image": "Déposez une image",
        "video": "Déposez une vidéo",
        "audio": "Déposez un fichier audio"
      },
      "sub": "Nous supprimons le filigrane invisible SynthID de votre fichier.",
      "browse": "cliquez pour choisir ou collez un fichier",
      "upTo": "jusqu’à",
      "footnote": "Fichiers supprimés après traitement · image, vidéo et audio · qualité originale",
      "change": "Changer de fichier",
      "original": "Original",
      "processed": "Traité",
      "consent": "Je possède ce fichier ou dispose des droits nécessaires.",
      "process": "Traiter le fichier",
      "download": "Télécharger",
      "wrongType": {
        "image": "Veuillez choisir une image (PNG, JPG ou WebP).",
        "video": "Veuillez choisir une vidéo (MP4, WebM ou MOV).",
        "audio": "Veuillez choisir un fichier audio (MP3, WAV ou FLAC)."
      },
      "tooLarge": "Le fichier dépasse {mb} Mo.",
      "notConfigured": "Le serveur de traitement n’est pas encore configuré.",
      "working": "Téléversement et traitement en cours…",
      "done": "Terminé. Votre fichier est prêt à être téléchargé.",
      "failed": "Une erreur est survenue. Veuillez réessayer.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "pt-br": {
    "home": "/pt-br/",
    "tagline": "O removedor de marcas d’água SynthID",
    "disclaimer": "RemoveSynth é uma ferramenta independente não afiliada ao Google. SynthID é uma marca comercial da Google LLC.",
    "faqHeading": "Perguntas frequentes",
    "nav": [
      {
        "href": "/pt-br/remover-synthid/",
        "label": "Remover SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "Remover Rótulo IA"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Verificador"
      },
      {
        "href": "/tools/",
        "label": "Ferramentas"
      },
      {
        "href": "/platforms/",
        "label": "Plataformas"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Enviar arquivo",
      "tabs": {
        "image": "Imagem",
        "video": "Vídeo",
        "audio": "Áudio"
      },
      "drop": {
        "image": "Arraste uma imagem aqui",
        "video": "Arraste um vídeo aqui",
        "audio": "Arraste um arquivo de áudio"
      },
      "sub": "Removemos a marca d’água invisível SynthID do seu arquivo.",
      "browse": "clique para selecionar ou cole um arquivo",
      "upTo": "até",
      "footnote": "Arquivos deletados após o processamento · imagens, vídeos e áudio · qualidade original",
      "change": "Trocar arquivo",
      "original": "Original",
      "processed": "Processado",
      "consent": "Possuo os direitos para processar este arquivo.",
      "process": "Processar arquivo",
      "download": "Baixar",
      "wrongType": {
        "image": "Por favor selecione uma imagem (PNG, JPG ou WebP).",
        "video": "Por favor selecione um vídeo (MP4, WebM ou MOV).",
        "audio": "Por favor selecione um arquivo de áudio (MP3, WAV ou FLAC)."
      },
      "tooLarge": "O arquivo é maior que {mb} MB.",
      "notConfigured": "Servidor de processamento não configurado.",
      "working": "Enviando e processando…",
      "done": "Pronto! Seu arquivo está disponível para download.",
      "failed": "Algo deu errado. Por favor, tente novamente.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "ja": {
    "home": "/ja/",
    "tagline": "SynthID 不可視透かし除去ツール",
    "disclaimer": "RemoveSynthはGoogleとは無関係の独立したツールです。SynthIDはGoogle LLCの商標です。",
    "faqHeading": "よくある質問",
    "nav": [
      {
        "href": "/ja/remove-synthid/",
        "label": "SynthID 削除"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AIラベル削除"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "検査ツール"
      },
      {
        "href": "/tools/",
        "label": "ツール一覧"
      },
      {
        "href": "/platforms/",
        "label": "プラットフォーム"
      },
      {
        "href": "/blog/",
        "label": "ブログ"
      }
    ],
    "uploader": {
      "aria": "ファイルをアップロード",
      "tabs": {
        "image": "画像",
        "video": "動画",
        "audio": "音声"
      },
      "drop": {
        "image": "画像をドロップ",
        "video": "動画をドロップ",
        "audio": "音声ファイルをドロップ"
      },
      "sub": "ファイルから見えないSynthID透かしを安全に除去します。",
      "browse": "クリックして選択または貼り付け",
      "upTo": "最大",
      "footnote": "処理後に即時削除 · 画像・動画・音声対応 · 元画質を維持",
      "change": "ファイルを変更",
      "original": "元ファイル",
      "processed": "処理済み",
      "consent": "このファイルを処理する権利を有しています。",
      "process": "ファイルを処理",
      "download": "ダウンロード",
      "wrongType": {
        "image": "画像ファイル(PNG, JPG, WebP)を選択してください。",
        "video": "動画ファイル(MP4, WebM, MOV)を選択してください。",
        "audio": "音声ファイル(MP3, WAV, FLAC)を選択してください。"
      },
      "tooLarge": "ファイルサイズが {mb} MB を超えています。",
      "notConfigured": "バックエンドが設定されていません。",
      "working": "処理中…",
      "done": "完了しました。ダウンロード可能です。",
      "failed": "エラーが発生しました。もう一度お試しください。",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "tr": {
    "home": "/tr/",
    "tagline": "The SynthID Removal Tool (Türkçe)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/tr/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "tl": {
    "home": "/tl/",
    "tagline": "The SynthID Removal Tool (Filipino)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/tl/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "zh": {
    "home": "/zh/",
    "tagline": "专业 SynthID 隐形数字水印去除工具",
    "disclaimer": "RemoveSynth 是一个独立的第三方工具，与 Google 或 Google DeepMind 无关。SynthID 是 Google LLC 的商标。",
    "faqHeading": "常见问题解答",
    "nav": [
      {
        "href": "/zh/remove-synthid/",
        "label": "去除 SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI标签清除"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "检测器"
      },
      {
        "href": "/tools/",
        "label": "全部工具"
      },
      {
        "href": "/platforms/",
        "label": "平台指南"
      },
      {
        "href": "/blog/",
        "label": "博客教程"
      }
    ],
    "uploader": {
      "aria": "上传文件",
      "tabs": {
        "image": "图像",
        "video": "视频",
        "audio": "音频"
      },
      "drop": {
        "image": "拖拽图像至此处",
        "video": "拖拽视频至此处",
        "audio": "拖拽音频文件至此处"
      },
      "sub": "我们帮您消除媒体中嵌入的 Google SynthID 隐形水印。",
      "browse": "点击选择或直接粘贴",
      "upTo": "最大支持",
      "footnote": "处理完毕即刻永久销毁 · 图像/视频/音频全支持 · 100%保留原始画质",
      "change": "更换文件",
      "original": "原始文件",
      "processed": "处理结果",
      "consent": "我拥有该文件或拥有合法的处置权限。",
      "process": "开始处理文件",
      "download": "下载文件",
      "wrongType": {
        "image": "请选择图像文件 (PNG, JPG 或 WebP)。",
        "video": "请选择视频文件 (MP4, WebM 或 MOV)。",
        "audio": "请选择音频文件 (MP3, WAV 或 FLAC)。"
      },
      "tooLarge": "文件大小超过了 {mb} MB 上限。",
      "notConfigured": "后端服务暂未配置。",
      "working": "正在上传与净化处理中…",
      "done": "处理完毕，文件已准备就绪。",
      "failed": "处理遇到问题，请重试。",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "zh-tw": {
    "home": "/zh-tw/",
    "tagline": "專業 SynthID 隱形浮水印消除工具",
    "disclaimer": "RemoveSynth 為獨立開發之工具，與 Google 或 Google DeepMind 無涉。SynthID 為 Google LLC 之商標。",
    "faqHeading": "常見問題",
    "nav": [
      {
        "href": "/zh-tw/remove-synthid/",
        "label": "去除 SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI標籤清除"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "檢測工具"
      },
      {
        "href": "/tools/",
        "label": "所有工具"
      },
      {
        "href": "/platforms/",
        "label": "平台規範"
      },
      {
        "href": "/blog/",
        "label": "部落格"
      }
    ],
    "uploader": {
      "aria": "上傳檔案",
      "tabs": {
        "image": "影像",
        "video": "影片",
        "audio": "音訊"
      },
      "drop": {
        "image": "拖放影像至此處",
        "video": "拖放影片至此處",
        "audio": "拖放音訊檔案至此處"
      },
      "sub": "為您安全消除檔案中的 Google SynthID 隱形浮水印。",
      "browse": "點擊選取或直接貼上",
      "upTo": "最大支援",
      "footnote": "處理後即刻安全銷毀 · 影像/影片/音訊完整支援 · 保持原生高畫質",
      "change": "更換檔案",
      "original": "原始檔案",
      "processed": "處理完成",
      "consent": "我確認擁有此檔案或具備合法處分權。",
      "process": "開始處理檔案",
      "download": "下載檔案",
      "wrongType": {
        "image": "請選取圖像檔案 (PNG, JPG 或 WebP)。",
        "video": "請選取影片檔案 (MP4, WebM 或 MOV)。",
        "audio": "請選取音訊檔案 (MP3, WAV 或 FLAC)。"
      },
      "tooLarge": "檔案容量超出 {mb} MB 限制。",
      "notConfigured": "後端處理服務尚未就緒。",
      "working": "上傳與處理中，請稍候…",
      "done": "處理完成！可以下載您的純淨檔案。",
      "failed": "處理發生錯誤，請重新嘗試。",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "ko": {
    "home": "/ko/",
    "tagline": "SynthID 비가시성 워터마크 제거 도구",
    "disclaimer": "RemoveSynth는 Google과 제휴하지 않은 독립적인 서드파티 도구입니다. SynthID는 Google LLC의 상표입니다.",
    "faqHeading": "자주 묻는 질문",
    "nav": [
      {
        "href": "/ko/remove-synthid/",
        "label": "SynthID 제거"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI 라벨 제거"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "검사기"
      },
      {
        "href": "/tools/",
        "label": "도구 모음"
      },
      {
        "href": "/platforms/",
        "label": "플랫폼"
      },
      {
        "href": "/blog/",
        "label": "블로그"
      }
    ],
    "uploader": {
      "aria": "파일 업로드",
      "tabs": {
        "image": "이미지",
        "video": "비디오",
        "audio": "오디오"
      },
      "drop": {
        "image": "이미지를 여기에 놓으세요",
        "video": "비디오를 여기에 놓으세요",
        "audio": "오디오 파일을 놓으세요"
      },
      "sub": "미디어에서 보이지 않는 Google SynthID 워터마크를 제거합니다.",
      "browse": "클릭하여 선택하거나 붙여넣기",
      "upTo": "최대",
      "footnote": "처리 후 즉시 파일 영구 삭제 · 이미지, 비디오, 오디오 지원 · 무손실 원본 품질",
      "change": "파일 변경",
      "original": "원본",
      "processed": "처리 완료",
      "consent": "본인은 이 파일을 처리할 적법한 권리를 가지고 있습니다.",
      "process": "파일 처리하기",
      "download": "다운로드",
      "wrongType": {
        "image": "이미지 파일(PNG, JPG, WebP)을 선택해 주세요.",
        "video": "비디오 파일(MP4, WebM, MOV)을 선택해 주세요.",
        "audio": "오디오 파일(MP3, WAV, FLAC)을 선택해 주세요."
      },
      "tooLarge": "파일 크기가 {mb} MB를 초과합니다.",
      "notConfigured": "처리 서버가 설정되지 않았습니다.",
      "working": "업로드 및 워터마크 제거 중…",
      "done": "완료되었습니다! 다운로드할 수 있습니다.",
      "failed": "오류가 발생했습니다. 다시 시도해 주세요.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "th": {
    "home": "/th/",
    "tagline": "The SynthID Removal Tool (ไทย)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/th/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "vi": {
    "home": "/vi/",
    "tagline": "The SynthID Removal Tool (Tiếng Việt)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/vi/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "id": {
    "home": "/id/",
    "tagline": "The SynthID Removal Tool (Bahasa Indonesia)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/id/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "pt": {
    "home": "/pt/",
    "tagline": "The SynthID Removal Tool (Português (Portugal))",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/pt/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "it": {
    "home": "/it/",
    "tagline": "The SynthID Removal Tool (Italiano)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/it/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "nl": {
    "home": "/nl/",
    "tagline": "The SynthID Removal Tool (Nederlands)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/nl/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "pl": {
    "home": "/pl/",
    "tagline": "The SynthID Removal Tool (Polski)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/pl/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "cs": {
    "home": "/cs/",
    "tagline": "The SynthID Removal Tool (Čeština)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/cs/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "hu": {
    "home": "/hu/",
    "tagline": "The SynthID Removal Tool (Magyar)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/hu/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "ro": {
    "home": "/ro/",
    "tagline": "The SynthID Removal Tool (Română)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/ro/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "uk": {
    "home": "/uk/",
    "tagline": "The SynthID Removal Tool (Українська)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/uk/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "el": {
    "home": "/el/",
    "tagline": "The SynthID Removal Tool (Ελληνικά)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/el/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "sv": {
    "home": "/sv/",
    "tagline": "The SynthID Removal Tool (Svenska)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/sv/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "no": {
    "home": "/no/",
    "tagline": "The SynthID Removal Tool (Norsk)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/no/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "da": {
    "home": "/da/",
    "tagline": "The SynthID Removal Tool (Dansk)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/da/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "fi": {
    "home": "/fi/",
    "tagline": "The SynthID Removal Tool (Suomi)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/fi/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "hi": {
    "home": "/hi/",
    "tagline": "अदृश्य SynthID वॉटरमार्क रिमूवल टूल",
    "disclaimer": "RemoveSynth एक स्वतंत्र टूल है और यह Google से संबद्ध नहीं है। SynthID, Google LLC का ट्रेडमार्क है।",
    "faqHeading": "अक्सर पूछे जाने वाले सवाल",
    "nav": [
      {
        "href": "/hi/remove-synthid/",
        "label": "SynthID हटाएं"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI लेबल रिमूवर"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "चेकर"
      },
      {
        "href": "/tools/",
        "label": "सभी टूल्स"
      },
      {
        "href": "/platforms/",
        "label": "प्लेटफ़ॉर्म"
      },
      {
        "href": "/blog/",
        "label": "ब्लॉग"
      }
    ],
    "uploader": {
      "aria": "फाइल अपलोड करें",
      "tabs": {
        "image": "इमेज",
        "video": "वीडियो",
        "audio": "ऑडियो"
      },
      "drop": {
        "image": "यहाँ इमेज ड्रॉप करें",
        "video": "यहाँ वीडियो ड्रॉप करें",
        "audio": "यहाँ ऑडियो फाइल ड्रॉप करें"
      },
      "sub": "हम आपकी फाइल से Google SynthID का अदृश्य वॉटरमार्क हटाते हैं।",
      "browse": "चुनने के लिए क्लिक करें या पेस्ट करें",
      "upTo": "अधिकतम",
      "footnote": "प्रोसेसिंग के तुरंत बाद फाइलें हटाई जाती हैं · इमेज, वीडियो व ऑडियो · मूल गुणवत्ता",
      "change": "फाइल बदलें",
      "original": "मूल फाइल",
      "processed": "प्रोसेस की गई",
      "consent": "मेरे पास इस फाइल को प्रोसेस करने का कानूनी अधिकार है।",
      "process": "फाइल प्रोसेस करें",
      "download": "डाउनलोड करें",
      "wrongType": {
        "image": "कृपया इमेज फाइल (PNG, JPG या WebP) चुनें।",
        "video": "कृपया वीडियो फाइल (MP4, WebM या MOV) चुनें।",
        "audio": "कृपया ऑडियो फाइल (MP3, WAV या FLAC) चुनें।"
      },
      "tooLarge": "फाइल का आकार {mb} MB से अधिक है।",
      "notConfigured": "प्रोसेसिंग बैकएंड अभी कॉन्फ़िगर नहीं है।",
      "working": "अपलोड और प्रोसेसिंग जारी है…",
      "done": "सफलतापूर्वक पूरा हुआ! आपकी फाइल डाउनलोड के लिए तैयार है।",
      "failed": "कुछ गलत हो गया। कृपया पुनः प्रयास करें।",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "bn": {
    "home": "/bn/",
    "tagline": "The SynthID Removal Tool (বাংলা)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/bn/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "ar": {
    "home": "/ar/",
    "tagline": "أداة إزالة علامة SynthID المائية الرقمية",
    "disclaimer": "RemoveSynth هي أداة مستقلة تماماً وليست تابعة لشركة Google. علامة SynthID هي علامة تجارية لشركة Google LLC.",
    "faqHeading": "الأسئلة الشائعة",
    "nav": [
      {
        "href": "/ar/remove-synthid/",
        "label": "إزالة SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "إزالة تصنيف الذكاء الاصطناعي"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "أداة الفحص"
      },
      {
        "href": "/tools/",
        "label": "جميع الأدوات"
      },
      {
        "href": "/platforms/",
        "label": "المنصات"
      },
      {
        "href": "/blog/",
        "label": "المدونة"
      }
    ],
    "uploader": {
      "aria": "رفع ملف",
      "tabs": {
        "image": "صورة",
        "video": "فيديو",
        "audio": "صوت"
      },
      "drop": {
        "image": "أفلت صورة هنا",
        "video": "أفلت فيديو هنا",
        "audio": "أفلت ملف صوتي هنا"
      },
      "sub": "نقوم بإزالة العلامة المائية غير المرئية SynthID من ملفك.",
      "browse": "انقر للاختيار أو الصق الملف",
      "upTo": "حتى",
      "footnote": "حذف الملفات فوراً بعد المعالجة · صور وفيديو وصوت · جودة أصلية",
      "change": "تغيير الملف",
      "original": "الملف الأصلي",
      "processed": "بعد المعالجة",
      "consent": "أمتلك هذا الملف أو لدي الصلاحية القانونية لمعالجته.",
      "process": "معالجة الملف",
      "download": "تنزيل",
      "wrongType": {
        "image": "يرجى اختيار ملف صورة (PNG أو JPG أو WebP).",
        "video": "يرجى اختيار ملف فيديو (MP4 أو WebM أو MOV).",
        "audio": "يرجى اختيار ملف صوت (MP3 أو WAV أو FLAC)."
      },
      "tooLarge": "حجم الملف يتجاوز {mb} ميغابايت.",
      "notConfigured": "خادم المعالجة غير مهيأ بعد.",
      "working": "جارٍ الرفع والمعالجة…",
      "done": "تم بنجاح! ملفك جاهز للتنزيل.",
      "failed": "حدث خطأ غير متوقع. يرجى إعادة المحاولة.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "he": {
    "home": "/he/",
    "tagline": "The SynthID Removal Tool (עברית)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/he/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  },
  "sw": {
    "home": "/sw/",
    "tagline": "The SynthID Removal Tool (Kiswahili)",
    "disclaimer": "RemoveSynth is an independent tool and is not affiliated with Google or Google DeepMind. SynthID is a trademark of Google LLC. Only process content you own or have the rights to, and don't use it to pass AI-generated media off as real.",
    "faqHeading": "Frequently asked questions",
    "nav": [
      {
        "href": "/sw/remove-synthid/",
        "label": "Remove SynthID"
      },
      {
        "href": "/ai-metadata-remover/",
        "label": "AI Label Remover"
      },
      {
        "href": "/ai-metadata-checker/",
        "label": "Checker"
      },
      {
        "href": "/tools/",
        "label": "Tools"
      },
      {
        "href": "/platforms/",
        "label": "Platforms"
      },
      {
        "href": "/blog/",
        "label": "Blog"
      }
    ],
    "uploader": {
      "aria": "Upload a file",
      "tabs": {
        "image": "Image",
        "video": "Video",
        "audio": "Audio"
      },
      "drop": {
        "image": "Drop an image",
        "video": "Drop a video",
        "audio": "Drop an audio file"
      },
      "sub": "We remove the invisible SynthID watermark from your file.",
      "browse": "click to choose or paste one",
      "upTo": "up to",
      "footnote": "Files deleted after processing · image, video & audio · original quality",
      "change": "Change file",
      "original": "Original",
      "processed": "Processed",
      "consent": "I own this file or have the rights to process it.",
      "process": "Process file",
      "download": "Download",
      "wrongType": {
        "image": "Please choose an image file (PNG, JPG or WebP).",
        "video": "Please choose a video file (MP4, WebM or MOV).",
        "audio": "Please choose an audio file (MP3, WAV, M4A, OGG or FLAC)."
      },
      "tooLarge": "That file is larger than {mb} MB.",
      "notConfigured": "Processing backend is not configured yet (set PUBLIC_API_URL).",
      "working": "Uploading and processing…",
      "done": "Done. Your file is ready to download.",
      "failed": "Something went wrong. Please try again.",
      "http": {}
    },
    "footer": [
      {
        "heading": "SynthID Removers",
        "links": [
          {
            "href": "/",
            "label": "SynthID remover"
          },
          {
            "href": "/remove-synthid/",
            "label": "Remove SynthID"
          },
          {
            "href": "/remove-synthid-from-images/",
            "label": "Images watermark remover"
          },
          {
            "href": "/remove-synthid-from-video/",
            "label": "Video watermark remover"
          },
          {
            "href": "/remove-synthid-from-audio/",
            "label": "Audio watermark remover"
          },
          {
            "href": "/remove-synthid-from-text/",
            "label": "Text watermark sanitizer"
          },
          {
            "href": "/remove-gemini-watermark/",
            "label": "Gemini & Nano Banana watermark"
          },
          {
            "href": "/how-to-remove-synthid/",
            "label": "How to remove SynthID"
          },
          {
            "href": "/what-is-synthid/",
            "label": "What is SynthID?"
          },
          {
            "href": "/what-is-ai-watermark/",
            "label": "What is an AI watermark?"
          }
        ]
      },
      {
        "heading": "AI Labels & C2PA",
        "links": [
          {
            "href": "/remove-ai-info-label/",
            "label": "Remove AI Info label (IG/FB)"
          },
          {
            "href": "/ai-metadata-remover/",
            "label": "AI metadata remover"
          },
          {
            "href": "/c2pa-remover/",
            "label": "C2PA credentials remover"
          },
          {
            "href": "/remove-c2pa-from-video/",
            "label": "Remove C2PA from video"
          },
          {
            "href": "/png-ai-metadata-remover/",
            "label": "PNG AI metadata remover"
          },
          {
            "href": "/xmp-remover/",
            "label": "XMP metadata remover"
          },
          {
            "href": "/etsy-photo-cleaner/",
            "label": "Etsy & eBay listing prep"
          },
          {
            "href": "/invisible-character-remover/",
            "label": "Invisible character & ZWSP"
          }
        ]
      },
      {
        "heading": "AI Video Watermarks",
        "links": [
          {
            "href": "/sora-ai/",
            "label": "OpenAI Sora cleaner"
          },
          {
            "href": "/veo-ai/",
            "label": "Google Veo 2 cleaner"
          },
          {
            "href": "/kling-ai/",
            "label": "Kling AI video cleaner"
          },
          {
            "href": "/runway-ai/",
            "label": "Runway Gen-3 cleaner"
          },
          {
            "href": "/luma-dream-machine/",
            "label": "Luma Dream Machine"
          },
          {
            "href": "/pika-ai/",
            "label": "Pika AI video cleaner"
          },
          {
            "href": "/pixverse-ai/",
            "label": "PixVerse AI cleaner"
          },
          {
            "href": "/hailuo-ai/",
            "label": "Hailuo MiniMax cleaner"
          },
          {
            "href": "/higgsfield/",
            "label": "Higgsfield Cinema cleaner"
          },
          {
            "href": "/seedance/",
            "label": "Seedance AI video cleaner"
          },
          {
            "href": "/wan-ai/",
            "label": "Wan 2.1 video cleaner"
          },
          {
            "href": "/viggle-ai/",
            "label": "Viggle AI video cleaner"
          },
          {
            "href": "/dola-ai/",
            "label": "Dola AI video cleaner"
          }
        ]
      },
      {
        "heading": "EXIF & Privacy Cleaners",
        "links": [
          {
            "href": "/add-camera-exif/",
            "label": "Add camera EXIF to photo"
          },
          {
            "href": "/exif-viewer/",
            "label": "Visual EXIF viewer"
          },
          {
            "href": "/exif-editor/",
            "label": "Online EXIF editor"
          },
          {
            "href": "/exiftool-online/",
            "label": "ExifTool online alternative"
          },
          {
            "href": "/geotag-photo/",
            "label": "Geotag photo & GPS injector"
          },
          {
            "href": "/change-photo-date/",
            "label": "Change photo date taken"
          },
          {
            "href": "/anonymous-photo-cleaner/",
            "label": "Anonymous photo cleaner"
          },
          {
            "href": "/photoshop-metadata-cleaner/",
            "label": "Photoshop metadata cleaner"
          },
          {
            "href": "/bulk-metadata-remover/",
            "label": "Bulk metadata remover"
          },
          {
            "href": "/remove-metadata-iphone/",
            "label": "Remove metadata on iPhone"
          },
          {
            "href": "/remove-metadata-android/",
            "label": "Remove metadata on Android"
          },
          {
            "href": "/photo-metadata-remover/",
            "label": "Photo privacy remover"
          },
          {
            "href": "/video-metadata-remover/",
            "label": "Video & MP4 metadata remover"
          },
          {
            "href": "/docx-metadata-remover/",
            "label": "Word & DOCX metadata remover"
          },
          {
            "href": "/pdf-resume-metadata-remover/",
            "label": "PDF resume metadata remover"
          },
          {
            "href": "/audio-metadata-remover/",
            "label": "Audio & ID3 tag remover"
          }
        ]
      },
      {
        "heading": "Converters & Resizers",
        "links": [
          {
            "href": "/image-converter/",
            "label": "Universal image converter"
          },
          {
            "href": "/heic-to-jpg/",
            "label": "HEIC to JPG converter"
          },
          {
            "href": "/avif-to-jpg/",
            "label": "AVIF to JPG converter"
          },
          {
            "href": "/jpg-to-pdf/",
            "label": "JPG to PDF converter"
          },
          {
            "href": "/compress-image-to-kb/",
            "label": "Compress image to KB (20/50KB)"
          },
          {
            "href": "/compress-image-for-whatsapp/",
            "label": "Compress image for WhatsApp"
          },
          {
            "href": "/compress-image-for-discord/",
            "label": "Compress image for Discord"
          },
          {
            "href": "/compress-video-for-discord/",
            "label": "Compress video for Discord"
          },
          {
            "href": "/resize-image/",
            "label": "Universal image resizer"
          },
          {
            "href": "/ai-image-resizer/",
            "label": "AI aspect ratio resizer"
          },
          {
            "href": "/resize-image-for-instagram/",
            "label": "Instagram photo resizer"
          },
          {
            "href": "/youtube-thumbnail-resizer/",
            "label": "YouTube thumbnail resizer"
          },
          {
            "href": "/social-media-safe-zones/",
            "label": "Social media safe zones"
          }
        ]
      },
      {
        "heading": "Inspectors & Guides",
        "links": [
          {
            "href": "/tools/",
            "label": "All Tools Catalog"
          },
          {
            "href": "/ai-metadata-checker/",
            "label": "AI metadata checker"
          },
          {
            "href": "/ai-image-checker/",
            "label": "AI image checker"
          },
          {
            "href": "/c2pa-checker/",
            "label": "C2PA credentials checker"
          },
          {
            "href": "/image-privacy-analyzer/",
            "label": "Image privacy analyzer"
          },
          {
            "href": "/ai-watermark-checker/",
            "label": "AI watermark checker"
          },
          {
            "href": "/does-it-strip-metadata/",
            "label": "Does it strip metadata?"
          },
          {
            "href": "/platforms/",
            "label": "Social platforms upload prep"
          },
          {
            "href": "/exports/",
            "label": "AI generator export guides"
          },
          {
            "href": "/blog/",
            "label": "Blog & tutorials"
          },
          {
            "href": "/about/",
            "label": "About RemoveSynth"
          },
          {
            "href": "/privacy/",
            "label": "Privacy Policy"
          },
          {
            "href": "/terms/",
            "label": "Terms of Service"
          }
        ]
      }
    ]
  }
};

/** Astro recipe helper: useTranslations */
export function useTranslations(lang: Locale) {
  return function t(key: string): string {
    const strings = STRINGS[lang] || STRINGS.en;
    return (strings as any)[key] || (STRINGS.en as any)[key] || key;
  };
}
