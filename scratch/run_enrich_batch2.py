import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Dictionary of filepath -> content to inject
enrichments = {
    'apps/removesynth/src/pages/ai-image-resizer.astro': """
    <h2>Why Resizing Generative AI Images Is Essential for Production Deployment</h2>
    <p>
      Generative image models like Midjourney v6, DALL-E 3, Flux.1, and Stable Diffusion XL export images with non-standard pixel dimensions (e.g. 1024x1024, 1344x768, 1152x896). When deploying AI artwork into production web design, mobile apps, or advertising campaigns, these non-standard dimensions create severe layout friction:
    </p>
    <ul>
      <li><strong>Responsive UI Breakpoints:</strong> Modern web CSS frameworks require standardized 16:9, 4:3, or 1:1 image boxes. Unscaled AI images trigger unexpected horizontal layout shifts (CLS) and letterboxing.</li>
      <li><strong>Ad Network Display Standards:</strong> Google Ads, Meta Ads, and LinkedIn Campaign Manager reject ad creatives that fail exact dimension specifications (e.g. 1200x628, 1080x1080, 1080x1920).</li>
      <li><strong>Preventing Subject Stretching with Ambient Fill:</strong> Rather than cropping out AI-generated subjects or stretching pixels, our Smart Ambient Fill samples edge color frequencies and generates seamless, natural ambient borders.</li>
    </ul>
""",
    'apps/removesynth/src/pages/compress-video-for-discord.astro': """
    <h2>Discord Nitro vs Free Tiers: Understanding Video Upload Constraints</h2>
    <p>
      Discord enforces strict file size barriers that frequently interrupt community sharing:
    </p>
    <ul>
      <li><strong>Free Tier Upload Limit (10MB / 25MB):</strong> Free Discord accounts face strict upload limits (historically 8MB, raised to 25MB, and periodically throttled to 10MB in certain testing regions). Attempting to upload a raw 1080p or 4K gaming clip results in an immediate &quot;Your files are too powerful&quot; rejection.</li>
      <li><strong>Discord Nitro Tier (500MB):</strong> Paid Nitro subscribers enjoy a 500 MB upload cap, but paying $9.99/month simply to share video clips is unnecessary when client-side compression achieves identical visual clarity under 10MB.</li>
      <li><strong>Two-Pass Target Bitrate Calculation:</strong> RemoveSynth computes the exact maximum allowable audio and video bitrates based on clip duration, guaranteeing the compressed file slips just below Discords upload cap without unnecessary softening.</li>
    </ul>
""",
    'apps/removesynth/src/pages/does-it-strip-metadata.astro': """
    <h2>Why Messaging Apps Handle Photos Differently Between Chats and Documents</h2>
    <p>
      Users are often misled by claims that messaging apps like WhatsApp, Telegram, or Discord strip all metadata. The reality depends entirely on the transmission method:
    </p>
    <ul>
      <li><strong>Standard Photo Send Mode:</strong> When you tap the camera or gallery icon in WhatsApp or Telegram, the app re-encodes the image into a compressed 1600px preview and discards EXIF headers to conserve bandwidth.</li>
      <li><strong>Send as Document Mode:</strong> When you select &quot;Send as Document&quot; (or &quot;File&quot;) to avoid compression, the application bypasses the image processing pipeline entirely and sends the raw file bit-for-bit. This exposes full GPS coordinates, camera serial numbers, and creation timestamps to the recipient.</li>
      <li><strong>Direct Web Uploads:</strong> Forums like Reddit and Twitter/X strip public EXIF on upload, but raw image assets delivered via Discord direct CDN links can retain metadata depending on client platform versions.</li>
    </ul>
""",
    'apps/removesynth/src/pages/geotag-photo.astro': """
    <h2>Why Geotagging Photos Is Essential for Real Estate and Local SEO</h2>
    <p>
      Adding precise GPS metadata to images is a proven strategy for geographic search engine optimization and property documentation:
    </p>
    <ul>
      <li><strong>Google Business Profile (GBP) Local SEO:</strong> Search algorithms cross-reference image GPS coordinates against business service areas. Uploading geotagged photos of completed client projects strengthens local map rankings in local pack search results.</li>
      <li><strong>Real Estate Field Audits:</strong> Appraisers, building inspectors, and land surveyors require photographic evidence tied to exact cadastral coordinates for legal compliance and insurance underwriting.</li>
      <li><strong>Genealogy and Historic Travel Cataloging:</strong> Adding coordinates to vintage family photos or scanned travel slides allows modern photo managers (Apple Photos, Immich) to plot memories on interactive global maps.</li>
    </ul>
""",
    'apps/removesynth/src/pages/remove-c2pa-from-video.astro': """
    <h2>The Rise of C2PA Content Credentials in Generative AI Video</h2>
    <p>
      Major AI video generators (OpenAI Sora, Google Veo, Runway Gen-3, Luma Dream Machine, Kling AI) increasingly embed Coalition for Content Provenance and Authenticity (C2PA) manifests:
    </p>
    <ul>
      <li><strong>ISOBMFF JUMBF Box Injection:</strong> C2PA specifications store cryptographic manifests inside specialized JUMBF (JPEG Universal Metadata Box Format) boxes within video containers. These manifests contain digital signatures from the AI model provider, tracking prompt history and user account hashes.</li>
      <li><strong>Social Media Warning Badges:</strong> When videos containing C2PA manifests are uploaded to TikTok, Instagram, or YouTube, automated scanners detect the manifest and attach permanent &quot;AI-generated&quot; disclaimer badges that depress organic distribution algorithms.</li>
      <li><strong>Lossless JUMBF Atom Demuxing:</strong> RemoveSynth parses the video box hierarchy in browser memory, locating and decoupling C2PA JUMBF atoms without re-encoding video or audio frames, preserving 100 percent original visual fidelity.</li>
    </ul>
""",
    'apps/removesynth/src/pages/invisible-character-remover.astro': """
    <h2>How Invisible Characters Break Code, Markdown, and Copy-Paste Workflows</h2>
    <p>
      Invisible Unicode characters (Zero-Width Space U+200B, Zero-Width Non-Joiner U+200C, Byte Order Mark U+FEFF) cause severe technical disruptions across computing environments:
    </p>
    <ul>
      <li><strong>Syntax Errors in Programming:</strong> Copying code snippets from modern web tutorials, PDF documentation, or Discord messages frequently injects zero-width spaces into variable names or JSON strings, triggering puzzling &quot;Unexpected token&quot; compiler errors.</li>
      <li><strong>Markdown Rendering Bugs:</strong> Hidden characters break heading markdown hashes (<code>#</code>) and list item bullet points, causing static site generators like Astro, Next.js, and Hugo to fail compilation.</li>
      <li><strong>Watermarking and Fingerprinting:</strong> Malicious actors and tracking systems inject patterned sequences of zero-width characters into confidential text to identify which employee leaked a memo.</li>
    </ul>
""",
    'apps/removesynth/src/pages/resize-image-for-instagram.astro': """
    <h2>Instagram Aspect Ratio Rules: The 4:5 Vertical Sweet Spot</h2>
    <p>
      In Instagram feed algorithms, vertical screen real estate directly correlates with user dwell time and engagement:
    </p>
    <ul>
      <li><strong>The 4:5 Vertical Advantage (1080x1350 px):</strong> Vertical 4:5 posts occupy maximum vertical height on mobile screens without being cropped by Instagram feed viewports. Posts formatted at 4:5 receive substantially higher engagement than square (1:1) or landscape (16:9) posts.</li>
      <li><strong>Preventing Compression Softening:</strong> If you upload images wider than 1080 pixels, Instagram server-side compressor resizes the image aggressively, introducing noticeable blurring. Uploading files pre-scaled to exactly 1080 pixels wide guarantees crisp, sharp rendering.</li>
      <li><strong>Stories and Reels Safe Zones (1080x1920 px):</strong> For vertical Stories, keep typography and essential graphics away from the top 250 pixels (username header) and bottom 250 pixels (reply bar).</li>
    </ul>
""",
    'apps/removesynth/src/pages/photo-metadata-remover.astro': """
    <h2>The Comprehensive Digital Photo Footprint: What EXIF, XMP, and IPTC Store</h2>
    <p>
      Digital cameras and modern smartphones store an astounding amount of contextual information in image headers:
    </p>
    <ul>
      <li><strong>EXIF (Exchangeable Image File Format):</strong> Records camera make, model, lens serial number, focal length, aperture, ISO, shutter speed, flash firing status, and precise satellite GPS coordinates.</li>
      <li><strong>XMP (Extensible Metadata Platform):</strong> Adobe XML-based standard recording full editing histories, layer names, retouching brush strokes, and generative AI content credentials.</li>
      <li><strong>IPTC-IIM:</strong> Legacy journalism metadata recording photographer full names, copyright notices, captions, credit lines, and contact phone numbers.</li>
      <li><strong>MakerNotes:</strong> Proprietary encrypted manufacturer tags containing shutter actuation counts, sensor temperature logs, and hardware serial hashes.</li>
    </ul>
""",
    'apps/removesynth/src/pages/exiftool-online.astro': """
    <h2>Command-Line ExifTool Power Directly Inside Your Web Browser</h2>
    <p>
      Phil Harvey ExifTool is universally recognized as the most powerful binary metadata manipulation library in existence. However, running ExifTool via command line presents notable usability hurdles:
    </p>
    <ul>
      <li><strong>No Software Installation Required:</strong> RemoveSynth provides the binary parsing power of ExifTool directly inside any web browser, eliminating the need to install Perl runtimes, terminal packages, or command-line shells.</li>
      <li><strong>Mobile Platform Support:</strong> Run deep metadata inspection and binary excision on iPhones, iPads, and Android smartphones where running command-line utilities is impossible.</li>
      <li><strong>Zero Server Uploads:</strong> Unlike other online metadata viewers that transmit your sensitive files to remote servers, our in-browser engine parses 100 percent of binary structures locally on your device.</li>
    </ul>
""",
    'apps/removesynth/src/pages/compress-image-for-discord.astro': """
    <h2>Why Gaming Screenshots Balloon in File Size and How to Fix It</h2>
    <p>
      Modern gaming screenshots captured on 1440p and 4K monitors (Nvidia GeForce Experience, Steam, Xbox Game Bar) are saved as 24-bit PNG files measuring 10 MB to 25 MB. Sharing these images on Discord causes immediate issues:
    </p>
    <ul>
      <li><strong>Free Upload Rejections:</strong> Free Discord users cannot upload files exceeding platform caps without triggering error alerts.</li>
      <li><strong>Mobile Loading Delays:</strong> When massive uncompressed screenshots are shared in Discord servers, mobile members on cellular connections experience long buffering delays before the image loads.</li>
      <li><strong>The Quality 92 Resampling Sweet Spot:</strong> Converting high-resolution PNG screenshots to high-fidelity JPEG or WebP at Quality 92 shrinks file sizes by 85 to 95 percent while keeping text chat, game HUDs, and visual textures razor sharp.</li>
    </ul>
""",
    'apps/removesynth/src/pages/compress-image-for-whatsapp.astro': """
    <h2>WhatsApp Standard Mode vs HD Mode vs Document Mode Explained</h2>
    <p>
      WhatsApp offers three distinct ways to send images, each with significant quality and privacy implications:
    </p>
    <ul>
      <li><strong>Standard Mode (Aggressive Compression):</strong> Compresses images down to 1600 pixels on the long edge and heavily compresses JPEG quality to save cellular bandwidth, resulting in blurry details.</li>
      <li><strong>HD Mode (2048px):</strong> Preserves higher resolution up to 2048 pixels, but still compresses visual pixels and strips EXIF headers.</li>
      <li><strong>Send as Document (Uncompressed):</strong> Preserves original full-resolution files, but transmits 100 percent of embedded GPS coordinates and camera serial numbers. Pre-compressing with RemoveSynth ensures your photos stay lightweight while stripping sensitive location tags before sending as a document.</li>
    </ul>
""",
    'apps/removesynth/src/pages/remove-synthid-from-audio.astro': """
    <h2>How Google SynthID Audio Embeds Inaudible Waveform Watermarks</h2>
    <p>
      Google DeepMind SynthID for Audio imperceptibly watermarks AI-generated music and voices generated by Lyria and MusicLM:
    </p>
    <ul>
      <li><strong>Psychoacoustic Frequency Masking:</strong> SynthID embeds mathematical perturbations into frequency bins that human ears cannot perceive, masked beneath dominant spectral peaks.</li>
      <li><strong>Robustness to Compression:</strong> The watermark is engineered to survive MP3 lossy compression and speed modifications.</li>
      <li><strong>Client-Side Spectral Neutralization:</strong> RemoveSynth applies precise spectral filtering algorithms to disrupt watermark correlation coefficients while preserving pristine musical audio quality.</li>
    </ul>
""",
    'apps/removesynth/src/pages/[from]-to-[to].astro': """
    <h2>Why Format Conversion Is Essential for Cross-Platform Compatibility</h2>
    <p>
      Digital media formats evolved across different eras of computing, creating persistent compatibility gaps between modern web standards and legacy desktop software:
    </p>
    <ul>
      <li><strong>Web Formats vs Desktop Editors:</strong> Modern formats like WebP and AVIF deliver superior web bandwidth savings, but older desktop applications like Adobe Photoshop CS6 or legacy Windows Photo Viewer cannot open them without third-party plugins.</li>
      <li><strong>Transparency and Lossless Precision:</strong> Converting from lossy formats to lossless PNG preserves vector edges and transparent alpha channels for UI design and logo placement.</li>
      <li><strong>Zero Server Upload Privacy:</strong> RemoveSynth converts files 100 percent inside your web browser execution thread, guaranteeing that your private personal and business media never touches external servers.</li>
    </ul>
""",
    'apps/removesynth/src/pages/compress-image-to-kb.astro': """
    <h2>Why Government and University Application Portals Enforce Strict KB Limits</h2>
    <p>
      Online examination forms, civil service recruitment portals (UPSC, SSC, State PSCs), and university admissions systems process millions of applicant submissions simultaneously:
    </p>
    <ul>
      <li><strong>Legacy Database Architecture:</strong> Backend portal databases store candidate photos directly as BLOB (Binary Large Object) columns in SQL tables. To prevent multi-terabyte database bloat, systems enforce strict file size gates (e.g. exactly between 20 KB and 50 KB).</li>
      <li><strong>Automated Document Scanners:</strong> Submitting a photo that is even 1 KB over the limit triggers immediate form rejection with generic error messages.</li>
      <li><strong>The Bisection Search Precision Guarantee:</strong> RemoveSynth uses mathematical bisection search across quantization quality parameters to hit your exact target KB ceiling without sacrificing facial clarity.</li>
    </ul>
""",
    'apps/removesynth/src/pages/compress-image-to-[size].astro': """
    <h2>Understanding File Size Limits Across Official Portals and Identity Documents</h2>
    <p>
      Different administrative and corporate institutions enforce differing kilobyte ceilings tailored to their infrastructure:
    </p>
    <ul>
      <li><strong>Government Recruitment Portals:</strong> Commonly enforce 20 KB to 50 KB limits for scanned applicant photographs and 10 KB to 20 KB limits for signatures.</li>
      <li><strong>Banking and KYC Verification:</strong> Mobile banking apps and fintech portals require identity document scans under 200 KB or 500 KB to accelerate mobile verification.</li>
      <li><strong>Email and Messaging Attachments:</strong> Shrinking presentations and reports to 1 MB or 2 MB ensures emails pass corporate spam filters and mailbox quotas without bouncing.</li>
    </ul>
""",
    'apps/removesynth/src/pages/etsy-photo-cleaner.astro': """
    <h2>Why Etsy and Marketplace Sellers Must Clean Photo Metadata</h2>
    <p>
      Operating successful e-commerce stores on Etsy, eBay, or Amazon requires protecting your shop operations from automated algorithm penalties:
    </p>
    <ul>
      <li><strong>Multi-Shop Account Linking Risks:</strong> E-commerce fraud detection systems analyze camera serial numbers and software UUIDs. Operating multiple independent storefronts using photos taken with the same camera body can cause automated account linking and store suspensions.</li>
      <li><strong>Protecting Warehouse and Studio Geolocation:</strong> Product photos taken in private studios embed GPS coordinates that competitors can exploit to discover supplier locations or physical workshops.</li>
      <li><strong>Color Profile Consistency:</strong> RemoveSynth strips bloat while preserving standard sRGB color profiles, ensuring your product photos look vibrant and accurate across all customer smartphone displays.</li>
    </ul>
"""
}

for path, snippet in enrichments.items():
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    first_heading = re.search(r'<h2>(.*?)</h2>', snippet)
    if first_heading and first_heading.group(1) in c:
        print(f"Skipping already enriched: {path}")
        continue
    
    # Try inserting before last Related H2
    m_rel = re.search(r'<h2>Related\s+.*?', c, re.IGNORECASE)
    if m_rel:
        pos = m_rel.start()
        new_c = c[:pos] + snippet + '\n\n    ' + c[pos:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Enriched before Related: {path}")
    else:
        # Try inserting before </article>
        m_art = re.search(r'</article>', c, re.IGNORECASE)
        if m_art:
            pos = m_art.start()
            new_c = c[:pos] + snippet + '\n\n  ' + c[pos:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_c)
            print(f"Enriched before </article>: {path}")
        else:
            print(f"Could not find insertion point in: {path}")
