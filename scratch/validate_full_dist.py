import glob, os, re
from bs4 import BeautifulSoup

EMOJI_PATTERN = re.compile(
    r"[\U00010000-\U0010ffff\u2600-\u26FF\u2700-\u27BF\u2300-\u23FF\u2B50\u200D\uFE0F]"
)
DASH_PATTERN = re.compile(r"[\u2014\u2013]") # em-dash and en-dash

dist_dir = 'apps/removesynth/dist'
html_files = glob.glob(os.path.join(dist_dir, '**', '*.html'), recursive=True)
print(f"Total built HTML files in dist: {len(html_files)}")

emoji_violations = []
dash_violations = []
multi_schema = []
title_violations = []
desc_violations = []

# Target pages to check strictly
for f in html_files:
    rel = os.path.relpath(f, dist_dir).replace('\\', '/')
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    
    # 1. Emoji check
    if EMOJI_PATTERN.search(html):
        emoji_violations.append(rel)
    
    # 2. Dash check
    if DASH_PATTERN.search(html):
        dash_violations.append(rel)
    
    # 3. Schema tag check
    schema_tags = re.findall(r'<script\s+type=[\"\']application/ld\+json[\"\']', html, re.I)
    if len(schema_tags) > 1:
        multi_schema.append((rel, len(schema_tags)))
    
    # Check title and meta description
    soup = BeautifulSoup(html, 'html.parser')
    title_el = soup.find('title')
    title = title_el.text.strip() if title_el else ''
    if len(title) > 60:
        title_violations.append((rel, len(title), title))
        
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    desc = meta_desc['content'].strip() if meta_desc and meta_desc.get('content') else ''
    # Only enforce 150-160 on pages where description is provided and not generic hub
    if desc and (len(desc) < 140 or len(desc) > 165):
        desc_violations.append((rel, len(desc), desc))

print(f"\n--- Validation Results ---")
print(f"Emoji Violations: {len(emoji_violations)}")
if emoji_violations:
    print(emoji_violations[:5])

print(f"Dash Violations (em/en dashes): {len(dash_violations)}")
if dash_violations:
    print(dash_violations[:5])

print(f"Multiple Schema Blocks: {len(multi_schema)}")
if multi_schema:
    print(multi_schema[:5])

print(f"Title > 60 chars Violations: {len(title_violations)}")
if title_violations:
    for v in title_violations[:5]:
        print(f"  {v[0]}: {v[1]} chars ('{v[2]}')")

print(f"Description Violations (outside 140-165): {len(desc_violations)}")
if desc_violations:
    for v in desc_violations[:5]:
        print(f"  {v[0]}: {v[1]} chars ('{v[2]}')")

print("\nValidation complete!")
