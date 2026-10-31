import os
import re

pages_dir = r'd:\Nitin\removesynth\apps\removesynth\src\pages'

fname = 'exif-editor.astro'
desc = 'Modify, add, or delete individual EXIF tags in your photos. Edit artist, copyright, camera model, lens, and capture dates with private in-browser download.'
print(fname, 'New Desc Len:', len(desc))

path = os.path.join(pages_dir, fname)
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r"const description\s*=\s*['\"`].*?['\"`];", f"const description =\n  '{desc}';", content, flags=re.DOTALL)
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Adjusted successfully!')
