import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/docx-metadata-remover.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

even_more_docx = """
      <h2>Forensic Audit Checklist: 8 Data Points You Must Verify Before Emailing Confidential Documents</h2>
      <p>
        Prior to transmitting Word documents to prospective employers, legal adversaries, journalists, or external clients, review this comprehensive forensic audit checklist:
      </p>
      <ul>
        <li><strong>1. Dublin Core Author Identity (dc:creator):</strong> Verify that the initial creator name is not set to your full name, personal email address, or an internal administrative assistant.</li>
        <li><strong>2. Last Modified By (cp:lastModifiedBy):</strong> Ensure the last-saved username does not expose internal collaborators, contractors, or executive ghostwriters.</li>
        <li><strong>3. Cumulative Revision Counter (cp:revision):</strong> Check that the revision number is reset to 1 rather than exhibiting hundreds of prior internal drafts.</li>
        <li><strong>4. Cumulative Active Editing Time (TotalTime):</strong> Confirm that the editing duration does not contradict billing agreements or reveal rushed template adaptation.</li>
        <li><strong>5. Local and Network Template Paths:</strong> Ensure the <code>Template</code> XML attribute does not expose internal network file paths, server shares, or private file directory trees.</li>
        <li><strong>6. Registered Company Name:</strong> Strip corporate enterprise registration strings that reveal affiliated corporate entities or holding companies.</li>
        <li><strong>7. Hidden XML Custom Properties:</strong> Inspect and purge <code>docProps/custom.xml</code> to delete internal matter numbers, client codes, and billing tags.</li>
        <li><strong>8. Embedded Binary Objects and Screenshots:</strong> Remove temporary EXIF or metadata headers from images pasted directly into document pages.</li>
      </ul>

      <h2>Why Cloud-Based Document Cleaners Create Extreme Legal and Security Liabilities</h2>
      <p>
        Many online utilities advertise free document metadata removal, but require users to upload their <code>.docx</code>, <code>.xlsx</code>, or <code>.pdf</code> files to remote cloud servers. For corporate professionals, this practice introduces severe regulatory and ethical risks:
      </p>
      <ul>
        <li><strong>Breach of Non-Disclosure Agreements (NDAs):</strong> Uploading unreleased product roadmaps, merger contracts, or confidential settlement terms to a third-party website directly breaches contractual confidentiality obligations.</li>
        <li><strong>GDPR and HIPAA Violations:</strong> Transmitting medical records, patient intake summaries, or employee personnel files containing personally identifiable information (PII) to unvetted cloud servers violates European GDPR and United States HIPAA privacy mandates.</li>
        <li><strong>Retention and Data Scraping Hazards:</strong> Free cloud conversion websites frequently monetize by logging user submissions or archiving documents on unsecured temporary buckets where they risk indexation or data breaches.</li>
        <li><strong>The In-Browser Zero-Upload Guarantee:</strong> RemoveSynth operates under a zero-knowledge architecture. Every byte of the OpenXML archive is decompressed, parsed, sanitized, and re-compressed directly inside your web browser execution thread. Not a single character or metadata tag is ever transmitted over the network.</li>
      </ul>
"""

if '<h2>Forensic Audit Checklist:' not in orig:
    target = '<h2>Comparison: RemoveSynth vs Microsoft Document Inspector</h2>'
    orig = orig.replace(target, even_more_docx + '\n\n      ' + target)

with open('apps/removesynth/src/pages/docx-metadata-remover.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'docx-metadata-remover body word count: {words}')
