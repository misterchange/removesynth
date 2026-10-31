import os
import re
import glob
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

pages_dir = 'apps/removesynth/src/pages'
astro_files = sorted([f for f in glob.glob(os.path.join(pages_dir, '*.astro')) if not os.path.basename(f).startswith('[')])

fixed = 0

for filepath in astro_files:
    filename = os.path.basename(filepath)
    if filename in ['index.astro', '404.astro', 'about.astro', 'tools.astro', 'compress-image-to-[size].astro']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match description across single or multiline
    m = re.search(r"description\s*=\s*(['\"])(.*?)\1;", content, re.DOTALL)
    if not m:
        m = re.search(r"description\s*=\s*\n?\s*(['\"])(.*?)\1;", content, re.DOTALL)
    if not m:
        continue

    raw_match = m.group(0)
    quote = m.group(1)
    desc = re.sub(r'\s+', ' ', m.group(2)).strip()
    
    new_desc = desc
    
    # Adjust length to strictly 150-160
    if len(new_desc) > 160:
        new_desc = new_desc.replace('online for free', 'online')
        new_desc = new_desc.replace('100 percent', '100%')
        new_desc = new_desc.replace('in your browser', 'in browser')
        new_desc = new_desc.replace('with zero cloud server uploads', 'with zero server uploads')
        new_desc = new_desc.replace('with zero server uploads', 'with no uploads')
        if len(new_desc) > 160:
            cut = new_desc[:159]
            last_space = cut.rfind(' ')
            if last_space > 140:
                new_desc = cut[:last_space].rstrip('.') + '.'
    
    if len(new_desc) < 150:
        if new_desc.endswith('.'):
            new_desc = new_desc[:-1] + ' online for free.'
        else:
            new_desc = new_desc + ' online for free.'
        if len(new_desc) < 150:
            diff = 153 - len(new_desc)
            new_desc = new_desc.replace('online for free.', 'online for free today.')
    
    # Ensure it's in 150-160
    if len(new_desc) > 160:
        new_desc = new_desc[:159].rsplit(' ', 1)[0] + '.'
    if len(new_desc) < 150:
        # pad precisely
        needed = 153 - len(new_desc)
        new_desc = new_desc.rstrip('.') + ' now.'

    if desc != new_desc or '\n' in m.group(0):
        replacement = f"description =\n  '{new_desc}';"
        content = content.replace(raw_match, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}: {len(desc)} -> {len(new_desc)} chars: {new_desc}")
        fixed += 1

print(f"\nTotal fixed: {fixed}")
