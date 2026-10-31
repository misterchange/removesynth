# -*- coding: utf-8 -*-
"""
Builder for 32 i18n locales for RemoveSynth.
"""
import os
import json

BASE_PATH = r"d:\Nitin\removesynth\apps\removesynth"
CONTENT_DIR = os.path.join(BASE_PATH, "src", "content")
LOCALES_DIR = os.path.join(CONTENT_DIR, "locales")
os.makedirs(LOCALES_DIR, exist_ok=True)

# Write types.ts
types_ts = '''import type { FaqItem } from '@removesynth/shared/lib/faq';

export interface HomeContent {
  lang: string;
  title: string;
  description: string;
  hero: {
    eyebrow: string;
    h1Before: string;
    h1Accent: string;
    h1After: string;
    lead: string;
    checks: string[];
    worksWith: string;
  };
  features: { title: string; text: string }[];
  inside: {
    kicker: string;
    h2: string;
    p: string;
    cards: { kicker: string; title: string; html: string }[];
  };
  how: { kicker: string; h2: string; steps: { title: string; text: string }[] };
  plans: {
    kicker: string;
    h2: string;
    p: string;
    free: { name: string; note: string; items: string[]; cta: string };
    pro: { badge: string; price: string; note: string; items: string[] };
  };
  hood: { kicker: string; h2: string; cards: { title: string; text: string; tag: string }[] };
  who: { kicker: string; h2: string; cards: { title: string; text: string }[]; note: string };
  seo: { h2: string; html: string }[];
  faqHeading: string;
  faqs: FaqItem[];
  cta: { h2: string; p: string; button: string };
}
'''
with open(os.path.join(CONTENT_DIR, "types.ts"), "w", encoding="utf-8") as f:
    f.write(types_ts)

print("types.ts written.")
