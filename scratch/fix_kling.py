import os, re
path = r'd:\Nitin\removesynth\apps\removesynth\src\pages\kling-ai.astro'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()
desc = 'Remove Kling AI 1.0, 1.5, and 2.0 video watermarks, C2PA manifests, and camera metadata tags. Free in-browser MP4 cleaner with zero re-encoding quality loss.'
print('kling-ai len:', len(desc))
c = re.sub(r"const description\s*=\s*['\"`].*?['\"`];", f"const description =\n  '{desc}';", c, flags=re.DOTALL)
with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated kling-ai!')
