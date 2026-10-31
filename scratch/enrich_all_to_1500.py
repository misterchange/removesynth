import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Custom enrichment blocks tailored to specific topics
tailored_blocks = {
    'ai-image-resizer.astro': """
    <h2>Common Aspect Ratio and Resolution Presets for Generative AI Models</h2>
    <p>
      Generative diffusion models require specific aspect ratio and pixel budget configurations during prompt generation:
    </p>
    <ul>
      <li><strong>Square 1:1 (1024x1024 px):</strong> The standard training baseline for DALL-E 2, DALL-E 3, and Stable Diffusion 1.5. Excellent for Instagram grid feeds, avatars, and icons.</li>
      <li><strong>Landscape 16:9 (1792x1024 or 1344x768 px):</strong> Common in Midjourney (--ar 16:9) and Flux.1 for desktop wallpapers, cinematic concept art, and YouTube video banners.</li>
      <li><strong>Portrait 9:16 (1024x1792 px):</strong> Essential for vertical TikTok, YouTube Shorts, and Instagram Reels cover art.</li>
      <li><strong>Standardizing with Ambient Fill:</strong> Using RemoveSynth to scale and pad non-standard generation outputs guarantees that downstream ad networks and content management systems accept the images without distortion.</li>
    </ul>

    <h2>Color Profile Preservation: sRGB, Display P3, and Rec.709</h2>
    <p>
      Generative AI renderers frequently export files with uncalibrated color spaces or non-standard gamma curves. When these files are uploaded to social media or viewed on different mobile screens, colors can shift or appear flat. RemoveSynth applies standardized sRGB tone mapping, ensuring that highlights, deep blacks, and saturated neon tones display consistently across all consumer monitors and mobile panels.
    </p>
""",
    'compress-video-for-discord.astro': """
    <h2>Video Transcoding Codecs: H.264 (AVC) vs H.265 (HEVC) vs VP9 for Discord</h2>
    <p>
      Selecting the correct video codec is critical when compressing files to fit under Discords free file size limit:
    </p>
    <ul>
      <li><strong>H.264 / AVC (Broadest Compatibility):</strong> Plays back instantly in all Discord desktop clients, mobile apps, and browser web versions without requiring hardware transcoding or codec downloads.</li>
      <li><strong>Audio Compression Budget (AAC at 96 kbps):</strong> Allocating 96 kbps to stereo AAC audio preserves crisp voice chat and gaming sound effects while leaving over 90 percent of the byte budget dedicated to high-motion video frames.</li>
      <li><strong>Resolution Scaling (720p vs 1080p):</strong> For fast-paced FPS gaming clips (Valorant, Apex Legends, Call of Duty), scaling from 4K to 720p at 60 frames per second often looks significantly smoother and sharper than attempting to compress 1080p into a tight 10 MB limit.</li>
    </ul>
""",
    'video-metadata-remover.astro': """
    <h2>Understanding QuickTime and MP4 Atom Box Trees (moov, mvhd, trak)</h2>
    <p>
      ISO Base Media File Format containers structure media as hierarchical atom boxes (ISOBMFF, ISO/IEC 14496-12):
    </p>
    <ul>
      <li><strong>The moov Atom:</strong> Contains the master movie header (<code>mvhd</code>) and track headers (<code>tkhd</code>) describing video resolution, frame rates, and sample timing.</li>
      <li><strong>The udta (User Data) Atom:</strong> Houses human-readable metadata, including camera serial numbers, GPS coordinates, editing software tags, and chapter markers.</li>
      <li><strong>FastStart Web Optimization:</strong> When stripping metadata, RemoveSynth relocates the <code>moov</code> atom to the beginning of the file (before the <code>mdat</code> video payload), enabling immediate streaming playback without waiting for the full file to download.</li>
    </ul>
""",
    'jpg-to-pdf.astro': """
    <h2>Page Layout Options: Portrait, Landscape, and Auto-Orientation</h2>
    <p>
      When assembling diverse collections of scanned documents and mobile photographs into a single PDF, orientation consistency is essential:
    </p>
    <ul>
      <li><strong>Auto-Orientation Matching:</strong> RemoveSynth inspects the pixel width and height of each individual image, automatically setting landscape PDF pages for horizontal photos and portrait pages for vertical mobile scans.</li>
      <li><strong>Custom Page Margins:</strong> Choose between zero-margin borderless presentation (ideal for digital art portfolios) or standard 0.5-inch printer margins (ideal for contracts, tax forms, and formal applications).</li>
      <li><strong>Lossless Image Stream Passthrough:</strong> Unlike clunky desktop PDF converters that decompress and re-encode JPEGs, RemoveSynth encapsulates JPEG byte streams directly into PDF <code>/DCTDecode</code> image XObjects, preserving 100 percent of original image sharpness with zero generational loss.</li>
    </ul>
""",
    'geotag-photo.astro': """
    <h2>Understanding GPS Rational Coordinates: Degrees, Minutes, and Seconds (DMS)</h2>
    <p>
      The EXIF specification requires geographic location to be stored as three pairs of unsigned 32-bit rational numbers:
    </p>
    <ul>
      <li><strong>Latitude and Longitude Storage:</strong> Coordinates are represented as <code>[Degrees/1, Minutes/1, Seconds/1000]</code> paired with reference direction characters (<code>'N'</code>/<code>'S'</code> and <code>'E'</code>/<code>'W'</code>).</li>
      <li><strong>GPS Altitude (Tag 0x0006):</strong> Encoded as an unsigned rational representing distance in meters above or below sea level, paired with <code>GPSAltitudeRef</code> (0 for above sea level, 1 for below sea level).</li>
      <li><strong>WGS 84 Geodetic Datum:</strong> RemoveSynth adheres strictly to the World Geodetic System 1984 (WGS 84) standard, ensuring coordinates map with mathematical precision across Google Maps, Apple Maps, OpenStreetMap, and GIS software.</li>
    </ul>
""",
    'does-it-strip-metadata.astro': """
    <h2>The Legal and Security Stakes of Unintentional Location Leaks</h2>
    <p>
      Unintentionally publishing metadata has resulted in major real-world security breaches and legal exposures:
    </p>
    <ul>
      <li><strong>Celebrity and Executive Residence Exposures:</strong> High-profile individuals posting informal photos of pets or packages on social media have repeatedly had their private residential addresses uncovered by internet sleuths reading EXIF tags.</li>
      <li><strong>Military and Defense Operational Security (OPSEC):</strong> Military personnel taking fitness tracker screenshots or snapshots on airbases have inadvertently disclosed the layout of confidential forward operating locations.</li>
      <li><strong>The Safe Sharing Protocol:</strong> Before sharing photos across any public forum, classified marketplace, or messaging platform, run them through RemoveSynth to permanently sever tracking telemetry.</li>
    </ul>
""",
    'remove-synthid-from-text.astro': """
    <h2>Understanding Token Selection Perturbation and Watermark Detectability</h2>
    <p>
      Statistical AI text watermarking relies on biasing the token selection process during language model autoregressive generation:
    </p>
    <ul>
      <li><strong>Green and Red Token Partitions:</strong> The watermarking algorithm hashes the previous token to pseudo-randomly partition the model vocabulary into &quot;green&quot; (favored) and &quot;red&quot; (penalized) word lists, nudging the model to select green tokens.</li>
      <li><strong>Detecting the Bias:</strong> A statistical detector counts the proportion of green tokens in a text passage. Human writing exhibits an equal balance, while watermarked AI text shows a statistically improbable excess of green tokens (z-score > 4.0).</li>
      <li><strong>Neutralizing the Pattern:</strong> Restructuring sentences and replacing predictable synonym sequences disrupts the artificial token balance, restoring natural human statistical variance.</li>
    </ul>
""",
    'photo-metadata-remover.astro': """
    <h2>Why Professional Photographers Sanitize RAW and JPEG Exports</h2>
    <p>
      In commercial photography, client delivery requires balancing metadata utility with confidentiality:
    </p>
    <ul>
      <li><strong>Protecting Proprietary Camera Settings:</strong> Shutter speed, aperture, lighting ratios, and custom Camera Raw color recipes represent professional trade secrets that competitors can analyze from unstripped files.</li>
      <li><strong>Eliminating Client Location Geotags:</strong> Commercial shoots at private client estates, celebrity homes, or corporate campuses must never leak GPS coordinates into public advertising materials.</li>
      <li><strong>Zero Recompression Guarantee:</strong> RemoveSynth operates strictly at the binary container level, excising metadata segments while keeping image scan packets 100 percent untouched.</li>
    </ul>
""",
    'invisible-character-remover.astro': """
    <h2>Common Invisible Unicode Characters and Their Hexadecimal Codepoints</h2>
    <p>
      Invisible characters belong to diverse Unicode categories designed for typography, bidirectional text, and formatting control:
    </p>
    <ul>
      <li><strong>U+200B (Zero-Width Space):</strong> Intended for line-break opportunities in non-delimited scripts, frequently misused for secret text steganography.</li>
      <li><strong>U+200C and U+200D (Zero-Width Non-Joiner & Joiner):</strong> Used in Persian, Arabic, and Indic typography to control ligature connections.</li>
      <li><strong>U+FEFF (Zero-Width No-Break Space / Byte Order Mark):</strong> Legacy byte-order indicator that frequently corrupts web templates when prepended to UTF-8 text files.</li>
      <li><strong>U+00AD (Soft Hyphen):</strong> Invisible hyphenation hint that appears only when a word breaks at the end of a line.</li>
    </ul>
""",
    'resize-image-for-instagram.astro': """
    <h2>Instagram Grid Formatting: How Square (1:1) Thumbnails Center Your Photos</h2>
    <p>
      Even when you post vertical 4:5 portraits or widescreen photos, Instagram main profile grid displays every post as a cropped 1:1 square:
    </p>
    <ul>
      <li><strong>The Grid Centering Rule:</strong> Instagram crops your 4:5 portrait (1080x1350) into a square (1080x1080) by slicing 135 pixels off the top and bottom. Always keep human faces, typography, and primary subjects centered within the middle 1080x1080 zone.</li>
      <li><strong>Avoiding Pixel Distortion:</strong> Uploading odd aspect ratios (like 3:2 or 16:9) results in awkward grid cropping. Using RemoveSynth ensures your subject looks balanced both in the home feed and on your profile grid.</li>
    </ul>
""",
    'remove-c2pa-from-video.astro': """
    <h2>C2PA Manifest Verification vs In-Browser Excision Mechanics</h2>
    <p>
      The Coalition for Content Provenance and Authenticity (C2PA) standard establishes cryptographic trust trees across digital media:
    </p>
    <ul>
      <li><strong>Cryptographic Manifest Binds:</strong> C2PA binds a digital certificate and asset hash to the media file container. If any pixel or audio frame is modified, the digital signature breaks, flagging the asset as tampered.</li>
      <li><strong>Complete JUMBF Excision:</strong> Rather than invalidating the signature, RemoveSynth completely decouples the JUMBF box from the file header, restoring the file to a standard, unencumbered MP4/MOV container.</li>
    </ul>
""",
    'exiftool-online.astro': """
    <h2>Comprehensive EXIF Tag Directory: Key Indicators Checked by ExifTool</h2>
    <p>
      Our in-browser ExifTool engine catalogs all critical TIFF, EXIF, and XMP metadata directories:
    </p>
    <ul>
      <li><strong>IFD0 (Primary Image Directory):</strong> Make, Model, Orientation, Software, DateTime, Artist, Copyright.</li>
      <li><strong>ExifIFD (Sub-Directory):</strong> ExposureTime, FNumber, ExposureProgram, ISO, DateTimeOriginal, LensModel.</li>
      <li><strong>GPS IFD:</strong> GPSVersionID, GPSLatitude, GPSLongitude, GPSAltitude, GPSTimeStamp.</li>
      <li><strong>MakerNotes:</strong> Proprietary hardware diagnostics from Canon, Nikon, Sony, Apple, and Fujifilm.</li>
    </ul>
""",
    'remove-synthid-from-audio.astro': """
    <h2>Acoustic Fidelity Preservation During Audio Watermark Removal</h2>
    <p>
      Removing imperceptible watermarks without introducing audible distortion requires surgical signal processing:
    </p>
    <ul>
      <li><strong>Preserving Dynamic Range:</strong> Narrow-band notch filtering or phase jittering is applied only to frequency bands carrying the statistical watermark, leaving musical fundamentals and voice formants pristine.</li>
      <li><strong>Bit-for-Bit Uncompressed Export:</strong> Sanitized audio is written directly to lossless WAV or high-bitrate MP3, ensuring master recordings retain 100 percent broadcast quality.</li>
    </ul>
""",
    'remove-gemini-watermark.astro': """
    <h2>Imagen 3 Wavelet Watermarking vs Traditional Visual Overlays</h2>
    <p>
      Unlike visible logo watermarks that occupy surface pixels, SynthID operates deep within image frequency transformations:
    </p>
    <ul>
      <li><strong>Multi-Scale Wavelet Decomposition:</strong> Modifies subtle coefficients across low, medium, and high spatial frequency sub-bands.</li>
      <li><strong>Resilience to Compression:</strong> Withstands standard JPEG compression, scaling, and contrast adjustments.</li>
      <li><strong>Neutralization Strategy:</strong> RemoveSynth applies anti-correlation smoothing across targeted wavelet sub-bands, breaking detector confidence while preserving crisp photorealistic textures.</li>
    </ul>
""",
    'compress-image-for-whatsapp.astro': """
    <h2>Optimizing Image Compression for Mobile Messaging Bandwidth</h2>
    <p>
      Sending photos over mobile cellular networks demands striking the optimal balance between visual clarity and data consumption:
    </p>
    <ul>
      <li><strong>Reducing Cellular Data Usage:</strong> Compressing high-resolution camera photos from 15 MB down to 400 KB reduces mobile upload and download times by over 95 percent.</li>
      <li><strong>Ensuring Instant Delivery:</strong> Recipient phones on weak 3G or 4G connections download optimized files immediately without spinning loading wheels.</li>
    </ul>
""",
    'compress-image-for-discord.astro': """
    <h2>Discord Nitro File Limits vs Free Account Sharing Solutions</h2>
    <p>
      Discord users frequently hit the free tier upload ceiling when sharing gaming clips and screenshots:
    </p>
    <ul>
      <li><strong>Zero Cost Alternative to Nitro:</strong> Rather than paying $9.99 monthly for Nitro file storage, our in-browser tool optimizes your images to slip under the free tier cap in seconds.</li>
      <li><strong>Batch Drag-and-Drop:</strong> Optimize multiple gaming screenshots simultaneously and share them across your Discord communities.</li>
    </ul>
""",
    'exif-editor.astro': """
    <h2>IPTC and XMP Metadata Standards: Editorial Captioning and Tagging</h2>
    <p>
      Beyond hardware EXIF settings, photojournalists and commercial creators rely on IPTC and XMP metadata:
    </p>
    <ul>
      <li><strong>IPTC Core Fields:</strong> Creator, Credit Line, Copyright Notice, Object Name (Title), Caption/Abstract, Keywords.</li>
      <li><strong>SEO Value for Image Search:</strong> Search engine crawlers (Google Image Search) index embedded IPTC title and caption tags, improving ranking visibility for commercial portfolios.</li>
    </ul>
""",
    '[from]-to-[to].astro': """
    <h2>Why In-Browser Transcoding Outperforms Remote Cloud Converters</h2>
    <p>
      Traditional online file converters force users to upload photos to external cloud servers, introducing privacy risks, upload delays, and file size limits:
    </p>
    <ul>
      <li><strong>Complete Data Privacy:</strong> All bitstream decoding and encoding executes 100 percent locally in device memory via WebAssembly and HTML5 Canvas. Your private photos never leave your device.</li>
      <li><strong>Zero Network Transfer Time:</strong> Conversions complete in milliseconds without waiting for multi-megabyte files to upload and download.</li>
    </ul>
""",
    'compress-image-to-kb.astro': """
    <h2>Exam Application Photo Guidelines: UPSC, SSC, IBPS, and State PSCs</h2>
    <p>
      Government recruitment boards enforce exact technical specifications for candidate applications:
    </p>
    <ul>
      <li><strong>Passport Photograph Specs:</strong> Size between 20 KB and 50 KB, resolution between 350x450 and 600x600 pixels, plain white or light background.</li>
      <li><strong>Digital Signature Specs:</strong> Size between 10 KB and 20 KB, resolution 300x100 pixels, scanned in black ink on white paper.</li>
      <li><strong>Guaranteed Compliance:</strong> RemoveSynth hits your exact KB target without repeated trial-and-error adjustments.</li>
    </ul>
""",
    'compress-image-to-[size].astro': """
    <h2>Kilobyte vs Kibibyte: How Systems Calculate File Size Ceilings</h2>
    <p>
      Understanding how file limits are calculated prevents unexpected upload failures:
    </p>
    <ul>
      <li><strong>Decimal Kilobytes (1 KB = 1000 Bytes):</strong> Standard used by storage manufacturers and web forms. A 50 KB limit means 50,000 bytes.</li>
      <li><strong>Binary Kibibytes (1 KiB = 1024 Bytes):</strong> Traditional operating system calculation. A 50 KiB limit equals 51,200 bytes.</li>
      <li><strong>Strict Bisection Clamping:</strong> RemoveSynth calculates targets using the stricter decimal standard, ensuring your file passes both binary and decimal upload checks.</li>
    </ul>
""",
    'etsy-photo-cleaner.astro': """
    <h2>Etsy Search Ranking Factors: How Photo Quality and Speed Impact Conversions</h2>
    <p>
      High-converting Etsy listings rely on pristine photography that loads instantaneously on mobile shopping apps:
    </p>
    <ul>
      <li><strong>Mobile Page Load Speeds:</strong> Over 65 percent of Etsy transactions occur on smartphones. Unbloated listing photos load immediately, reducing cart abandonment.</li>
      <li><strong>Clean Color Accuracy:</strong> Stripping metadata bloat while preserving sRGB color profiles ensures item colors match real-world inventory, minimizing customer returns.</li>
    </ul>
"""
}

# Run the enrichment loop
for filename, block in tailored_blocks.items():
    path = 'apps/removesynth/src/pages/' + filename
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
    except Exception as e:
        print(f"Error opening {path}: {e}")
        continue
    
    first_heading = re.search(r'<h2>(.*?)</h2>', block)
    if first_heading and first_heading.group(1) in c:
        continue
    
    # Try inserting before last Related H2 or before </article>
    m_rel = re.search(r'<h2>Related\s+.*?', c, re.IGNORECASE)
    if m_rel:
        pos = m_rel.start()
        new_c = c[:pos] + block + '\n\n    ' + c[pos:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Enriched: {filename}")
    else:
        m_art = re.search(r'</article>', c, re.IGNORECASE)
        if m_art:
            pos = m_art.start()
            new_c = c[:pos] + block + '\n\n  ' + c[pos:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_c)
            print(f"Enriched: {filename}")
        else:
            print(f"Could not find insertion point: {filename}")

print("Enrichment run complete.")
