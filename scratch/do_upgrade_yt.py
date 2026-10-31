import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/youtube-thumbnail-resizer.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

more_yt_sections = """
    <h2>High Click-Through Rate (CTR) Design Principles: Contrast, Human Faces, and Text Size</h2>
    <p>
      Achieving a competitive click-through rate on YouTube (consistently above 6 to 10 percent) requires adhering to cognitive visual hierarchy rules tailored to small screens:
    </p>
    <ul>
      <li><strong>The 3-Second Mobile Test:</strong> Over 70 percent of YouTube watch time occurs on mobile devices. When your thumbnail appears on a smartphone screen, it measures roughly 180 by 100 pixels. If your text is smaller than 40pt or uses thin serif fonts, it becomes completely illegible. Limit thumbnail typography to 3 to 5 punchy words in bold sans-serif typefaces (Impact, Montserrat Black, Bebas Neue).</li>
      <li><strong>High-Contrast Face Framing:</strong> Human brains are evolutionary wired to detect facial emotion. Frame human faces to occupy at least 30 to 45 percent of the thumbnail height, with clear eye contact and high contrast between the subject and the ambient background.</li>
      <li><strong>Color Saturation and Gamut Separation:</strong> The default YouTube interface is either stark white (Light Mode) or dark charcoal (Dark Mode). Utilizing vibrant accent borders (warm amber, neon cyan, electric lime) separates your thumbnail from the surrounding page UI.</li>
      <li><strong>Visual Storytelling Without Title Duplication:</strong> Never repeat your video title verbatim in the thumbnail. Instead, use the thumbnail to present the emotional question or visual punchline that the title describes.</li>
    </ul>

    <h2>Compressing Thumbnails Under 2MB Without Losing Sharpness: The Quality 92 Rule</h2>
    <p>
      Many creators export thumbnails directly from Photoshop or Illustrator as 24-bit PNG files, resulting in files measuring 3 to 8 MB. When attempting to upload, YouTube throws an error. Desperate creators then use aggressive web compressors that degrade the image into noisy, artifact-ridden mush.
    </p>
    <p>
      RemoveSynth solves this dilemma by applying optimal 2D DCT quantization:
    </p>
    <ul>
      <li><strong>Why PNG is Overkill for Thumbnails:</strong> PNG uses lossless DEFLATE compression, which is brilliant for flat logos but mathematically inefficient for photographs with millions of unique color gradients. A photograph saved as PNG often takes 4 MB, whereas the identical image saved as a high-quality JPEG (Quality 92) takes only 320 KB (over 90 percent smaller).</li>
      <li><strong>The Visual Sweet Spot (Quality 92):</strong> At JPEG Quality 92, quantization noise remains well below the human visual threshold (Peak Signal-to-Noise Ratio exceeding 44 dB), while staying far below the 2.0 MB platform limit.</li>
      <li><strong>WebP Format Support:</strong> Modern YouTube versions fully accept WebP format. Exporting as WebP achieves an additional 25 to 35 percent file size reduction compared to JPEG at identical structural similarity.</li>
    </ul>

    <h2>Common YouTube Thumbnail Mistakes That Cost You Views and Impressions</h2>
    <p>
      Avoid these common thumbnail pitfalls that undermine creator performance:
    </p>
    <ul>
      <li><strong>Placing Critical Info in the Bottom Right Corner:</strong> The video duration badge (for example, &quot;18:42&quot;) is hardcoded into the lower right corner across all mobile, desktop, and TV apps. Any text, face, or logo placed in the bottom right 150 by 70 pixel rectangle is completely blocked from view.</li>
      <li><strong>Ignoring Mobile Aspect Ratio Cropping:</strong> In certain mobile app views (such as vertical recommendation rails and subscriptions feeds), YouTube occasionally crops edge margins. Always keep focal elements centered.</li>
      <li><strong>Over-Cluttering the Canvas:</strong> Adding multiple arrows, speech bubbles, five logos, and two background scenes creates visual chaos. Simple, bold, uncluttered compositions consistently outperform complex collages.</li>
    </ul>
"""

if '<h2>High Click-Through Rate (CTR)' not in orig:
    target = '<h2>Why RemoveSynth Outperforms Cloud Resizers'
    orig = orig.replace(target, more_yt_sections + '\n\n    ' + target)

with open('apps/removesynth/src/pages/youtube-thumbnail-resizer.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'youtube-thumbnail-resizer body word count: {words}')
