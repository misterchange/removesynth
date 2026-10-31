import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    with urllib.request.urlopen('http://localhost:4322/avif-to-jpg/') as response:
        html = response.read().decode('utf-8')
        print(f"HTTP Status: 200, length: {len(html)}")
        title = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
        print("Title:", title.group(1).strip() if title else "No title")
        desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
        if desc:
            print(f"Desc ({len(desc.group(1))} chars): {desc.group(1)}")
        else:
            print("No desc")
        
        # Check text words
        text = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<svg.*?</svg>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<[^>]+>', ' ', text)
        words = text.split()
        print(f"Total visible text words: {len(words)}")
        
        h2s = re.findall(r'<h2.*?>(.*?)</h2>', html, re.DOTALL | re.IGNORECASE)
        print(f"H2 count: {len(h2s)}")
        for i, h in enumerate(h2s):
            clean_h = re.sub(r'<[^>]+>', '', h).strip()
            print(f"  H2 {i+1}: {clean_h}")
except Exception as e:
    print("Error:", e)
