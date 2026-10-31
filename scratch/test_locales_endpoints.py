import urllib.request
import re

TEST_LOCALES = [
    'en', 'es', 'de', 'fr', 'pt-br', 'ja', 'tr', 'tl',
    'zh', 'zh-tw', 'ko', 'th', 'vi', 'id',
    'pt', 'it', 'nl', 'pl', 'cs', 'hu', 'ro', 'uk', 'el', 'sv', 'no', 'da', 'fi',
    'hi', 'bn',
    'ar', 'he', 'sw'
]

print(f"Testing all {len(TEST_LOCALES)} locale endpoints on http://localhost:4321 ...\n")
all_passed = True

for loc in TEST_LOCALES:
    url = f"http://localhost:4321/{'' if loc == 'en' else loc + '/'}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            code = resp.getcode()
            html = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>(.*?)</title>', html)
            title = title_m.group(1).encode('ascii', 'replace').decode('ascii') if title_m else 'No title'
            html_lang_m = re.search(r'<html\s+([^>]+)>', html)
            html_tag = html_lang_m.group(1) if html_lang_m else 'No html tag'
            hreflangs = re.findall(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"', html)
            h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', html)
            h1 = h1_m.group(1).encode('ascii', 'replace').decode('ascii')[:30] if h1_m else ''
            print(f"[{code}] {loc.upper():<6} -> {url:<30} | {html_tag:<22} | Hreflang: {len(hreflangs)} | Title: {title[:35]}...")
            if code != 200 or len(hreflangs) < 32:
                all_passed = False
    except Exception as e:
        print(f"[FAIL] {loc}: {url} -> {e}")
        all_passed = False

print(f"\nALL 32 ENDPOINTS TEST PASSED: {all_passed}")
