import os
import glob
import re

patterns = ['apps/removesynth/src/**/*', 'packages/shared/src/**/*']
all_files = []
for p in patterns:
    all_files.extend(glob.glob(p, recursive=True))

dash_pattern = re.compile(r'[—–]')
# Extended emoji pattern
emoji_pattern = re.compile(r'[\U00010000-\U0010ffff\u2600-\u26FF\u2700-\u27BF\uFE0F\u200D\u2300-\u23FF\u2B50\u2B55\u2934\u2935\u25AA\u25AB\u25B6\u25C0\u25FB-\u25FE]')

dash_replaced = 0
emoji_replaced = 0
modified_files = []

for f in all_files:
    if os.path.isfile(f) and not f.endswith(('.png', '.jpg', '.webp', '.svg', '.woff2', '.ttf', '.ico')):
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                content = fp.read()
        except Exception:
            continue

        new_content = content
        d_matches = len(dash_pattern.findall(new_content))
        if d_matches > 0:
            new_content = dash_pattern.sub('-', new_content)
            dash_replaced += d_matches

        e_matches = len(emoji_pattern.findall(new_content))
        if e_matches > 0:
            new_content = emoji_pattern.sub('', new_content)
            emoji_replaced += e_matches

        if new_content != content:
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(new_content)
            modified_files.append((f, d_matches, e_matches))

print(f"Total files modified: {len(modified_files)}")
print(f"Total dashes replaced with '-': {dash_replaced}")
print(f"Total emojis removed: {emoji_replaced}")
for f, dm, em in modified_files[:25]:
    print(f"  {f} (dashes: {dm}, emojis: {em})")
