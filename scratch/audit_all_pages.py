import os, glob, re

pages_dir = 'apps/removesynth/src/pages'
astro_files = sorted(glob.glob(os.path.join(pages_dir, '*.astro')))

print(f"Total .astro pages: {len(astro_files)}")
print("-" * 75)
print(f"{'Page Name':<35} | {'Words':<6} | {'Math':<5} | {'Examp':<5} | {'SVG':<5} | {'FAQ':<5}")
print("-" * 75)

for f in astro_files:
    basename = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    # Strip script and frontmatter for word count
    clean = re.sub(r'---.*?---', '', content, flags=re.DOTALL)
    clean = re.sub(r'<script.*?</script>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    words = len(clean.split())
    
    has_math = 'math-block' in content or 'Mathematical Formulation' in content
    has_example = 'Worked Example' in content or 'worked-example' in content
    has_svg = '<svg' in content and 'viewBox' in content
    has_faq = 'faqSchema' in content or 'faq-item' in content or 'Frequently Asked Questions' in content
    
    print(f"{basename:<35} | {words:<6} | {str(has_math):<5} | {str(has_example):<5} | {str(has_svg):<5} | {str(has_faq):<5}")
