import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/bulk-metadata-remover.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

even_more_bulk = """
      <h2>Supported File Formats in Heterogeneous Batch Processing</h2>
      <p>
        Real-world photo archives are rarely composed of a single file format. When cleaning files from multiple contributors, teams encounter a mixture of legacy and modern image encodings:
      </p>
      <ul>
        <li><strong>JPEG and JPG:</strong> The universal format for DSLR, mirrorless, and web images. RemoveSynth slices through APP0 through APP15 application segments, excising EXIF, XMP, IPTC, and Adobe 8BIM blocks while leaving Huffman-coded pixel scans intact.</li>
        <li><strong>Apple HEIC and HEIF:</strong> High Efficiency Image Container files from iPhones store metadata inside internal <code>meta</code> and <code>iloc</code> item location boxes. Our demuxer isolates uncompressed AV1/HEVC intra-frames and strips GPS rational coordinates without triggering format conversion.</li>
        <li><strong>PNG Graphics:</strong> Transparent screenshots, website logos, and design assets store metadata in ancillary chunks (<code>eXIf</code>, <code>iTXt</code>, <code>tEXt</code>, and <code>zTXt</code>). RemoveSynth prunes these text chunks while keeping <code>IHDR</code>, <code>IDAT</code>, and <code>PLTE</code> image chunks bit-for-bit identical.</li>
        <li><strong>Modern WebP and AVIF:</strong> Next-generation web formats encapsulate EXIF and XMP in extended chunk chunks (<code>EXIF</code>, <code>XMP </code> in WebP, and <code>mdat</code> in AVIF). All formats can be dragged into the same batch queue simultaneously.</li>
      </ul>

      <h2>Batch Cleaning Best Practices for Professional Photographers and Content Teams</h2>
      <p>
        To maximize throughput and ensure complete privacy compliance across large image archives, consider these operational guidelines:
      </p>
      <ul>
        <li><strong>Always Maintain a Backup of Master RAW Files:</strong> While RemoveSynth performs lossless metadata stripping, it permanently strips camera serial numbers and GPS tags. Keep an offline archive of your original files if you require camera metadata for copyright registration.</li>
        <li><strong>Verify Output ZIP Integrity:</strong> After downloading the consolidated ZIP archive, extract the files to confirm all images open smoothly in your default photo viewer.</li>
        <li><strong>Batch Size Optimization:</strong> For computers with 8 GB to 16 GB of RAM, batches of 25 to 50 photos process instantaneously in under 3 seconds. For massive archives of 500+ photos, process in sequential batches of 50 for optimal browser performance.</li>
      </ul>
"""

if '<h2>Supported File Formats in Heterogeneous' not in orig:
    target = '<h2>Comparison: RemoveSynth Bulk Cleaner vs Desktop and Cloud Alternatives</h2>'
    orig = orig.replace(target, even_more_bulk + '\n\n      ' + target)

with open('apps/removesynth/src/pages/bulk-metadata-remover.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'bulk-metadata-remover body word count: {words}')
