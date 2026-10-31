import os
import glob
import re
from bs4 import BeautifulSoup

dist_dir = 'apps/removesynth/dist'
html_files = glob.glob(f'{dist_dir}/**/*.html', recursive=True)
print(f'Total HTML files in dist: {len(html_files)}')

emoji_pattern = re.compile(r'[\U00010000-\U0010ffff\u2600-\u26FF\u2700-\u27BF]')
dash_pattern = re.compile(r'[—–]')

violations = {
    'title_len': [],
    'desc_len': [],
    'emojis': [],
    'dashes': [],
    'jsonld_count': []
}

for path in html_files:
    rel_path = os.path.relpath(path, dist_dir)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # check emojis
    if emoji_pattern.search(content):
        violations['emojis'].append(rel_path)

    # check dashes
    if dash_pattern.search(content):
        violations['dashes'].append(rel_path)

    # parse with soup
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('title')
    title_text = title.text if title else ''
    if len(title_text) > 60:
        violations['title_len'].append((rel_path, len(title_text), title_text))

    meta_desc = soup.find('meta', attrs={'name': 'description'})
    desc_text = meta_desc['content'] if meta_desc and meta_desc.has_attr('content') else ''
    if desc_text and (len(desc_text) < 145 or len(desc_text) > 165):
        violations['desc_len'].append((rel_path, len(desc_text), desc_text))

    jsonld_tags = soup.find_all('script', type='application/ld+json')
    if len(jsonld_tags) != 1:
        violations['jsonld_count'].append((rel_path, len(jsonld_tags)))

print('=== AUDIT RESULTS ===')
print(f"Emojis found: {len(violations['emojis'])}")
if violations['emojis']:
    print('Sample emoji files:', violations['emojis'][:5])
print(f"Dashes found: {len(violations['dashes'])}")
if violations['dashes']:
    print('Sample dash files:', violations['dashes'][:5])
print(f"Titles > 60 chars: {len(violations['title_len'])}")
if violations['title_len']:
    print('Sample long titles:', violations['title_len'][:5])
print(f"Desc outside 145-165 chars: {len(violations['desc_len'])}")
if violations['desc_len']:
    print('Sample desc issues:', violations['desc_len'][:5])
print(f"JSON-LD count != 1: {len(violations['jsonld_count'])}")
if violations['jsonld_count']:
    print('Sample jsonld count issues:', violations['jsonld_count'][:5])
