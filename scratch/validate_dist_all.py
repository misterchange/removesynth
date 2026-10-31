import os
import re
import json

dist_dir = r'd:\Nitin\removesynth\apps\removesynth\dist'

sample_slugs = [
    'remove-synthid-from-images',
    'remove-synthid-from-video',
    'remove-synthid-from-audio',
    'remove-synthid-from-text',
    'photo-metadata-remover',
    'video-metadata-remover',
    'remove-ai-info-label',
    'remove-gemini-watermark',
    'jpg-to-pdf',
    'heic-to-jpg',
    'social-media-safe-zones',
    'exif-viewer',
    'dola-ai',
    'higgsfield',
    'pika-ai',
    'runway-ai',
    'sora-ai',
    'veo-ai',
    'wan-ai',
]

results = []

for slug in sample_slugs:
    html_path = os.path.join(dist_dir, slug, 'index.html')
    if not os.path.exists(html_path):
        results.append({'slug': slug, 'error': 'FILE_NOT_FOUND'})
        continue
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Title
    t_match = re.search(r'<title>(.*?)</title>', html)
    title = t_match.group(1) if t_match else ''

    # Meta desc
    d_match = re.search(r'<meta name="description" content="(.*?)"', html)
    desc = d_match.group(1) if d_match else ''

    # Em/en dashes
    dashes = len(re.findall(r'[—–]', html))

    # Emojis
    emojis = len(re.findall(r'[\U0001F300-\U0001FAFF]', html))

    # JSON-LD
    scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    json_ld_ok = False
    graph_nodes = 0
    if len(scripts) == 1:
        try:
            data = json.loads(scripts[0])
            if '@graph' in data:
                json_ld_ok = True
                graph_nodes = len(data['@graph'])
        except Exception as e:
            json_ld_ok = False

    results.append({
        'slug': slug,
        'title_len': len(title),
        'desc_len': len(desc),
        'title': title,
        'dashes': dashes,
        'emojis': emojis,
        'json_ld_blocks': len(scripts),
        'json_ld_ok': json_ld_ok,
        'graph_nodes': graph_nodes
    })

import pandas as pd
df = pd.DataFrame(results)
print(df.to_string())
