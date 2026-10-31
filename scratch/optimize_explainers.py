import re

with open('packages/shared/src/data/explainers.ts', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace curly quotes and apostrophes in explainers.ts
code = code.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
code = code.replace('—', '-').replace('–', '-')

# Specific title replacements
title_fixes = {
    'Instagram "AI info" Label: What Triggers It and How to Check Your Photos': 'Instagram AI info Label: What Triggers It and How to Check',
    'TikTok AI-Generated Label: How TikTok Detects and Labels AI Content': 'TikTok AI Label: How TikTok Detects and Flags AI Media',
    'Does X (Twitter) Label AI Images? Synthetic Media Rules Explained': 'Does X Label AI Images? Synthetic Media Rules Explained',
    'ChatGPT Image Metadata: Does ChatGPT Add C2PA Content Credentials?': 'ChatGPT Image Metadata: Does ChatGPT Add C2PA Credentials?',
    'Adobe Firefly Content Credentials: What Metadata Firefly Adds': 'Adobe Firefly Metadata: C2PA Content Credentials Explained',
    'Meta AI Images: "Imagined with AI" Labels, Watermarks and Metadata': 'Meta AI Images: Imagined With AI Labels and Metadata Guide',
    'Stable Diffusion PNG Metadata: Prompts and Parameters in Your Images': 'Stable Diffusion PNG Metadata: Prompts & Parameters Guide',
    'Bing Image Creator and Microsoft Designer: Content Credentials Explained': 'Bing Image Creator & Designer: C2PA Metadata Explained',
    'Higgsfield AI Video Metadata & Watermarks: What You Need to Know': 'Higgsfield AI Video Metadata & Watermarks Explained',
    'Seedance 2.0, 2.1 & 2.2 Video Metadata & Watermarks Explained': 'Seedance 2.0, 2.1 & 2.2 Video Metadata & Watermarks Guide'
}

for old_t, new_t in title_fixes.items():
    code = code.replace(old_t, new_t)

def pad_or_trim(desc: str) -> str:
    desc = desc.strip()
    if 150 <= len(desc) <= 160:
        return desc
    if len(desc) < 150:
        fillers = [
            ' Free client-side tool with zero server uploads.',
            ' 100% free tool with zero server uploads.',
            ' 100% private tool, zero server uploads.',
            ' Free tool with zero uploads.',
            ' Free in-browser tool.',
            ' Zero uploads.'
        ]
        for f in fillers:
            cand = desc + f
            if 150 <= len(cand) <= 160:
                return cand
        # crafted
        cand = desc.rstrip('.') + '. Clean files losslessly in-browser with zero uploads.'
        if len(cand) > 160:
            cand = cand[:157].rsplit(' ', 1)[0] + '...'
        while len(cand) < 150:
            cand = cand.rstrip('.') + ' Free tool.'
        if len(cand) > 160:
            cand = cand[:160]
        return cand
    else:
        # > 160
        cand = desc[:157]
        last_sp = cand.rfind(' ')
        if last_sp > 140:
            return cand[:last_sp] + '...'
        return cand + '...'

# Replace descriptions in explainers.ts
def desc_replacer(match):
    prefix = match.group(1)
    desc = match.group(2)
    new_desc = pad_or_trim(desc)
    return f"{prefix}'{new_desc}'"

code = re.sub(r"(description:\s*)\n?\s*['\"]([^'\"]+)['\"]", desc_replacer, code)

with open('packages/shared/src/data/explainers.ts', 'w', encoding='utf-8') as f:
    f.write(code)

print("explainers.ts updated successfully!")
