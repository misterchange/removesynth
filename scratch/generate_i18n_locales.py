# -*- coding: utf-8 -*-
"""
Generates the modular locale files for all 32 languages for RemoveSynth
"""
import os
import json

BASE_PATH = r"d:\Nitin\removesynth\apps\removesynth"
CONTENT_DIR = os.path.join(BASE_PATH, "src", "content")
LOCALES_DIR = os.path.join(CONTENT_DIR, "locales")
os.makedirs(LOCALES_DIR, exist_ok=True)

# Helper to write a locale file
def write_locale(lang_code, var_name, data):
    ts_code = f"""import type {{ HomeContent }} from '../types';

export const {var_name}: HomeContent = {json.dumps(data, ensure_ascii=False, indent=2)};
"""
    file_path = os.path.join(LOCALES_DIR, f"{lang_code}.ts")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(ts_code)
    print(f"Wrote {lang_code}.ts")

print("Generator helper ready.")
