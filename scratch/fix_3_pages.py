import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. video-metadata-remover.astro
with open('apps/removesynth/src/pages/video-metadata-remover.astro', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<h2>Frequently Asked Questions About Video Metadata</h2>'
sec = """
    <h2>Understanding QuickTime and MP4 Atom Box Trees (moov, mvhd, trak)</h2>
    <p>
      ISO Base Media File Format containers structure media as hierarchical atom boxes (ISOBMFF, ISO/IEC 14496-12):
    </p>
    <ul>
      <li><strong>The moov Atom:</strong> Contains the master movie header (<code>mvhd</code>) and track headers (<code>tkhd</code>) describing video resolution, frame rates, and sample timing.</li>
      <li><strong>The udta (User Data) Atom:</strong> Houses human-readable metadata, including camera serial numbers, GPS coordinates, editing software tags, and chapter markers.</li>
      <li><strong>FastStart Web Optimization:</strong> When stripping metadata, RemoveSynth relocates the <code>moov</code> atom to the beginning of the file (before the <code>mdat</code> video payload), enabling immediate streaming playback without waiting for the full file to download.</li>
    </ul>
"""
if target in c and '<h2>Understanding QuickTime' not in c:
    c = c.replace(target, sec + '\n\n    ' + target)
    with open('apps/removesynth/src/pages/video-metadata-remover.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Enriched video-metadata-remover.astro")

# 2. remove-synthid-from-text.astro
with open('apps/removesynth/src/pages/remove-synthid-from-text.astro', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<h2>Frequently Asked Questions About SynthID Text</h2>'
sec = """
    <h2>Understanding Token Selection Perturbation and Watermark Detectability</h2>
    <p>
      Statistical AI text watermarking relies on biasing the token selection process during language model autoregressive generation:
    </p>
    <ul>
      <li><strong>Green and Red Token Partitions:</strong> The watermarking algorithm hashes the previous token to pseudo-randomly partition the model vocabulary into &quot;green&quot; (favored) and &quot;red&quot; (penalized) word lists, nudging the model to select green tokens.</li>
      <li><strong>Detecting the Bias:</strong> A statistical detector counts the proportion of green tokens in a text passage. Human writing exhibits an equal balance, while watermarked AI text shows a statistically improbable excess of green tokens (z-score > 4.0).</li>
      <li><strong>Neutralizing the Pattern:</strong> Restructuring sentences and replacing predictable synonym sequences disrupts the artificial token balance, restoring natural human statistical variance.</li>
    </ul>
"""
if target in c and '<h2>Understanding Token Selection' not in c:
    c = c.replace(target, sec + '\n\n    ' + target)
    with open('apps/removesynth/src/pages/remove-synthid-from-text.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Enriched remove-synthid-from-text.astro")

# 3. remove-gemini-watermark.astro
with open('apps/removesynth/src/pages/remove-gemini-watermark.astro', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<h2>Frequently Asked Questions About Gemini Watermarks</h2>'
sec = """
    <h2>Imagen 3 Wavelet Watermarking vs Traditional Visual Overlays</h2>
    <p>
      Unlike visible logo watermarks that occupy surface pixels, SynthID operates deep within image frequency transformations:
    </p>
    <ul>
      <li><strong>Multi-Scale Wavelet Decomposition:</strong> Modifies subtle coefficients across low, medium, and high spatial frequency sub-bands.</li>
      <li><strong>Resilience to Compression:</strong> Withstands standard JPEG compression, scaling, and contrast adjustments.</li>
      <li><strong>Neutralization Strategy:</strong> RemoveSynth applies anti-correlation smoothing across targeted wavelet sub-bands, breaking detector confidence while preserving crisp photorealistic textures.</li>
    </ul>
"""
if target in c and '<h2>Imagen 3 Wavelet Watermarking' not in c:
    c = c.replace(target, sec + '\n\n    ' + target)
    with open('apps/removesynth/src/pages/remove-gemini-watermark.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Enriched remove-gemini-watermark.astro")
