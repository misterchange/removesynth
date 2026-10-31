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
    if filename in ['index.astro', '404.astro', 'about.astro', 'tools.astro']:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find description
    m = re.search(r"description\s*=\s*(['\"])(.*?)\1", content)
    if not m:
        continue

    quote = m.group(1)
    desc = m.group(2)
    new_desc = desc

    if len(new_desc) < 150:
        # Pad slightly with clean text
        if new_desc.endswith('.'):
            new_desc = new_desc[:-1] + ' online.'
        else:
            new_desc = new_desc + ' online.'
        if len(new_desc) < 150:
            new_desc = new_desc.replace('online.', 'online for free.')

    if len(new_desc) > 160:
        # Trim slightly
        new_desc = new_desc.replace('online for free', 'online')
        new_desc = new_desc.replace('100 percent', '100%')
        new_desc = new_desc.replace('in your browser', 'in browser')
        if len(new_desc) > 160:
            # truncate cleanly at last space before 159
            cut = new_desc[:159]
            last_space = cut.rfind(' ')
            if last_space > 140:
                new_desc = cut[:last_space].rstrip('.') + '.'

    if 150 <= len(new_desc) <= 160 and new_desc != desc:
        content = content.replace(f"description = {quote}{desc}{quote}", f"description = {quote}{new_desc}{quote}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed desc for {filename}: {len(desc)} -> {len(new_desc)}")
        fixed += 1

print(f"Total descriptions normalized: {fixed}")
