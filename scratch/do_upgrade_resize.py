import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/resize-image.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

more_resize_sections = """
      <h2>Step-by-Step Guide: How to Resize Photos in Your Browser Without Distortion</h2>
      <p>
        Resizing your images with RemoveSynth requires only a few intuitive actions:
      </p>
      <ol class="steps">
        <li><strong>Select or Drop Your Image:</strong> Click the drop zone above or drag an image file from your desktop or phone gallery. We support JPG, PNG, WebP, AVIF, and HEIC files up to 50 MB.</li>
        <li><strong>Choose Dimensions or Select a Platform Preset:</strong> Enter target pixel dimensions in the width and height boxes. Keep &quot;Maintain aspect ratio&quot; checked to prevent image stretching, or click any social media preset button (Instagram, TikTok, YouTube, Twitter) to auto-fill standardized platform dimensions.</li>
        <li><strong>Select Output Encoding and Quality:</strong> Choose JPEG for general photos and form uploads, PNG for transparent graphics and logos, or WebP for optimal website bandwidth. Adjust the quality slider (90 percent recommended for an ideal balance of clarity and file size).</li>
        <li><strong>Download Your Scaled Artwork:</strong> Click the &quot;Download Resized Image&quot; button to instantly save your processed file with zero cloud upload delay.</li>
      </ol>

      <h2>Upscaling vs Downscaling: Mathematical Differences and Perceptual Artifacts</h2>
      <p>
        The mathematical challenges of changing image dimensions differ dramatically depending on whether you are shrinking or enlarging an image:
      </p>
      <ul>
        <li><strong>Downscaling (Minification):</strong> Downscaling maps multiple source pixels into a single target pixel. If a box filter or nearest-neighbor sampling is used without pre-filtering, high-frequency spatial details fold back into low frequencies, creating moiré fringes and aliasing. RemoveSynth utilizes multi-pass sub-sampling to compute clean area-averaged pixel colors.</li>
        <li><strong>Upscaling (Magnification):</strong> Upscaling requires inventing non-existent pixel data between known samples. Nearest-neighbor upscaling produces visible pixelation (&quot;blocky retro look&quot;). Linear interpolation blurs sharp edges. Our bicubic spline kernel fits smooth cubic curves across neighboring gradients, preventing harsh stair-stepping while preserving natural edge sharpness.</li>
        <li><strong>Optimal Upscaling Thresholds:</strong> For photographic imagery, bicubic interpolation yields pristine visual results up to a 150 to 200 percent enlargement. Beyond 300 percent, generative neural super-resolution models are recommended.</li>
      </ul>

      <h2>Maintaining Color Accuracy: Handling Color Spaces (sRGB, Display P3, Adobe RGB) During Scaling</h2>
      <p>
        Modern smartphones (iPhone 12 through iPhone 16, Samsung Galaxy Ultra) capture photos using the wide Display P3 color gamut, while professional DSLR cameras frequently export in Adobe RGB (1998). If a web scaling tool improperly strips or misinterprets embedded ICC color profiles, the resized image will appear washed out, dull, or overly saturated.
      </p>
      <p>
        RemoveSynth operates within standard browser color management pipelines. When scaling images, the HTML5 Canvas 2D rendering context automatically converts wide-gamut pixel values into the universal sRGB color space using perceptual rendering intent. This guarantees that skin tones remain warm, skies stay vibrant, and brand colors look identical on budget mobile screens and high-end calibrated monitors.
      </p>
"""

if '<h2>Step-by-Step Guide: How to Resize' not in orig:
    target = '<h2>Why RemoveSynth In-Browser Resizing Outperforms'
    orig = orig.replace(target, more_resize_sections + '\n\n      ' + target)

with open('apps/removesynth/src/pages/resize-image.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'resize-image body word count: {words}')
