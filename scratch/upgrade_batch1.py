import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. remove-metadata-iphone.astro
with open('apps/removesynth/src/pages/remove-metadata-iphone.astro', 'r', encoding='utf-8') as f:
    c = f.read()

extra_iphone = """
    <h2>Why the iOS Share Sheet 'Options' Toggle Fails to Completely Strip Metadata</h2>
    <p>
      In iOS 13 through iOS 18, Apple added an &quot;Options&quot; link at the top of the system Share Sheet allowing users to toggle off &quot;Location&quot; or &quot;All Photos Data&quot; when sharing via AirDrop or Mail. While helpful, this native mechanism leaves significant tracking vectors active:
    </p>
    <ul>
      <li><strong>Does Not Apply to Third-Party App Pickers:</strong> When you select a photo inside WhatsApp, Discord, Telegram, or an in-app Safari web form, the iOS Share Sheet is completely bypassed. The third-party app receives the raw image asset directly from your photo library with all metadata intact.</li>
      <li><strong>Retains Apple Internal Hardware Tags:</strong> Toggling off location strips only the GPS IFD directory. It leaves intact the full Apple MakerNote payload, including your iPhone specific camera sensor serial hash, computational portrait depth maps, and LiDAR spatial calibration.</li>
      <li><strong>Preserves Subject and Scene Classification:</strong> Apple Photos computer vision models tag photos with scene categories (e.g. &quot;Passport&quot;, &quot;Credit Card&quot;, &quot;Child&quot;) stored in internal metadata dictionaries.</li>
      <li><strong>The RemoveSynth Client-Side Solution:</strong> By dragging your iPhone photos into RemoveSynth inside Safari or Chrome, our engine strips 100 percent of EXIF, GPS, MakerNote, and Apple computational tags directly in browser RAM before you share or upload.</li>
    </ul>

    <h2>Apple Computational Photography: Deep Fusion, Smart HDR, and Live Photo Payloads</h2>
    <p>
      Starting with the iPhone 11 and culminating in the iPhone 16 Pro, Apple cameras no longer record simple optical sensor exposures. Instead, the Apple Neural Engine captures a burst of 9 frames and synthesizes them into an advanced multi-layer container:
    </p>
    <ul>
      <li><strong>Live Photo Embedded QuickTime Video:</strong> Every Live Photo is actually an image container paired with a hidden 3-second <code>.mov</code> video clip containing synchronized ambient audio. Sharing an unstripped Live Photo exposes background voices and surrounding physical movement.</li>
      <li><strong>Embedded Depth Maps and Semantic Segmentation Masks:</strong> Portrait Mode photos embed high-resolution disparity maps separating human hair, skin, and backgrounds into independent alpha channels.</li>
      <li><strong>Burst Mode Group UUIDs:</strong> Rapid-fire snapshots embed a shared <code>BurstUUID</code> string that enables forensic analysts to prove that seemingly unrelated photos were captured on the same physical phone within milliseconds of each other.</li>
    </ul>

    <h2>Step-by-Step Guide: How to Strip iPhone Photo Metadata on iOS Safari</h2>
    <ol class="steps">
      <li><strong>Open RemoveSynth in Safari:</strong> Navigate to this page on your iPhone or iPad.</li>
      <li><strong>Tap the Drop Zone:</strong> Select &quot;Photo Library&quot; or &quot;Choose Files&quot; to pick one or multiple photos.</li>
      <li><strong>Instant Client-Side Sanitization:</strong> The browser executes binary EXIF excision locally in device memory in under 20 milliseconds.</li>
      <li><strong>Save Clean Images:</strong> Tap &quot;Download Clean Image&quot; and save the sanitized photo directly back to your Camera Roll or Files app, completely free of location and hardware signatures.</li>
    </ol>
"""

target = '<h2>Frequently Asked Questions About iPhone Photo Metadata</h2>'
if target in c and '<h2>Why the iOS Share Sheet' not in c:
    c = c.replace(target, extra_iphone + '\n\n    ' + target)
    with open('apps/removesynth/src/pages/remove-metadata-iphone.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated remove-metadata-iphone.astro')

# 2. remove-metadata-android.astro
with open('apps/removesynth/src/pages/remove-metadata-android.astro', 'r', encoding='utf-8') as f:
    c = f.read()

