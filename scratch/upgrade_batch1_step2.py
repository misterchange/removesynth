import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. remove-metadata-iphone.astro
with open('apps/removesynth/src/pages/remove-metadata-iphone.astro', 'r', encoding='utf-8') as f:
    c = f.read()

iphone_sec = """
    <h2>Why AirDrop and iCloud Shared Albums Leak Family Geolocation</h2>
    <p>
      Many iPhone users assume that AirDrop or iCloud Shared Albums sanitize photos automatically. Apple ecosystem sharing preserves rich camera attributes by design:
    </p>
    <ul>
      <li><strong>AirDrop Direct Peer-to-Peer Transfer:</strong> AirDrop transfers the raw container byte-for-byte. Sending a photo via AirDrop to an acquaintance, coworker, or classmate transmits exact home GPS coordinates and camera serial numbers.</li>
      <li><strong>iCloud Shared Photo Albums:</strong> When family members contribute to a shared album, contributors can tap the &quot;i&quot; info button to view map pins and capture time stamps for every single contributor photo.</li>
      <li><strong>iMessage Full Resolution Sharing:</strong> Sending photos via iMessage with &quot;Low Quality Image Mode&quot; disabled transmits full EXIF payloads. Running photos through RemoveSynth beforehand guarantees zero metadata transfer.</li>
    </ul>
"""
if '<h2>Why AirDrop and iCloud' not in c:
    c = c.replace('<h2>Frequently Asked Questions About iPhone Photo Metadata</h2>', iphone_sec + '\n\n    <h2>Frequently Asked Questions About iPhone Photo Metadata</h2>')
    with open('apps/removesynth/src/pages/remove-metadata-iphone.astro', 'w', encoding='utf-8') as f:
        f.write(c)

# 2. remove-metadata-android.astro
with open('apps/removesynth/src/pages/remove-metadata-android.astro', 'r', encoding='utf-8') as f:
    c = f.read()

android_sec = """
    <h2>Google Photos Cloud Backups: How EXIF Tags Are Cataloged and Indexed</h2>
    <p>
      When photos automatically sync from an Android phone to Google Photos cloud storage, Google automated indexing systems parse and catalog every metadata tag:
    </p>
    <ul>
      <li><strong>Facial Recognition Clustering:</strong> Combined with GPS locations, Google Photos builds an interactive timeline of where and when you met specific individuals.</li>
      <li><strong>Search Query Association:</strong> Searching &quot;beach 2023&quot; or &quot;Paris&quot; inside Google Photos works because the system indexes the embedded GPS and timestamp tags.</li>
      <li><strong>Public Album Link Vulnerability:</strong> Generating a public Google Photos sharing link allows recipients to download original quality files containing unstripped GPS metadata. Sanitizing files with RemoveSynth prior to sharing prevents location leakage.</li>
    </ul>

    <h2>WhatsApp, Telegram, and Signal: How Messaging Apps Treat Android EXIF Data</h2>
    <p>
      How your photos are handled depends on whether you send them as standard compressed media or uncompressed document files:
    </p>
    <ul>
      <li><strong>Standard Chat Media Send:</strong> WhatsApp and Telegram re-compress images and strip EXIF data from standard chat views.</li>
      <li><strong>Send as Document (Uncompressed):</strong> When you choose &quot;Send as Document&quot; in WhatsApp or Telegram to preserve 4K quality, the platforms transmit the original, unstripped file byte-for-byte, exposing full GPS coordinates and camera serials to the recipient. Always sanitize with RemoveSynth before sending as a document.</li>
    </ul>
"""
if '<h2>Google Photos Cloud Backups:' not in c:
    c = c.replace('<h2>Frequently Asked Questions About Android Photo Metadata</h2>', android_sec + '\n\n    <h2>Frequently Asked Questions About Android Photo Metadata</h2>')
    with open('apps/removesynth/src/pages/remove-metadata-android.astro', 'w', encoding='utf-8') as f:
        f.write(c)

# 3. add-camera-exif.astro
with open('apps/removesynth/src/pages/add-camera-exif.astro', 'r', encoding='utf-8') as f:
    c = f.read()

camera_sec = """
    <h2>Why Drone and Action Cam Photographers Inject Custom Camera Profiles</h2>
    <p>
      Aerial drone footage (DJI Mavic, Mini, Inspire) and action cameras (GoPro Hero, Insta360) frequently write fragmented or non-standard EXIF headers:
    </p>
    <ul>
      <li><strong>Harmonizing Aerial Shots with Ground Cameras:</strong> Commercial real estate photographers shoot aerial vistas on drones and interior architectural photos on full-frame mirrorless bodies. Injecting standard camera tags allows client galleries to filter and present shoots consistently.</li>
      <li><strong>Fixing Scanned Film Drone Emulations:</strong> Photographers emulating cinematic aerial styles use custom camera tags to catalog film stock profiles.</li>
      <li><strong>Client Delivery Compliance:</strong> Stock photo agencies and enterprise clients mandate specific camera make and model fields in submission metadata.</li>
    </ul>

    <h2>EXIF MakerNote Preservation: Why Fake Online EXIF Tools Corrupt Images</h2>
    <p>
      Many rudimentary online EXIF editors corrupt image files because they overwrite TIFF offsets blindly without recalculating IFD pointer tables. RemoveSynth parses the complete TIFF IFD structure with byte-level precision, generating clean, standard-compliant EXIF segments that open reliably in Photoshop, Lightroom, and Windows File Explorer.
    </p>
"""
if '<h2>Why Drone and Action Cam' not in c:
    c = c.replace('<h2>Frequently Asked Questions</h2>', camera_sec + '\n\n    <h2>Frequently Asked Questions</h2>')
    with open('apps/removesynth/src/pages/add-camera-exif.astro', 'w', encoding='utf-8') as f:
        f.write(c)

# 4. heic-to-jpg.astro
with open('apps/removesynth/src/pages/heic-to-jpg.astro', 'r', encoding='utf-8') as f:
    c = f.read()

heic_sec = """
    <h2>Batch HEIC to JPG Transcoding: Processing Hundreds of Vacation Photos Locally</h2>
    <p>
      Returning from vacation with 500 iPhone HEIC photos creates a major bottleneck when sharing photos with family members on Android or Windows PCs:
    </p>
    <ul>
      <li><strong>Avoiding Cloud Upload Bandwidth Caps:</strong> Uploading 500 HEIC photos (typically 1.5 GB of data) to online cloud converter websites consumes significant home or mobile bandwidth and risks third-party data scraping.</li>
      <li><strong>Multi-Threaded Parallel Conversion:</strong> RemoveSynth leverages your computer local multi-core CPU via Web Workers. Converting 30 HEIC photos takes only a few seconds directly in browser RAM.</li>
      <li><strong>Consolidated ZIP Download:</strong> Save all converted JPEGs in a single click as a tidy, organized ZIP file ready for thumb drives or email.</li>
    </ul>
"""
if '<h2>Batch HEIC to JPG Transcoding:' not in c:
    c = c.replace('<h2>Frequently Asked Questions About Converting HEIC to JPG</h2>', heic_sec + '\n\n    <h2>Frequently Asked Questions About Converting HEIC to JPG</h2>')
    with open('apps/removesynth/src/pages/heic-to-jpg.astro', 'w', encoding='utf-8') as f:
        f.write(c)

print('Updated Batch 1 step 2')
