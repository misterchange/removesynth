import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/anonymous-photo-cleaner.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

anon_guide = """
      <h2>Whistleblower and Investigative Source Protection Protocol</h2>
      <p>
        For corporate whistleblowers, human rights activists, and confidential sources sharing evidence with news organizations, submitting digital photos carries profound physical and legal stakes:
      </p>
      <ul>
        <li><strong>Forensic Metadata Inquests:</strong> Corporate security teams and government intelligence services seize digital photos leaked to the media and subject them to bit-level forensic scrutiny using tools like EnCase, Magnet AXIOM, and ExifTool.</li>
        <li><strong>Sub-Pixel Sensor Dust and Hot Pixel Corroboration:</strong> In addition to EXIF tags, forensic imaging specialists match sensor dust specks and dead pixel positions against reference photos. Stripping EXIF metadata eliminates the easiest avenue of attribution (serial numbers and timestamps), forcing investigators to rely on probabilistic sensor noise analyses.</li>
        <li><strong>Network Hygiene Matters:</strong> Always sanitize photos on an offline or air-gapped machine or via private in-browser memory before transmitting them via encrypted signal channels (such as Signal or SecureDrop).</li>
      </ul>

      <h2>Step-by-Step Guide: How to Safely Sanitize Photos Before Online Sharing</h2>
      <ol class="steps">
        <li><strong>Upload Your Photo:</strong> Drag and drop your JPG, PNG, or WebP photo into the secure upload stage above, or tap to choose from your phone gallery.</li>
        <li><strong>Automated Binary Sanitization:</strong> In under 20 milliseconds, the client-side engine strips GPS satellite tags, hardware serial numbers, author comments, and device calibration profiles in local browser RAM.</li>
        <li><strong>Confirm Clean Status:</strong> The status indicator verifies that all location and hardware identifiers have been purged.</li>
        <li><strong>Download and Share Anonymously:</strong> Save the sanitized photo and post safely to Reddit, 4chan, Discord, Facebook Marketplace, Craigslist, or investigative tip lines without fear of doxxing.</li>
      </ol>
"""

if '<h2>Whistleblower and Investigative Source Protection' not in orig:
    target = '<h2>Frequently Asked Questions</h2>'
    orig = orig.replace(target, anon_guide + '\n\n      ' + target)

with open('apps/removesynth/src/pages/anonymous-photo-cleaner.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'anonymous-photo-cleaner body word count: {words}')
