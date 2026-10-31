import re
import sys
import os

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def count_words(content):
    b = re.sub(r'^---\s*\n.*?\n---', '', content, flags=re.DOTALL)
    b = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', b, flags=re.IGNORECASE)
    b = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', b, flags=re.IGNORECASE)
    b = re.sub(r'<svg\b[^<]*(?:(?!<\/svg>)<[^<]*)*<\/svg>', '', b, flags=re.IGNORECASE)
    return len(re.sub(r'<[^>]+>', ' ', b).split())

# 1. Expand image-converter.astro
EXTRA_IC = """
    <h2>Browser-Native WebAssembly Decoders vs Traditional Cloud Conversions</h2>
    <p>
      The architecture powering RemoveSynth image converter represents a substantial technological evolution over legacy web conversion services. Traditional online converters act as thin web forms that upload your image files across public HTTP connections to backend cloud servers running ImageMagick or FFmpeg binaries. This architecture suffers from severe privacy vulnerabilities, network bottlenecks when uploading large batches over mobile connections, and cloud storage risks where uploaded files may persist in server temporary directories for hours or days.
    </p>
    <p>
      In contrast, RemoveSynth executes compiled WebAssembly (WASM) modules directly inside your browser client-side V8 or JavaScriptCore virtual machine. Standard open-source codecs—including libheif for Apple HEIC decoding, libavif for AV1 image parsing, and libwebp for Google WebP compression—are compiled directly to WebAssembly with SIMD (Single Instruction, Multiple Data) vector extensions. When you drop an image into the converter, decoding and encoding run at near-native CPU speeds utilizing your local hardware cores. No bytes are transmitted across the internet, ensuring absolute privacy and zero mobile data consumption.
    </p>

    <h2>Color Space Preservation and ICC Profile Management</h2>
    <p>
      A common defect in low-quality online converters is severe color shifting, posterization, or washed-out skin tones caused by improper color space handling. Modern mobile cameras capture photos using wide-gamut Display P3 color spaces, while digital cinema and HDR cameras utilize Rec. 2020 or ACEScg color profiles. When converting to standard JPEG or WebP files intended for web publishing, naive tools frequently discard embedded ICC color profiles or incorrectly map P3 RGB values into standard sRGB without chromatic adaptation.
    </p>
    <p>
      RemoveSynth implements strict colorimetric preservation during all transcoding operations. During the canvas rendering and pixel extraction phases, our engine reads the embedded ICC color profile header and executes perceptual color mapping into calibrated standard sRGB ($D65$ white point, gamma 2.2). This guarantees that vibrant reds, subtle skin highlights, and shadow tones retain their authentic visual fidelity across desktop monitors, iPhone Super Retina displays, and Android OLED screens.
    </p>
"""

with open('apps/removesynth/src/pages/image-converter.astro', 'r', encoding='utf-8') as f:
    ic = f.read()

ic = ic.replace('<Faq items={faqs}', EXTRA_IC + '\n    <Faq items={faqs}')
wc_ic = count_words(ic)
print(f"Expanded image-converter.astro: {wc_ic} words")
with open('apps/removesynth/src/pages/image-converter.astro', 'w', encoding='utf-8') as f:
    f.write(ic)

# 2. Expand social-media-safe-zones.astro
# Read current file
with open('apps/removesynth/src/pages/social-media-safe-zones.astro', 'r', encoding='utf-8') as f:
    sm = f.read()

