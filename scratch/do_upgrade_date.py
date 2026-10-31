import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/change-photo-date.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

legal_date_section = """
      <h2>Forensic Timestamps in Legal Evidence: Chain of Custody and Tamper Verification</h2>
      <p>
        In civil litigation, criminal proceedings, and insurance claim verifications, digital photo timestamps are routinely scrutinized during electronic discovery (e-discovery):
      </p>
      <ul>
        <li><strong>Chain of Custody and Spoliation:</strong> Submitting photos in court with modified or mismatched EXIF dates can trigger spoliation motions or evidentiary disqualification if not properly documented.</li>
        <li><strong>Internal Inconsistencies:</strong> Digital cameras write redundant timestamp records across multiple sub-directories: <code>ExifIFD:DateTimeOriginal</code>, <code>InteropIFD</code>, and manufacturer MakerNotes. Naive date editors that alter only the primary tag leave contradictory records that forensic tools immediately flag as manipulated.</li>
        <li><strong>The Privacy Strip Option:</strong> For private individuals sharing photos with journalists, regulatory bodies, or public forums, utilizing our &quot;Strip All Timestamps&quot; mode completely zeroes all timestamp tags uniformly, eliminating temporal correlation vectors without introducing suspicious date contradictions.</li>
      </ul>
"""

if '<h2>Forensic Timestamps in Legal Evidence:' not in orig:
    target = '<h2>Frequently Asked Questions</h2>'
    orig = orig.replace(target, legal_date_section + '\n\n      ' + target)

with open('apps/removesynth/src/pages/change-photo-date.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'change-photo-date body word count: {words}')
