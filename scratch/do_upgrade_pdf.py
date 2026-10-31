import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/pdf-resume-metadata-remover.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

step_guide = """
    <h2>Step-by-Step Guide: How to Anonymize a PDF Resume on Windows, Mac, iPhone, and Android</h2>
    <p>
      Sanitizing your resume with RemoveSynth takes less than 30 seconds and requires no software installation or registration:
    </p>
    <ol class="steps">
      <li><strong>Select Your PDF Resume:</strong> Drag your PDF file from your desktop file manager into the upload zone above, or tap the box on your smartphone to select from the Apple Files app or Android Downloads folder.</li>
      <li><strong>Automated ISO 32000-1 In-Browser Parsing:</strong> The tool instantly scans the PDF cross-reference table, decouples the <code>/Info</code> dictionary, nullifies author, creator, and producer entries, and excises historical XMP metadata streams directly inside client memory.</li>
      <li><strong>Inspect and Verify Clean Properties:</strong> The live preview displays all detected metadata tags alongside their sanitized states, confirming zero remaining personal identifiers.</li>
      <li><strong>Download Your ATS-Ready Resume:</strong> Click the download button to save your clean, anonymized PDF. Submit with complete confidence to job portals, corporate recruiters, and executive search firms.</li>
    </ol>
"""

if '<h2>Step-by-Step Guide: How to Anonymize' not in orig:
    target = '<h2>Frequently Asked Questions</h2>'
    orig = orig.replace(target, step_guide + '\n\n    ' + target)

with open('apps/removesynth/src/pages/pdf-resume-metadata-remover.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'pdf-resume-metadata-remover body word count: {words}')
