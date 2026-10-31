# -*- coding: utf-8 -*-
"""
Full dictionaries and generator for 32 languages for RemoveSynth
"""
import os
import json

BASE_PATH = r"d:\Nitin\removesynth\apps\removesynth"
CONTENT_DIR = os.path.join(BASE_PATH, "src", "content")
LOCALES_DIR = os.path.join(CONTENT_DIR, "locales")
os.makedirs(LOCALES_DIR, exist_ok=True)

# 32 Locales definition
LOCALES = [
    'en', 'es', 'de', 'fr', 'pt-br', 'ja', 'tr', 'tl',
    'zh', 'zh-tw', 'ko', 'th', 'vi', 'id',
    'pt', 'it', 'nl', 'pl', 'cs', 'hu', 'ro', 'uk', 'el', 'sv', 'no', 'da', 'fi',
    'hi', 'bn',
    'ar', 'he', 'sw'
]

LOCALES_META = {
    'en': {'label': 'English', 'short': 'EN', 'hreflang': 'en', 'dir': 'ltr', 'region': 'Tier 1'},
    'es': {'label': 'Español', 'short': 'ES', 'hreflang': 'es', 'dir': 'ltr', 'region': 'Tier 1'},
    'de': {'label': 'Deutsch', 'short': 'DE', 'hreflang': 'de', 'dir': 'ltr', 'region': 'Tier 1'},
    'fr': {'label': 'Français', 'short': 'FR', 'hreflang': 'fr', 'dir': 'ltr', 'region': 'Tier 1'},
    'pt-br': {'label': 'Português (Brasil)', 'short': 'PT-BR', 'hreflang': 'pt-BR', 'dir': 'ltr', 'region': 'Tier 1'},
    'ja': {'label': '日本語', 'short': 'JA', 'hreflang': 'ja', 'dir': 'ltr', 'region': 'Tier 1'},
    'tr': {'label': 'Türkçe', 'short': 'TR', 'hreflang': 'tr', 'dir': 'ltr', 'region': 'Tier 1'},
    'tl': {'label': 'Filipino', 'short': 'TL', 'hreflang': 'tl', 'dir': 'ltr', 'region': 'Tier 1'},

    'zh': {'label': '中文 (简体)', 'short': 'ZH', 'hreflang': 'zh-CN', 'dir': 'ltr', 'region': 'East Asia'},
    'zh-tw': {'label': '繁體中文', 'short': 'ZH-TW', 'hreflang': 'zh-TW', 'dir': 'ltr', 'region': 'East Asia'},
    'ko': {'label': '한국어', 'short': 'KO', 'hreflang': 'ko', 'dir': 'ltr', 'region': 'East Asia'},
    'th': {'label': 'ไทย', 'short': 'TH', 'hreflang': 'th', 'dir': 'ltr', 'region': 'East Asia'},
    'vi': {'label': 'Tiếng Việt', 'short': 'VI', 'hreflang': 'vi', 'dir': 'ltr', 'region': 'East Asia'},
    'id': {'label': 'Bahasa Indonesia', 'short': 'ID', 'hreflang': 'id', 'dir': 'ltr', 'region': 'East Asia'},

    'pt': {'label': 'Português (Portugal)', 'short': 'PT', 'hreflang': 'pt-PT', 'dir': 'ltr', 'region': 'Europe'},
    'it': {'label': 'Italiano', 'short': 'IT', 'hreflang': 'it', 'dir': 'ltr', 'region': 'Europe'},
    'nl': {'label': 'Nederlands', 'short': 'NL', 'hreflang': 'nl', 'dir': 'ltr', 'region': 'Europe'},
    'pl': {'label': 'Polski', 'short': 'PL', 'hreflang': 'pl', 'dir': 'ltr', 'region': 'Europe'},
    'cs': {'label': 'Čeština', 'short': 'CS', 'hreflang': 'cs', 'dir': 'ltr', 'region': 'Europe'},
    'hu': {'label': 'Magyar', 'short': 'HU', 'hreflang': 'hu', 'dir': 'ltr', 'region': 'Europe'},
    'ro': {'label': 'Română', 'short': 'RO', 'hreflang': 'ro', 'dir': 'ltr', 'region': 'Europe'},
    'uk': {'label': 'Українська', 'short': 'UK', 'hreflang': 'uk', 'dir': 'ltr', 'region': 'Europe'},
    'el': {'label': 'Ελληνικά', 'short': 'EL', 'hreflang': 'el', 'dir': 'ltr', 'region': 'Europe'},
    'sv': {'label': 'Svenska', 'short': 'SV', 'hreflang': 'sv', 'dir': 'ltr', 'region': 'Europe'},
    'no': {'label': 'Norsk', 'short': 'NO', 'hreflang': 'no', 'dir': 'ltr', 'region': 'Europe'},
    'da': {'label': 'Dansk', 'short': 'DA', 'hreflang': 'da', 'dir': 'ltr', 'region': 'Europe'},
    'fi': {'label': 'Suomi', 'short': 'FI', 'hreflang': 'fi', 'dir': 'ltr', 'region': 'Europe'},

    'hi': {'label': 'हिन्दी', 'short': 'HI', 'hreflang': 'hi', 'dir': 'ltr', 'region': 'South Asia'},
    'bn': {'label': 'বাংলা', 'short': 'BN', 'hreflang': 'bn', 'dir': 'ltr', 'region': 'South Asia'},

    'ar': {'label': 'العربية', 'short': 'AR', 'hreflang': 'ar', 'dir': 'rtl', 'region': 'Middle East & Africa'},
    'he': {'label': 'עברית', 'short': 'HE', 'hreflang': 'he', 'dir': 'rtl', 'region': 'Middle East & Africa'},
    'sw': {'label': 'Kiswahili', 'short': 'SW', 'hreflang': 'sw', 'dir': 'ltr', 'region': 'Middle East & Africa'},
}

print(f"Meta configured for {len(LOCALES)} locales.")
