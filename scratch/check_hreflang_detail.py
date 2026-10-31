import urllib.request
import re

url = "http://localhost:4321/ja/"
html = urllib.request.urlopen(url).read().decode('utf-8')

print("--- HEAD HREFLANG TAGS FOR /ja/ ---")
tags = re.findall(r'<link\s+rel="alternate"[^>]+>', html)
for t in tags:
    print(t)
print(f"Total alternate links: {len(tags)}")