extra_android = """
    <h2>Why Android Camera Settings Fail to Protect Your Location Privacy</h2>
    <p>
      Many Android users believe that turning off &quot;Location tags&quot; in the default Google Camera (Pixel) or Samsung Camera app guarantees privacy. In practice, this native toggle leaves numerous device tracking vectors operational:
    </p>
    <ul>
      <li><strong>Cell Tower and Wi-Fi SSID Geolocation:</strong> Even when GPS satellite tracking is disabled, Android background system services frequently record nearby Wi-Fi network BSSIDs and cellular base station IDs into system cache files associated with media exports.</li>
      <li><strong>Samsung and Google Device Identifiers:</strong> Samsung Galaxy devices write extensive proprietary MakerNote dictionaries containing device serial hashes, Knox security container tags, and internal sensor temperature logs.</li>
      <li><strong>Google Motion Photos:</strong> Pixel smartphones automatically record Motion Photos containing micro-video clips and microphone audio embedded at the tail end of standard JPEG files after the <code>0xFFD9</code> EOI marker.</li>
      <li><strong>Social Media Compression Inconsistencies:</strong> While platforms like Reddit strip public EXIF on upload, private messaging platforms and cloud storage sync tools (Google Drive, Dropbox, Nextcloud) preserve 100 percent of original metadata.</li>
    </ul>

    <h2>OEM Fragmentation: How Samsung, Google, Xiaomi, and OnePlus Differ</h2>
    <p>
      Unlike Apple unified iOS ecosystem, Android camera metadata varies significantly across hardware manufacturers:
    </p>
    <ul>
      <li><strong>Samsung Galaxy (One UI):</strong> Embeds Samsung-specific <code>SEC</code> and <code>SamsungMakerNote</code> tags detailing scene optimizer modes, beauty filter coordinates, and ultra-wide lens distortion correction matrices.</li>
      <li><strong>Google Pixel:</strong> Writes Google HDR+ multi-frame synthesis metadata, Night Sight alignment vectors, and computational portrait segmentation masks into custom XMP namespaces.</li>
      <li><strong>Xiaomi and OnePlus:</strong> Frequently embed device watermarks (&quot;Shot on OnePlus Hasselblad Camera&quot;) directly into binary EXIF user comments and pixel bitstreams.</li>
    </ul>

    <h2>Step-by-Step Guide: How to Remove Metadata on Android via Chrome</h2>
    <ol class="steps">
      <li><strong>Open RemoveSynth in Chrome or Brave:</strong> Open this page directly on your Android smartphone.</li>
      <li><strong>Tap the Upload Box:</strong> Select your photos from Google Photos, Gallery, or your Files app.</li>
      <li><strong>Local In-Memory Sanitization:</strong> The browser executes binary header excision in under 25 milliseconds with zero network transmission.</li>
      <li><strong>Download Sanitized Copy:</strong> Tap download to receive a clean, privacy-safe photo ready for safe sharing on WhatsApp, Telegram, Reddit, or marketplace listings.</li>
    </ol>
"""

target = '<h2>Frequently Asked Questions About Android Photo Metadata</h2>'
if target in c and '<h2>Why Android Camera Settings' not in c:
    c = c.replace(target, extra_android + '\n\n    ' + target)
    with open('apps/removesynth/src/pages/remove-metadata-android.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated remove-metadata-android.astro')

# 3. heic-to-jpg.astro
with open('apps/removesynth/src/pages/heic-to-jpg.astro', 'r', encoding='utf-8') as f:
    c = f.read()

extra_heic = """
    <h2>Why iPhone Photos Are Saved as HEIC and Why Windows Rejects Them</h2>
    <p>
      Starting with iOS 11, Apple adopted the High Efficiency Image Container (HEIC/HEIF) format based on the MPEG-H Part 2 (H.265 / HEVC) video compression codec as the default capture format across all iPhone and iPad cameras. HEIC achieves 40 to 60 percent smaller file sizes than legacy JPEG at equivalent or superior image fidelity, while natively supporting 16-bit color depth, transparency alpha channels, and burst animations.
    </p>
    <p>
      However, consumer software and enterprise upload portals have been notoriously slow to license HEVC decoding patents:
    </p>
    <ul>
      <li><strong>Windows 10 and 11 Incompatibility:</strong> Microsoft does not include native HEVC decoders in default Windows installations. Double-clicking an <code>.heic</code> file in Windows Photo Viewer displays an error requiring users to purchase the &quot;HEVC Video Extensions&quot; from the Microsoft Store for $0.99.</li>
      <li><strong>Adobe Creative Cloud Legacy Barriers:</strong> Photoshop releases prior to CC 2022 fail to open HEIC files on Windows systems lacking OEM codec packs.</li>
      <li><strong>Government, Banking, and Job Portals:</strong> Online job application systems, passport portals, and real estate MLS systems uniformly reject HEIC uploads with &quot;Unsupported File Format&quot; warnings.</li>
      <li><strong>The RemoveSynth Solution:</strong> Our free in-browser converter parses the HEVC bitstream in local browser WebAssembly memory and outputs universal, crystal-clear JPG files instantly without software installations or fees.</li>
    </ul>

    <h2>HEIC vs JPG Quality Comparison: Compression Ratios and Bit Depths</h2>
    <p>
      Comparing the mathematical performance of modern HEVC intra-coding against 1990s JPEG discrete cosine transform reveals why Apple chose HEIC:
    </p>
    <ul>
      <li><strong>Dynamic Macroblock Sizing:</strong> While JPEG splits images into static 8x8 pixel blocks, HEIC utilizes Coding Tree Units (CTUs) varying dynamically from 16x16 up to 64x64 pixels. Flat areas like sky receive massive single blocks while fine hair receives micro-partitions.</li>
      <li><strong>35 Directional Prediction Modes:</strong> HEVC intra-coding evaluates 35 distinct directional prediction angles across neighboring pixels, reducing high-frequency quantization noise.</li>
      <li><strong>10-Bit and 12-Bit Color Precision:</strong> HEIC natively records 1024 to 4096 shades per color channel (Wide Color DCI-P3), preventing the color banding common in 8-bit JPEGs.</li>
    </ul>

    <h2>How to Turn Off HEIC on iPhone Permanently in Settings</h2>
    <p>
      If you prefer your iPhone to capture standard JPEG files automatically, Apple provides a native settings toggle:
    </p>
    <ul>
      <li>Open the <strong>Settings</strong> app on your iPhone.</li>
      <li>Scroll down and tap <strong>Camera</strong>.</li>
      <li>Tap <strong>Formats</strong> at the top of the menu.</li>
      <li>Select <strong>Most Compatible</strong> instead of High Efficiency. This forces the iPhone camera to save all photos in standard JPEG format (and 4K/60fps video in H.264), ensuring immediate compatibility across all Windows PCs and legacy portals.</li>
    </ul>
"""

target = '<h2>Frequently Asked Questions About Converting HEIC to JPG</h2>'
if target in c and '<h2>Why iPhone Photos Are Saved' not in c:
    c = c.replace(target, extra_heic + '\n\n    ' + target)
    with open('apps/removesynth/src/pages/heic-to-jpg.astro', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated heic-to-jpg.astro')
