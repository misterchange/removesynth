import type { HomeContent } from '../types';

export const en: HomeContent = {
  "lang": "en",
  "title": "Remove AI Detection and Metadata from Images, Videos, Audio & Text",
  "description": "Free online AI metadata and watermark remover for AI images, AI video, AI audio and AI-generated text. Upload PNG, JPG, WebP, AVIF, HEIC, MP4, MOV, WebM, MKV, MP3, WAV, OGG, FLAC, M4A, TXT, DOCX or PDF to strip SynthID and C2PA losslessly in-browser with zero uploads.",
  "hero": {
    "eyebrow": "No sign-up · Free · Images, video & audio",
    "h1Before": "Free ",
    "h1Accent": "SynthID remover",
    "h1After": " online",
    "lead": "Remove SynthID from AI-generated images and videos. Upload your file, process it in one click, and download it in its original format and quality.",
    "checks": [
      "Images, video & audio",
      "Every video frame",
      "Files deleted after processing"
    ],
    "worksWith": "Works with files from"
  },
  "features": [
    {
      "title": "Images and video",
      "text": "One SynthID remover for PNG, JPG and WebP stills and MP4, WebM and MOV clips."
    },
    {
      "title": "Every frame",
      "text": "On video, the whole clip is processed, not just a few sample frames."
    },
    {
      "title": "Original quality",
      "text": "Your file keeps its resolution, format and frame rate."
    },
    {
      "title": "No sign-up",
      "text": "Drop a file and go. No account needed during early access."
    },
    {
      "title": "Files deleted",
      "text": "Uploads are deleted as soon as your result is sent back. Nothing is kept."
    },
    {
      "title": "Works anywhere",
      "text": "Runs in any modern browser on desktop, tablet or phone."
    }
  ],
  "inside": {
    "kicker": "What’s inside an AI file",
    "h2": "Two ways AI content gets labelled",
    "p": "Most AI tools mark what they generate. Neither mark is visible.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "An invisible signal in the pixels",
        "html": "SynthID (sometimes written “Synth ID”) is woven into the image data and across every video frame. You can’t see it, and it is built to survive cropping, filters, compression and screenshots. <a href=\"/what-is-synthid/\">What is SynthID?</a>"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "A signed record in the metadata",
        "html": "Many generators also attach C2PA Content Credentials, a signed note in the file’s metadata saying how it was made. <a href=\"/blog/synthid-vs-c2pa/\">SynthID vs C2PA</a>"
      }
    ]
  },
  "how": {
    "kicker": "How it works",
    "h2": "Remove SynthID in four steps",
    "steps": [
      {
        "title": "Drop your file",
        "text": "Choose an image or video made with a tool that applies SynthID, such as Gemini, Imagen or Veo."
      },
      {
        "title": "Confirm your rights",
        "text": "Tick the box to confirm you own the file or are allowed to process it."
      },
      {
        "title": "We process it",
        "text": "Your file is checked and processed on our server, frame by frame for video."
      },
      {
        "title": "Download",
        "text": "Compare before and after, then download the result in its original format."
      }
    ]
  },
  "plans": {
    "kicker": "Plans",
    "h2": "Free while in early access",
    "p": "Every feature is free during early access. Paid plans will add higher limits.",
    "free": {
      "name": "Free",
      "note": "no card needed",
      "items": [
        "Images and video",
        "Up to 50 MB per file",
        "Original quality",
        "No account needed"
      ],
      "cta": "Process a file"
    },
    "pro": {
      "badge": "Coming soon",
      "price": "Credits",
      "note": "monthly or yearly",
      "items": [
        "Larger files and longer videos",
        "Batch processing",
        "Priority processing",
        "API access"
      ]
    }
  },
  "hood": {
    "kicker": "Under the hood",
    "h2": "Built for quality and privacy",
    "cards": [
      {
        "title": "Every frame processed",
        "text": "Video is handled across the whole clip, so nothing is skipped between frames.",
        "tag": "frame 1 → 240 · done"
      },
      {
        "title": "Nothing kept",
        "text": "Files live in a temporary folder only while they’re processed, then they’re deleted.",
        "tag": "0 files stored"
      },
      {
        "title": "Original quality",
        "text": "Resolution, format and frame rate stay the same as the file you uploaded.",
        "tag": "1080×1920 · 30fps → 1080×1920 · 30fps"
      }
    ]
  },
  "who": {
    "kicker": "Who it’s for",
    "h2": "Built for people who work with their own AI media",
    "cards": [
      {
        "title": "Creators",
        "text": "You made the image or video and want the clean file you intended to export."
      },
      {
        "title": "Researchers & journalists",
        "text": "You’re testing watermark robustness and need a fast way to test files."
      },
      {
        "title": "Developers",
        "text": "You’re building media pipelines and want an API for batch processing. Coming soon."
      }
    ],
    "note": "Only process files you own or have permission to use, and always be transparent about how your media was made."
  },
  "seo": [
    {
      "h2": "How to use the SynthID remover",
      "html": "Drop your file into the box above, tick the confirmation to confirm your rights, and click <strong>Process file</strong>. Once it finishes, compare the before and after, then download the result. Read our step-by-step guide on <a href=\"/how-to-remove-synthid/\">how to remove SynthID watermarks</a> for more detail."
    },
    {
      "h2": "Which AI tools add SynthID?",
      "html": "Google adds SynthID to media generated across its AI products, including the Gemini app, Imagen and Veo."
    },
    {
      "h2": "Why editing doesn’t remove SynthID",
      "html": "SynthID isn’t a logo or a metadata tag. It’s woven into the pixels themselves, and Google designed it specifically to survive cropping, resizing, filters, compression and screenshots. Stripping metadata doesn’t touch it either. That’s why you need a dedicated tool to <a href=\"/remove-synthid/\">remove SynthID</a>."
    }
  ],
  "faqHeading": "Frequently asked questions",
  "faqs": [
    {
      "q": "What is a SynthID remover?",
      "a": "A SynthID remover is a tool that processes AI-generated images and videos carrying Google’s SynthID watermark. RemoveSynth is a free online tool: you upload a file and download a processed version."
    },
    {
      "q": "Is this SynthID remover free?",
      "a": "Yes. While in early access, RemoveSynth is completely free to use. Paid plans with higher limits and batch processing will be added later."
    },
    {
      "q": "What file types can I upload?",
      "a": "You can upload PNG, JPG and WebP images, and MP4, WebM and MOV videos up to the file size listed below the uploader."
    },
    {
      "q": "Do you keep my files?",
      "a": "No. Files are held in a temporary directory while being processed and deleted as soon as your download is ready. We never store them, use them for training, or share them."
    },
    {
      "q": "Does cropping or taking a screenshot remove SynthID?",
      "a": "No, not reliably. SynthID is embedded in the pixel data across the image and is designed to survive standard edits, screenshots and re-saving."
    },
    {
      "q": "Is RemoveSynth affiliated with Google?",
      "a": "No. RemoveSynth is an independent tool. SynthID is a technology and trademark of Google LLC."
    }
  ],
  "cta": {
    "h2": "Try the SynthID remover",
    "p": "Free, no sign-up, works on images and video.",
    "button": "Remove SynthID now"
  }
};
