import os
import re
import glob
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

pages_dir = 'apps/removesynth/src/pages'
astro_files = sorted([f for f in glob.glob(os.path.join(pages_dir, '*.astro')) if not os.path.basename(f).startswith('[')])

print(f"Total top-level Astro pages: {len(astro_files)}")

results = []

for filepath in astro_files:
    filename = os.path.basename(filepath)
    if filename in ['index.astro', '404.astro', 'about.astro', 'tools.astro']:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    fm = fm_match.group(1) if fm_match else ""
    
    title_match = re.search(r"title\s*=\s*['\"]([^'\"]+)['\"]", fm)
    title = title_match.group(1) if title_match else ""
    
    desc_match = re.search(r"description\s*=\s*['\"]([^'\"]+)['\"]", fm)
    desc = desc_match.group(1) if desc_match else ""
    
    # Body text
    body = re.sub(r'^---\s*\n.*?\n---', '', content, flags=re.DOTALL)
    body_no_script = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', body, flags=re.IGNORECASE)
    body_no_style = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', body_no_script, flags=re.IGNORECASE)
    body_no_svg = re.sub(r'<svg\b[^<]*(?:(?!<\/svg>)<[^<]*)*<\/svg>', '', body_no_style, flags=re.IGNORECASE)
    body_text = re.sub(r'<[^>]+>', ' ', body_no_svg)
    words = body_text.split()
    word_count = len(words)
    
    h2s = re.findall(r'<h2[^>]*>(.*?)<\/h2>', body, re.IGNORECASE | re.DOTALL)
    
    has_math = 'math-block' in body or '$$' in body or 'matrix' in body
    has_worked = 'worked-example' in body or 'Worked Example' in body or 'Concrete' in body or 'Numerical' in body
    has_svg = '<svg' in body
    
    results.append({
        'file': filename,
        'words': word_count,
        'h2_count': len(h2s),
        'title_len': len(title),
        'desc_len': len(desc),
        'has_math': has_math,
        'has_worked': has_worked,
        'has_svg': has_svg,
    })

out_lines = []
out_lines.append(f"{'File':<35} | {'Words':<6} | {'H2s':<4} | {'T_len':<5} | {'D_len':<5} | {'Math':<5} | {'Work':<5} | {'SVG':<4}")
out_lines.append("-" * 80)
under_1500 = []
for r in results:
    status = "OK" if r['words'] >= 1500 else "LOW"
    if r['words'] < 1500:
        under_1500.append(r)
    out_lines.append(f"{r['file']:<35} | {r['words']:<6} | {r['h2_count']:<4} | {r['title_len']:<5} | {r['desc_len']:<5} | {str(r['has_math']):<5} | {str(r['has_worked']):<5} | {str(r['has_svg']):<4} {status if status == 'LOW' else ''}")

out_lines.append(f"\nTotal under 1,500 words: {len(under_1500)}")
for u in under_1500:
    out_lines.append(f"  -> {u['file']}: {u['words']} words")

output_str = "\n".join(out_lines)
with open('scratch/page_words_result.txt', 'w', encoding='utf-8') as f:
    f.write(output_str)

print(output_str)