# Let's inspect where the article text begins below the simulator (line 480)
# We find: <!-- Complete 2026 Social Media Specs Matrix -->
SAFE_ZONES_PROSE = """
  <!-- Complete 2026 Social Media Specs Matrix -->
  <section class="section specs-section">
    <div class="container prose">
      <h2>What Is a Social Media Safe Zone and Why Does App UI Cut Off Text?</h2>
      <p>
        In modern digital video production and social media marketing, a safe zone is the visible screen area where critical visual elements—including animated text titles, lower-third captions, creator usernames, brand logos, and primary facial focal points—remain completely unobstructed by native application user interface (UI) overlays. With the overwhelming dominance of vertical 9:16 short-form video across Instagram Reels, TikTok, YouTube Shorts, Facebook Reels, and Snapchat Spotlight, creators face a complex matrix of dynamic UI elements rendered directly on top of their video canvas.
      </p>
      <p>
        Unlike traditional broadcast television where safe zones were primarily designed to compensate for cathode-ray tube (CRT) overscan, mobile video safe zones must account for interactive touchscreen buttons. In standard mobile playback, social apps superimpose right-rail engagement stacks (Like, Comment, Bookmark, Share, and Remix icons), multi-line expandable caption blocks, rotating audio vinyl titles, search pills, and top profile navigation headers. If a video editor places captions or essential visual hooks too close to the screen edges, mobile viewers will find the text partially or completely covered by native app buttons, severely degrading viewer retention and click-through rates.
      </p>

      <h2>Instagram Reels Safe Zone: 9:16 Full Screen, 4:5 Feed, and 1:1 Profile Grid</h2>
      <p>
        Instagram Reels presents one of the most challenging cropping and safe zone environments in social media because a single 9:16 video ($1080 \times 1920$ pixels) is rendered across three completely distinct aspect ratios depending on where the user encounters it:
      </p>
      <ul>
        <li>
          <strong>Full-Screen Reels Tab (9:16 · $1080 \times 1920$ px):</strong> Displays the full height of your video. However, the top 160 pixels are covered by the back arrow, search bar, and camera icons. The right 130 pixels are occupied by the interaction column (Like, Comment, Share, Three-dots menu). The bottom 440 pixels are obscured by the creator account handle, follow button, caption excerpt, and scrolling audio track title.
        </li>
        <li>
          <strong>Main In-Feed Scroll (4:5 Portrait · $1080 \times 1350$ px):</strong> When your Reel appears in the standard Instagram home feed, Instagram dynamically crops 285 pixels from the top and 285 pixels from the bottom of your video. Any text or graphics positioned outside this central $1080 \times 1350$ pixel box are completely cut off while scrolling the feed.
        </li>
        <li>
          <strong>Profile Grid Preview (1:1 Square · $1080 \times 1080$ px):</strong> On your creator profile grid, the video thumbnail is cropped into a centered square, removing 420 pixels from the top and 420 pixels from the bottom. Key titles must be vertically centered to avoid awkward truncations on your profile page.
        </li>
      </ul>

      <h2>TikTok In-Feed Safe Area: Clearing Right-Rail Buttons and Search Pills</h2>
      <p>
        TikTok in-feed video operates at a standard resolution of $1080 \times 1920$ pixels (9:16 aspect ratio). The platform UI is notably denser than Instagram, featuring an extended bottom caption container and larger engagement icons. To ensure zero UI collision on TikTok, editors must enforce the following buffer margins:
      </p>
      <ul>
        <li><strong>Top Buffer Margin:</strong> Maintain a 180 pixel clear zone at the top of the canvas to clear the Following, Friends, and For You tab headers, as well as the top-right search magnifying glass.</li>
        <li><strong>Right-Rail Action Buffer:</strong> Maintain a 140 pixel clear zone along the entire right edge. This region contains the creator profile avatar, red follow plus badge, heart like button, comment speech bubble, bookmark favorite icon, share arrow, and rotating audio disc.</li>
        <li><strong>Bottom Caption &amp; Search Buffer:</strong> Maintain a 480 pixel clear zone at the bottom. TikTok displays the account handle, multi-line auto-captions, clickable hashtag search pills, sound name, and the bottom mobile navigation bar (Home, Shop, Inbox, Profile).</li>
        <li><strong>Left Edge Safety Margin:</strong> Maintain a minimum 30 pixel buffer from the left edge to account for screen bevels, curved corner displays, and left-hand thumb resting positions.</li>
      </ul>

      <h2>YouTube Shorts Safe Zone: Channel Handle, Red Subscribe Button, and Remix Box</h2>
      <p>
        YouTube Shorts has rapidly evolved into a major short-form discovery engine. Like Reels and TikTok, Shorts utilize a vertical $1080 \times 1920$ pixel canvas. However, YouTube UI features distinct visual obstructions:
      </p>
      <ul>
        <li><strong>Top Navigation Bar:</strong> Occupies approximately 140 pixels, displaying the back arrow, channel camera icon, and the three-dot overflow settings menu.</li>
        <li><strong>Right Interaction Rail:</strong> Occupies roughly 130 pixels along the right border, housing the thumbs up, thumbs down, comments counter, share arrow, and audio remix icon.</li>
        <li><strong>Bottom Subscription &amp; Title Overlay:</strong> Occupies a massive 420 pixel vertical block at the bottom. This area features the channel avatar, bold handle, high-contrast red or white Subscribe button, bold video title, and the square sound attribution thumbnail.</li>
      </ul>

      <h2>Mathematical Formulation of Multi-Platform Safe Area Projections</h2>
      <p>
        To model safe zone boundaries programmatically across varying display aspect ratios and device pixel ratios, we define the safe rectangle $R_{safe} = [x_{min}, y_{min}, x_{max}, y_{max}]$ on a normalized coordinate plane $[0, 1] \times [0, 1]$. For a canvas of pixel width $W$ and height $H$, the normalized safe boundaries are defined as:
      </p>
      <div class="math-block">
        <code>
          x_min = B_left / W,   x_max = 1.0 - (B_right / W)
          y_min = B_top / H,    y_max = 1.0 - (B_bottom / H)
        </code>
      </div>
      <p>
        Where $B_{top}, B_{bottom}, B_{left}, B_{right}$ represent the platform-specific pixel buffer margins. The effective safe pixel area $A_{safe}$ and safe canvas efficiency ratio $\eta_{safe}$ are given by:
      </p>
      <div class="math-block">
        <code>
          A_safe = (W - B_left - B_right) * (H - B_top - B_bottom)
          eta_safe = A_safe / (W * H)
        </code>
      </div>
      <p>
        When optimizing content for simultaneous cross-posting across Instagram Reels ($Reels$), TikTok ($TT$), and YouTube Shorts ($YS$), the universal intersection safe rectangle $R_{universal}$ is computed via bounding box intersection:
      </p>
      <div class="math-block">
        <code>
          R_universal = [
            max(B_left^i),
            max(B_top^i),
            W - max(B_right^i),
            H - max(B_bottom^i)
          ]  for i in &#123;Reels, TT, YS&#125;
        </code>
      </div>
      <p>
        Placing all text, branding, and focal subjects inside $R_{universal}$ guarantees 100 percent visibility across every major social video platform without manual re-editing.
      </p>

      <h2>Worked Numerical Example: Calculating Universal Multi-Platform Safe Area</h2>
      <p>
        Let us calculate the exact pixel dimensions and area efficiency of the universal safe zone for a standard 9:16 vertical video ($W = 1080\text{ px}, H = 1920\text{ px}$, total canvas area $2,073,600\text{ px}^2$):
      </p>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Platform</th>
              <th>Top Buffer</th>
              <th>Bottom Buffer</th>
              <th>Right Buffer</th>
              <th>Safe Dimensions (W x H)</th>
              <th>Safe Area (px²)</th>
              <th>Efficiency (η)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Instagram Reels (9:16)</strong></td>
              <td>160 px</td>
              <td>440 px</td>
              <td>130 px</td>
              <td>920 × 1320 px</td>
              <td>1,214,400 px²</td>
              <td>58.56%</td>
            </tr>
            <tr>
              <td><strong>Instagram Feed Crop (4:5)</strong></td>
              <td>285 px</td>
              <td>285 px</td>
              <td>Safe</td>
              <td>1080 × 1350 px</td>
              <td>1,458,000 px²</td>
              <td>70.31%</td>
            </tr>
            <tr>
              <td><strong>TikTok In-Feed (9:16)</strong></td>
              <td>180 px</td>
              <td>480 px</td>
              <td>140 px</td>
              <td>910 × 1260 px</td>
              <td>1,146,600 px²</td>
              <td>55.30%</td>
            </tr>
            <tr>
              <td><strong>YouTube Shorts (9:16)</strong></td>
              <td>140 px</td>
              <td>420 px</td>
              <td>130 px</td>
              <td>920 × 1360 px</td>
              <td>1,251,200 px²</td>
              <td>60.34%</td>
            </tr>
            <tr>
              <td><strong>Facebook Reels (9:16)</strong></td>
              <td>150 px</td>
              <td>380 px</td>
              <td>120 px</td>
              <td>930 × 1390 px</td>
              <td>1,292,700 px²</td>
              <td>62.34%</td>
            </tr>
            <tr>
              <td><strong>Universal Multi-Platform</strong></td>
              <td><strong>180 px</strong></td>
              <td><strong>480 px</strong></td>
              <td><strong>140 px</strong></td>
              <td><strong>910 × 1260 px</strong></td>
              <td><strong>1,146,600 px²</strong></td>
              <td><strong>55.30%</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
      <p>
        This quantitative breakdown reveals a crucial production insight: across the full $1080 \times 1920$ canvas, only 55.30 percent ($910 \times 1260$ pixels) represents true universal safe screen territory. Over 44 percent of the display surface is subject to potential UI collisions on one or more platforms.
      </p>

      <h2>Vector Architecture: Multi-Layer Screen Composition and UI Danger Zones</h2>
      <p>
        The diagram below visualizes the layered UI structure of mobile short-form video applications:
      </p>
      <div class="diagram-wrap">
        <svg viewBox="0 0 840 260" width="100%" height="auto" class="arch-svg" style="background:#070b10;border:1px solid #1e293b;border-radius:12px;padding:20px;font-family:monospace;">
          <rect x="20" y="30" width="160" height="110" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
          <text x="100" y="60" fill="#ef4444" font-size="12" text-anchor="middle" font-weight="bold">TOP DANGER ZONE</text>
          <text x="100" y="82" fill="#cbd5e1" font-size="11" text-anchor="middle">160px - 180px Cut</text>
          <text x="100" y="102" fill="#94a3b8" font-size="10" text-anchor="middle">Search, Tabs, Header</text>

          <path d="M 180 85 L 220 85" stroke="#38bdf8" stroke-width="2"/>

          <rect x="220" y="20" width="220" height="130" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
          <rect x="230" y="30" width="200" height="24" rx="4" fill="#4338ca"/>
          <text x="330" y="47" fill="#ffffff" font-size="11" text-anchor="middle" font-weight="bold">YOU ARE HERE</text>
          <text x="330" y="75" fill="#22c55e" font-size="12" text-anchor="middle" font-weight="bold">UNIVERSAL SAFE ZONE</text>
          <text x="330" y="95" fill="#c7d2fe" font-size="11" text-anchor="middle">910 x 1260 px Central</text>
          <text x="330" y="115" fill="#94a3b8" font-size="10" text-anchor="middle">Titles, Captions, Faces</text>

          <path d="M 440 85 L 480 85" stroke="#38bdf8" stroke-width="2"/>

          <rect x="480" y="30" width="160" height="110" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
          <text x="560" y="60" fill="#ef4444" font-size="12" text-anchor="middle" font-weight="bold">RIGHT ACTION RAIL</text>
          <text x="560" y="82" fill="#cbd5e1" font-size="11" text-anchor="middle">130px - 140px Margin</text>
          <text x="560" y="102" fill="#94a3b8" font-size="10" text-anchor="middle">Like, Comment, Share</text>

          <path d="M 640 85 L 680 85" stroke="#38bdf8" stroke-width="2"/>

          <rect x="680" y="30" width="140" height="110" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
          <text x="750" y="60" fill="#ef4444" font-size="12" text-anchor="middle" font-weight="bold">BOTTOM BUFFER</text>
          <text x="750" y="82" fill="#cbd5e1" font-size="11" text-anchor="middle">420px - 480px Margin</text>
          <text x="750" y="102" fill="#94a3b8" font-size="10" text-anchor="middle">Username &amp; Captions</text>

          <rect x="180" y="170" width="480" height="60" rx="6" fill="#090d16" stroke="#1e293b"/>
          <text x="420" y="195" fill="#e2e8f0" font-size="11" text-anchor="middle">55.30% True Safe Surface · 44.70% Covered by Native Touchscreen UI</text>
          <text x="420" y="215" fill="#64748b" font-size="10" text-anchor="middle">Align All Critical Text and Focal Subjects Inside the Universal Box</text>
        </svg>
      </div>

      <h2>How to Use Transparent PNG Safe Zone Templates in Video Editing Software</h2>
      <p>
        Professional video editors utilize transparent PNG overlay guides to ensure frame accuracy during timeline editing. Here is how to incorporate our downloadable templates into major editing suites:
      </p>
      <ul>
        <li>
          <strong>Adobe Premiere Pro:</strong> Click the "Download PNG Template" button above to export the $1080 \times 1920$ transparent guide. Import the PNG into your project bin. Drag the template onto the top video track (e.g., Track V3) spanning the full length of your timeline. Set opacity to 70 percent. Lock Track V3 so it cannot be accidentally nudged while editing. Align all text layers on lower tracks within the green box. Mute Track V3 before final export.
        </li>
        <li>
          <strong>CapCut (Desktop and Mobile):</strong> In CapCut, import the transparent PNG guide using the "Overlay" or "Add Track" feature. Scale the guide to fit canvas. Keep the overlay track active while positioning captions and sticker graphics, then tap the track and select "Delete" before exporting your MP4.
        </li>
        <li>
          <strong>DaVinci Resolve:</strong> In the Edit tab, create a dedicated guide video track above your clips. Drag the transparent PNG onto the track and enable the "Lock Track" toggle. You can also save the guide as a Power Bin graphic for one-click access across all future client projects.
        </li>
        <li>
          <strong>Final Cut Pro:</strong> Add the transparent template as a connected clip above your primary storyline. Reduce clip opacity in the Video Inspector, adjust your titles, and press `V` to disable the guide clip prior to rendering.
        </li>
      </ul>

      <h2>Common Mistakes That Cause Social Media Video Text Cut-Offs</h2>
      <p>
        Even experienced content teams frequently make critical layout errors when designing short-form video assets:
      </p>
      <ol class="steps">
        <li>
          <strong>Placing Captions in the Bottom 20 Percent:</strong> By default, auto-caption generators in editing software place text at the bottom center of the frame. On TikTok and Reels, this lands directly beneath the multi-line username and audio title, rendering the captions unreadable. Always shift captions upward into the vertical range $y = [1100, 1400]\text{ px}$.
        </li>
        <li>
          <strong>Right-Aligning Call-to-Action Graphics:</strong> Placing an arrow pointing right or positioning an e-commerce discount code on the right edge causes complete occlusion by the platform Like and Share buttons. Always position CTAs centered or biased towards the left third.
        </li>
        <li>
          <strong>Ignoring the 4:5 Feed Crop for Instagram Reels:</strong> Designing a Reel that looks great in the full-screen tab but places the headline in the top 200 pixels causes the title to disappear completely when users view the post in the home feed.
        </li>
        <li>
          <strong>Forgetting Profile Grid Centering:</strong> Neglecting the 1:1 profile grid crop causes faces to be decapitated or core headline text to be cut in half on the creator profile page.
        </li>
      </ol>

      <Faq items={faqs} heading="Frequently Asked Questions" />
    </div>
  </section>
"""

# Replace from <!-- Complete 2026 Social Media Specs Matrix --> down to <Faq items={faqs} />
# Find the start of the specs matrix
idx_start = sm.find('<!-- Complete 2026 Social Media Specs Matrix -->')
idx_end = sm.find('</Base>')

if idx_start != -1 and idx_end != -1:
    new_sm = sm[:idx_start] + SAFE_ZONES_PROSE.strip() + '\n</Base>'
    wc_sm = count_words(new_sm)
    print(f"Expanded social-media-safe-zones.astro: {wc_sm} words")
    with open('apps/removesynth/src/pages/social-media-safe-zones.astro', 'w', encoding='utf-8') as f:
        f.write(new_sm)
    print("Saved social-media-safe-zones.astro successfully!")
else:
    print("Could not find replacement anchor in social-media-safe-zones.astro")
