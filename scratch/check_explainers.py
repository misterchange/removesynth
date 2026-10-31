import re

with open('packages/shared/src/data/explainers.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for title and description
title_matches = re.findall(r"title:\s*['\"]([^'\"]+)['\"]", content)
desc_matches = re.findall(r"description:\s*['\"]([^'\"]+)['\"]", content)

print(f"Total titles found: {len(title_matches)}")
for t in title_matches:
    if len(t) > 60:
        print(f"  Long title ({len(t)}): {t}")

print(f"\nTotal descriptions found: {len(desc_matches)}")
for d in desc_matches:
    if len(d) < 145 or len(d) > 165:
        print(f"  Desc ({len(d)}): {d}")
