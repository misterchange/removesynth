import json
import re

path = 'apps/removesynth/dist/remove-synthid-from-images/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
print(f'Found {len(scripts)} JSON-LD blocks')
for i, s in enumerate(scripts):
    try:
        data = json.loads(s)
        print(f'Block {i}: Valid JSON. Keys: {list(data.keys())}')
        if '@graph' in data:
            print(f'  @graph has {len(data["@graph"])} nodes: {[n.get("@type") for n in data["@graph"]]}')
    except Exception as e:
        print(f'Block {i} ERROR:', e)

em_dashes = len(re.findall(r'[—–]', html))
print(f'Em/en dashes found in HTML: {em_dashes}')

title_match = re.search(r'<title>(.*?)</title>', html)
meta_desc_match = re.search(r'<meta name="description" content="(.*?)"', html)
print('Title:', title_match.group(1) if title_match else 'None')
print('Meta Desc:', meta_desc_match.group(1) if meta_desc_match else 'None')
if title_match:
    print('Title len:', len(title_match.group(1)))
if meta_desc_match:
    print('Meta desc len:', len(meta_desc_match.group(1)))
