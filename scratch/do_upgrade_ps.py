import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/photoshop-metadata-cleaner.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

more_sections = """
    <h2>Lightroom Document History vs Photoshop XMP Ancestors: Key Architectural Differences</h2>
    <p>
      While both Adobe Photoshop and Adobe Lightroom Classic write metadata into exported files, they record distinct categories of operational data that impact file size and confidentiality in different ways:
    </p>
    <ul>
      <li><strong>Photoshop DocumentAncestors:</strong> Exclusively an array of historical document IDs (<code>photoshop:DocumentAncestors</code>). Its primary downside is sheer file bloat. Because it consists of hundreds of thousands of GUID strings, it causes massive storage waste without offering any utility to end users or web visitors.</li>
      <li><strong>Lightroom Edit History (xmpMM:History):</strong> A chronological audit trail recording every export, edit step, module switch, and virtual copy creation. Each history event includes exact timestamps, software version strings, and sub-second action descriptors.</li>
      <li><strong>Lightroom Tone Recipes (crs:):</strong> Unlike Photoshop, which bakes layer adjustments directly into pixel data, Lightroom retains non-destructive parametric adjustment instructions in <code>crs:</code> blocks. If these blocks remain embedded in public JPEGs, any third party can inspect your exact post-processing formula.</li>
      <li><strong>The Combined Cleaning Solution:</strong> RemoveSynth addresses both problems simultaneously. It purges the massive DocumentAncestors array to reduce file sizes by up to 98 percent, while also stripping Lightroom history and camera raw tone parameters to protect client confidentiality.</li>
    </ul>

    <h2>Protecting Commercial Privacy: Why Agency Exports Must Be Sanitized Before Client Delivery</h2>
    <p>
      In commercial photography, corporate design, and freelance creative work, delivering uncleaned Photoshop files poses significant legal and competitive risks:
    </p>
    <ul>
      <li><strong>Preventing Competitive Reverse-Engineering:</strong> High-end retouching studios and creative directors invest years developing signature color grading styles. Delivering files containing unstripped Camera Raw presets enables competitors to copy your aesthetic with a single click.</li>
      <li><strong>Preventing Internal Workflow Leaks:</strong> Document ancestor UUIDs and history logs frequently contain internal client codenames, server share paths, employee usernames, and previous revision dates that should never be visible to clients or the public.</li>
      <li><strong>Accelerating Web Page Performance:</strong> When delivering image assets for web development, clean files load instantly. Eliminating 15 MB of metadata bloat from a product hero image can mean the difference between a sub-second page load and an abandoned shopping cart.</li>
      <li><strong>Ensuring CMS and Social Media Upload Success:</strong> Leading platforms like WordPress, Shopify, and Webflow automatically accept sanitized images without running out of memory or throwing unexplained upload errors.</li>
    </ul>
"""

if '<h2>Lightroom Document History vs' not in orig:
    target = '<h2>Why RemoveSynth Outperforms'
    orig = orig.replace(target, more_sections + '\n\n    ' + target)

with open('apps/removesynth/src/pages/photoshop-metadata-cleaner.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'photoshop-metadata-cleaner body word count: {words}')
