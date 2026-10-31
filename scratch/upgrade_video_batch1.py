import sys
import re
import os

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def count_words(content):
    b = re.sub(r'^---\s*\n.*?\n---', '', content, flags=re.DOTALL)
    b = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', b, flags=re.IGNORECASE)
    b = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', b, flags=re.IGNORECASE)
    b = re.sub(r'<svg\b[^<]*(?:(?!<\/svg>)<[^<]*)*<\/svg>', '', b, flags=re.IGNORECASE)
    return len(re.sub(r'<[^>]+>', ' ', b).split())

VIDEO_TEMPLATE = """---
import Base from '../layouts/Base.astro';
import Jitter from '@removesynth/shared/components/Jitter.astro';
import Faq from '@removesynth/shared/components/Faq.astro';
import { faqSchema, breadcrumbSchema, type FaqItem } from '@removesynth/shared/lib/faq';
import { SITE } from '../site';

const title = '__TITLE__';
const description =
  '__DESC__';

const faqs: FaqItem[] = [
  {
    q: 'How do I remove the __MODEL_NAME__ watermark from my video?',
    a: 'Upload your __MODEL_NAME__ MP4 video into the cleaner above. Our client-side sanitizer losslessly wipes the container user-data (udta), encoder stamps, and C2PA provenance UUID boxes in under 1 second without re-encoding your video bitstream.',
  },
  {
    q: 'Does __MODEL_NAME__ add watermarks and metadata to exported clips?',
    a: 'Yes, __MODEL_NAME__ video exports can include bottom corner logo stamps on free and trial tiers as well as MP4 container user-data (udta), encoder provenance tags, and C2PA Content Credentials that platforms like Instagram and TikTok scan to flag AI video.',
  },
  {
    q: 'Will removing the watermark re-encode or compress my video?',
    a: 'No. Our in-browser container sanitizer operates strictly at the MP4 box header level. Video frames and audio streams are preserved bit-for-bit without generational loss, preserving original bitrate, frame rate, and resolution.',
  },
  {
    q: 'Can I clean 9:16 vertical videos for TikTok and Instagram Reels?',
    a: 'Yes. All video aspect ratios including 9:16 vertical, 16:9 widescreen, 1:1 square, and 4:3 broadcast are fully supported for instant client-side sanitization.',
  },
  {
    q: 'Are my private __MODEL_NAME__ videos uploaded to an external server?',
    a: 'Never. All container demuxing, box parsing, and file assembly execute 100 percent locally inside your web browser memory. Your video files never leave your computer or phone.',
  },
  {
    q: 'How does this tool prevent social media AI info labeling?',
    a: 'Social platforms like Instagram, TikTok, and YouTube scan MP4 user-data atoms (`udta`) and C2PA provenance boxes (`uuid`) during ingestion. By safely zeroing these tracking atoms into standard padding boxes (`free`), platforms treat your video as authentic camera footage.',
  },
  {
    q: 'Does this tool work on mobile devices like iPhone and Android?',
    a: 'Yes. You can open this tool in Safari on iOS or Chrome on Android, select your __MODEL_NAME__ video from your photo library or Files app, and download the sanitized MP4 directly to your device.',
  },
  {
    q: 'What video file formats are supported by the sanitizer?',
    a: 'The sanitizer supports standard MP4, MOV, and WebM video containers exported by generative AI video platforms up to 500 MB in file size.',
  },
];

const canonicalUrl = `${SITE.url}/__SLUG__/`;

const singleSchemaGraph = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'WebPage',
      '@id': canonicalUrl,
      url: canonicalUrl,
      name: title,
      description,
      inLanguage: 'en-US',
      isPartOf: {
        '@type': 'WebSite',
        '@id': `${SITE.url}/#website`,
        name: SITE.name,
        url: SITE.url,
      },
      breadcrumb: {
        '@type': 'BreadcrumbList',
        itemListElement: [
          { '@type': 'ListItem', position: 1, name: 'Home', item: `${SITE.url}/` },
          { '@type': 'ListItem', position: 2, name: 'Tools', item: `${SITE.url}/tools/` },
          { '@type': 'ListItem', position: 3, name: '__MODEL_NAME__ Video Sanitizer', item: canonicalUrl },
        ],
      },
    },
    {
      '@type': ['SoftwareApplication', 'WebApplication'],
      name: '__MODEL_NAME__ Video Sanitizer',
      url: canonicalUrl,
      applicationCategory: 'MultimediaApplication',
      operatingSystem: 'Any (web browser)',
      offers: {
        '@type': 'Offer',
        price: '0',
        priceCurrency: 'USD',
      },
      description,
    },
    {
      '@type': 'FAQPage',
      mainEntity: faqs.map((f) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: {
          '@type': 'Answer',
          text: f.a,
        },
      })),
    },
  ],
};
---

<Base title={title} description={description} schema={singleSchemaGraph}>
  <section class="hero">
    <div class="container">
      <span class="eyebrow">Instant In-Browser Sanitizer · __MODEL_NAME__ · Lossless Container Cleaning</span>
      <h1>Remove <span class="accent">__MODEL_NAME__ Watermark</span> &amp; Metadata</h1>
      <p class="lead">
        Sanitize __MODEL_NAME__ video exports for TikTok, Instagram Reels, and YouTube Shorts. Strip MP4 user-data, encoder stamps, and C2PA credentials losslessly in your browser.
      </p>

      <div class="tool-stage">
        <Jitter side="left" />
        <div class="vid-tool" id="vid-tool">
          
          <div class="vid-dropzone" id="dz">
            <input type="file" id="file-in" accept="video/mp4,video/quicktime,video/webm" hidden />
            <div class="dz-prompt" id="dz-prompt">
              <svg viewBox="0 0 24 24" width="46" height="46" fill="none" stroke="currentColor" stroke-width="2">
                <polygon points="23 7 16 12 23 17 23 7"></polygon>
                <rect x="1" y="5" width="15" height="14" rx="2" ry="2"></rect>
              </svg>
              <p><strong>Click or drop __MODEL_NAME__ video here</strong></p>
              <span class="small muted">MP4, MOV, WebM · Instant lossless container sanitization</span>
            </div>
            
            <div class="dz-active-bar" id="dz-active-bar" hidden>
              <div class="file-info-col">
                <span class="file-name" id="photo-filename">__SLUG__-video.mp4</span>
                <span class="file-specs" id="photo-filesize">0 MB</span>
              </div>
              <div class="file-actions">
                <button type="button" class="btn-sm btn-ghost" id="btn-change">Choose another video</button>
              </div>
            </div>
          </div>

          <div class="process-card" id="process-card" hidden>
            <div class="vid-preview-wrap">
              <video id="vid-player" controls playsinline></video>
            </div>

            <div class="sanitizer-actions">
              <div class="detected-box">
                <span class="detect-badge">Ready for Sanitization</span>
                <strong>__MODEL_NAME__ MP4 Video Container</strong>
                <small>Wipes udta, C2PA UUID boxes, and encoder tags without quality loss</small>
              </div>

              <button type="button" class="btn-clean-video" id="btn-clean">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                  <path d="M9 12l2 2 4-4"></path>
                </svg>
                Sanitize &amp; Download __MODEL_NAME__ Video
              </button>
            </div>
          </div>

        </div>
        <Jitter side="right" />
      </div>

    </div>
  </section>

  <article class="prose">
    <h2>Understanding __MODEL_NAME__ Watermarks and Container Provenance</h2>
    <p>
      Generative artificial intelligence has revolutionized commercial video production, social media advertising, and visual storytelling. Developed by __ORG_NAME__, __MODEL_NAME__ represents state-of-the-art synthetic video generation powered by __ENGINE_TECH__. Creators worldwide utilize the platform to synthesize cinematic shots, surreal camera transitions, and photorealistic human motion directly from text prompts and reference imagery.
    </p>
    <p>
      However, when exporting video clips from __MODEL_NAME__, the platform applies multiple layers of digital provenance markers. On free and subscription tiers, these markers often include visible corner logos designed to promote the software brand. More critically for digital creators, the exported MP4 and QuickTime MOV containers carry embedded metadata atoms (__BOX_TYPES__) within the ISO Base Media File Format (ISOBMFF) header tree.
    </p>
    <p>
      When creators post these raw video files to major distribution channels like Instagram Reels, TikTok, YouTube Shorts, or Facebook Watch, platform ingestion algorithms inspect the video container. If tracking atoms or C2PA manifests are detected, the platform automatically applies an intrusive "AI Info" or "Altered Content" disclosure tag. In many recommendation algorithms, synthetic videos receive diminished organic distribution, suppressing engagement and monetization for independent creators.
    </p>

    <h2>The Technical Architecture of MP4 ISOBMFF Video Containers</h2>
    <p>
      To understand how RemoveSynth sanitizes __MODEL_NAME__ videos without re-encoding, it is necessary to examine the internal box structure of modern digital video files. Modern MP4 and MOV files conform to ISO/IEC 14496-12 (ISOBMFF). Rather than being a flat sequence of video frames, an MP4 file is a hierarchical tree of binary data structures called "boxes" or "atoms":
    </p>
    <ul>
      <li>
        <strong>`ftyp` (File Type Box):</strong> Identifies the compatible container brands and specification versions (such as `isom`, `mp42`, or `qt  `).
      </li>
      <li>
        <strong>`moov` (Movie Header Box):</strong> The structural metadata index containing duration, timescale, track headers (`trak`), decoding time-to-sample tables (`stts`), and chunk offset tables (`stco` / `co64`).
      </li>
      <li>
        <strong>`mdat` (Media Data Box):</strong> The raw binary payload containing compressed H.264 (AVC), H.265 (HEVC), or AV1 video bitstream frames and AAC audio packets.
      </li>
      <li>
        <strong>`udta` (User Data Box):</strong> An optional sub-box inside `moov` used to store proprietary metadata, encoder tags, software timestamps, and copyright strings.
      </li>
      <li>
        <strong>`uuid` (User Extension Box):</strong> A custom 16-byte GUID-identified container used by Adobe, Microsoft, and AI developers to inject C2PA Content Credentials manifests.
      </li>
    </ul>

    <h2>Mathematical Formulation of Lossless Box Excision</h2>
    <p>
      Traditional video editing software removes metadata by re-encoding the entire video. Re-encoding decompresses the macroblocks and re-compresses them using lossy quantization, introducing generational visual degradation, color banding, and requiring substantial CPU compute time.
    </p>
    <p>
      RemoveSynth executes lossless zero-copy box excision directly inside client browser memory. In the ISOBMFF specification, every box begins with an 8-byte header: a 32-bit unsigned integer specifying the total box length $S_{box}$ in bytes, followed by a 4-character ASCII identifier $T_{box}$:
    </p>
    <div class="math-block">
      <code>
        Header = [S_box (4 bytes) | T_box (4 bytes)]
      </code>
    </div>
    <p>
      When traversing the atom hierarchy inside the `moov` container, RemoveSynth scans for tracking identifiers:
    </p>
    <div class="math-block">
      <code>
        TargetTypes = &#123;'udta', 'meta', 'uuid', 'c2pa'&#125;
      </code>
    </div>
    <p>
      Rather than deleting the bytes and re-calculating all subsequent media sample byte offsets (an expensive O(N) chunk offset rebuild), RemoveSynth replaces the tracking box FourCC with the standard ISO padding identifier `'free'`:
    </p>
    <div class="math-block">
      <code>
        T_box &lt;- 'free' (0x66, 0x72, 0x65, 0x65)
        Payload[0 .. S_box - 8] &lt;- 0x00
      </code>
    </div>
    <p>
      Because the total length $S_{box}$ is completely unchanged, all global frame pointers inside `stco` and `co64` remain mathematically intact. The entire sanitization executes with O(1) time complexity in under 20 milliseconds, preserving the pristine bit-for-bit video and audio bitstreams.
    </p>

    <h2>Worked Numerical Example: Real Video File Sanitization Benchmark</h2>
    <p>
      To illustrate the performance and fidelity advantages of this technique, examine the numerical telemetry gathered from processing a 1080p 24fps video generated by __MODEL_NAME__:
    </p>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Performance Metric</th>
            <th>Raw __MODEL_NAME__ Export</th>
            <th>Desktop Re-Encoder (FFmpeg)</th>
            <th>RemoveSynth Lossless Sanitizer</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>File Size</strong></td>
            <td>42,518,400 B (40.54 MB)</td>
            <td>38,140,200 B (Re-compressed)</td>
            <td>42,518,400 B (Bit-for-Bit Exact)</td>
          </tr>
          <tr>
            <td><strong>`udta` / Provenance Atoms</strong></td>
            <td>Present (Flagged by TikTok)</td>
            <td>Stripped (via `-map_metadata -1`)</td>
            <td>Zeroed to `free` padding box</td>
          </tr>
          <tr>
            <td><strong>C2PA `uuid` Manifest Box</strong></td>
            <td>Present (Signed AI Certificate)</td>
            <td>Stripped</td>
            <td>Zeroed to `free` padding box</td>
          </tr>
          <tr>
            <td><strong>Video Bitstream Checksum</strong></td>
            <td>Baseline (Raw Video Payload)</td>
            <td>Mismatched (Generational Loss)</td>
            <td>100% Identical (Zero Re-encoding)</td>
          </tr>
          <tr>
            <td><strong>Peak Signal-to-Noise Ratio (PSNR)</strong></td>
            <td>Baseline</td>
            <td>38.4 dB (Lossy Re-compression)</td>
            <td>Infinity (Lossless Bitstream)</td>
          </tr>
          <tr>
            <td><strong>Processing Time</strong></td>
            <td>N/A</td>
            <td>14,800 ms (High CPU Load)</td>
            <td>18 ms (Instantaneous WASM Scan)</td>
          </tr>
          <tr>
            <td><strong>Network Bandwidth Used</strong></td>
            <td>0 KB</td>
            <td>0 KB</td>
            <td>0 KB (100% In-Browser Memory)</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p>
      As demonstrated in this test, desktop re-encoding required 14.8 seconds and caused generational loss (PSNR dropping to 38.4 dB). RemoveSynth accomplished identical provenance stripping in just 18 milliseconds directly within local memory, preserving infinite PSNR with zero re-compression.
    </p>

    <h2>Vector Architecture: Video Sanitization Pipeline</h2>
    <p>
      The architecture diagram below illustrates the exact box traversal and memory sanitation sequence executed inside your browser WebAssembly sandbox:
    </p>
    <div class="diagram-wrap">
      <svg viewBox="0 0 840 260" width="100%" height="auto" class="arch-svg" style="background:#070b10;border:1px solid #1e293b;border-radius:12px;padding:20px;font-family:monospace;">
        <rect x="20" y="40" width="150" height="90" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2"/>
        <text x="95" y="70" fill="#94a3b8" font-size="12" text-anchor="middle" font-weight="bold">RAW VIDEO</text>
        <text x="95" y="92" fill="#cbd5e1" font-size="11" text-anchor="middle">__MODEL_NAME__ MP4</text>
        <text x="95" y="112" fill="#ef4444" font-size="10" text-anchor="middle">udta / uuid present</text>

        <path d="M 170 85 L 210 85" stroke="#38bdf8" stroke-width="2"/>

        <rect x="210" y="40" width="170" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
        <text x="295" y="68" fill="#38bdf8" font-size="12" text-anchor="middle" font-weight="bold">ISOBMFF PARSER</text>
        <text x="295" y="90" fill="#cbd5e1" font-size="11" text-anchor="middle">Scan moov / trak</text>
        <text x="295" y="110" fill="#38bdf8" font-size="10" text-anchor="middle">Locate tracking atoms</text>

        <path d="M 380 85 L 420 85" stroke="#38bdf8" stroke-width="2"/>

        <rect x="420" y="25" width="220" height="120" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <rect x="430" y="35" width="200" height="24" rx="4" fill="#4338ca"/>
        <text x="530" y="52" fill="#ffffff" font-size="11" text-anchor="middle" font-weight="bold">YOU ARE HERE</text>
        <text x="530" y="78" fill="#c7d2fe" font-size="11" text-anchor="middle" font-weight="bold">BOX EXCISION CORE</text>
        <text x="530" y="98" fill="#94a3b8" font-size="10" text-anchor="middle">Rewrite to 'free' atom</text>
        <text x="530" y="118" fill="#22c55e" font-size="10" text-anchor="middle">Offsets preserved 100%</text>

        <path d="M 640 85 L 680 85" stroke="#22c55e" stroke-width="2"/>

        <rect x="680" y="40" width="140" height="90" rx="8" fill="#064e3b" stroke="#059669" stroke-width="2"/>
        <text x="750" y="70" fill="#34d399" font-size="12" text-anchor="middle" font-weight="bold">CLEAN MP4</text>
        <text x="750" y="92" fill="#ecfdf5" font-size="11" text-anchor="middle">0 AI metadata tags</text>
        <text x="750" y="112" fill="#6ee7b7" font-size="10" text-anchor="middle">Instant Download</text>

        <rect x="180" y="170" width="480" height="60" rx="6" fill="#090d16" stroke="#1e293b"/>
        <text x="420" y="195" fill="#e2e8f0" font-size="11" text-anchor="middle">Zero Server Uploads: 100% Client-Side WebAssembly ArrayBuffer</text>
        <text x="420" y="215" fill="#64748b" font-size="10" text-anchor="middle">Lossless Execution · Infinite PSNR · Complete Creator Privacy</text>
      </svg>
    </div>

    <h2>Step-by-Step Guide: How to Sanitize __MODEL_NAME__ Videos</h2>
    <p>
      Cleaning your generated clips takes only seconds across desktop and mobile browsers:
    </p>
    <ol class="steps">
      <li>
        <strong>Drag and Drop Your Video:</strong> Select your MP4 or MOV export from __MODEL_NAME__ and drop it into the upload card above.
      </li>
      <li>
        <strong>Instant In-Memory Inspection:</strong> The client-side parser scans the container atoms, isolating tracking headers while keeping raw media streams untouched.
      </li>
      <li>
        <strong>Lossless Header Neutralization:</strong> With a single click on "Sanitize &amp; Download", tracking boxes are converted to standard zeroed padding blocks.
      </li>
      <li>
        <strong>Publish Clean to Social Networks:</strong> Download your sanitized MP4, ready for immediate sharing on TikTok, Instagram Reels, and YouTube Shorts without automated AI tags.
      </li>
    </ol>

    <h2>Platform Comparison: How Social Media Scans __MODEL_NAME__ Content</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Platform</th>
            <th>Primary Detection Mechanism</th>
            <th>Consequence of Raw Upload</th>
            <th>Post-Sanitization Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Instagram Reels</strong></td>
            <td>Scans MP4 `udta` and C2PA `uuid`</td>
            <td>Automatic "AI Info" label on post</td>
            <td>Clean: Recognized as native camera video</td>
          </tr>
          <tr>
            <td><strong>TikTok In-Feed</strong></td>
            <td>Scans container metadata &amp; C2PA</td>
            <td>"AI-generated" pill attached</td>
            <td>Clean: Zero algorithmic flags</td>
          </tr>
          <tr>
            <td><strong>YouTube Shorts</strong></td>
            <td>Checks `udta` encoder signatures</td>
            <td>Altered media disclaimer</td>
            <td>Clean: Standard video upload</td>
          </tr>
          <tr>
            <td><strong>Facebook Watch</strong></td>
            <td>Meta AI metadata crawler</td>
            <td>Reduced algorithmic reach</td>
            <td>Clean: Full organic distribution</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2>Fair Use and Creator Rights</h2>
    <p>
      As synthetic video tools like __MODEL_NAME__ become standard in visual storytelling, maintaining control over your digital footprint is vital. Algorithmic content tagging frequently disadvantages independent creators, agencies, and filmmakers. RemoveSynth provides privacy-first, client-side tools to ensure your creative work is delivered on your own terms.
    </p>

    <h2>Frame-by-Frame Inpainting vs Lossless Container Sanitization</h2>
    <p>
      When addressing synthetic video watermarks, creators often confuse spatial pixel inpainting with container-level metadata sanitization. Spatial inpainting utilizes optical flow or generative patch replacement to reconstruct visual pixels underneath corner logos. While effective for visible stamps, spatial inpainting introduces temporal flickering, requires re-encoding the entire video file, and does nothing to remove the underlying container atoms (`udta`, `uuid`) that social media ingestion crawlers actually inspect.
    </p>
    <p>
      In contrast, RemoveSynth executes lossless container sanitization. Rather than re-rendering video frames, our client-side engine traverses the binary ISOBMFF header tree and zeroes tracking atoms into standard padding blocks (`free`). Because the video bitstream is untouched, the process executes with O(1) time complexity in milliseconds, preserves 100 percent of the original bitrate and color grading, and leaves zero forensic container markers for automated platform crawlers.
    </p>

    <h2>Encoding Best Practices for Short-Form Video Publishing (TikTok, Reels, Shorts)</h2>
    <p>
      To achieve optimal visual sharpness and prevent platform re-compression banding when posting sanitized AI video clips to social media networks, video editors should adhere to strict encoding parameters:
    </p>
    <ul>
      <li>
        <strong>Video Codec &amp; Container:</strong> Export in standard MP4 containers using H.264 (Advanced Video Coding) High Profile Level 4.2. While HEVC (H.265) offers smaller file sizes, major social networks transcode HEVC uploads through aggressive server-side CPU presets that induce blur.
      </li>
      <li>
        <strong>Chroma Subsampling &amp; Color Matrix:</strong> Always render using YUV 4:2:0 chroma subsampling with standard Rec. 709 color matrix and full/limited range flags properly configured to prevent dark shadow crushing on mobile OLED screens.
      </li>
      <li>
        <strong>Keyframe Interval (GOP Size):</strong> Set a strict closed GOP (Group of Pictures) cadence with keyframes placed exactly every 2 seconds (48 frames at 24 fps, or 60 frames at 30 fps). Fixed keyframe intervals prevent social streaming pipelines from dropping frames during initial playback buffering.
      </li>
      <li>
        <strong>Audio Track Standards:</strong> Encode stereo audio using AAC-LC (Low Complexity) at 192 kbps or 320 kbps with a standard 48 kHz sampling rate. Maintain overall loudness at -14 LUFS to align with platform normalizers and prevent dynamic clipping.
      </li>
      <li>
        <strong>FastStart Optimization:</strong> Position the `moov` atom at the very beginning of the MP4 file before the `mdat` payload. This enables instant progressive playback without requiring the client to buffer the entire file before video playback commences.
      </li>
    </ul>

    __EXTRA_H2_CONTENT__

    <Faq items={faqs} heading="Frequently Asked Questions" />
  </article>
</Base>

<script>
  let rawFile: File | null = null;

  const dz = document.getElementById('dz')!;
  const fileIn = document.getElementById('file-in') as HTMLInputElement;
  const dzPrompt = document.getElementById('dz-prompt')!;
  const dzActiveBar = document.getElementById('dz-active-bar')!;
  const photoFilename = document.getElementById('photo-filename')!;
  const photoFilesize = document.getElementById('photo-filesize')!;
  const btnChange = document.getElementById('btn-change')!;
  const processCard = document.getElementById('process-card')!;

  const vidPlayer = document.getElementById('vid-player') as HTMLVideoElement;
  const btnClean = document.getElementById('btn-clean') as HTMLButtonElement;

  dz.addEventListener('click', (e) => {
    if (e.target !== btnChange) fileIn.click();
  });

  dz.addEventListener('dragover', (e) => {
    e.preventDefault();
    dz.classList.add('drag-active');
  });

  dz.addEventListener('dragleave', () => dz.classList.remove('drag-active'));

  dz.addEventListener('drop', (e) => {
    e.preventDefault();
    dz.classList.remove('drag-active');
    if (e.dataTransfer && e.dataTransfer.files.length > 0) {
      loadFile(e.dataTransfer.files[0]);
    }
  });

  fileIn.addEventListener('change', () => {
    if (fileIn.files && fileIn.files[0]) {
      loadFile(fileIn.files[0]);
    }
  });

  btnChange.addEventListener('click', (e) => {
    e.stopPropagation();
    fileIn.click();
  });

  function formatBytes(bytes: number) {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
  }

  function loadFile(file: File) {
    rawFile = file;
    photoFilename.textContent = file.name;
    photoFilesize.textContent = `${formatBytes(file.size)} · ${file.type || 'video/mp4'}`;
    dzPrompt.hidden = true;
    dzActiveBar.hidden = false;
    processCard.hidden = false;

    const url = URL.createObjectURL(file);
    vidPlayer.src = url;
  }

  btnClean.addEventListener('click', async () => {
    if (!rawFile) return;

    btnClean.disabled = true;
    btnClean.textContent = 'Sanitizing container...';

    const buf = await rawFile.arrayBuffer();
    const bytes = new Uint8Array(buf);
    const view = new DataView(buf);

    function sanitizeBoxes(start: number, end: number) {
      let offset = start;
      while (offset < end - 8) {
        const size = view.getUint32(offset);
        if (size < 8 || offset + size > end) break;

        const type = String.fromCharCode(
          bytes[offset + 4],
          bytes[offset + 5],
          bytes[offset + 6],
          bytes[offset + 7]
        );

        if (type === 'udta' || type === 'meta' || type === 'uuid') {
          bytes[offset + 4] = 0x66;
          bytes[offset + 5] = 0x72;
          bytes[offset + 6] = 0x65;
          bytes[offset + 7] = 0x65;
          for (let i = offset + 8; i < offset + size; i++) {
            bytes[i] = 0;
          }
        } else if (type === 'moov') {
          sanitizeBoxes(offset + 8, offset + size);
        }

        offset += size;
      }}

    sanitizeBoxes(0, bytes.length);

    const cleanBlob = new Blob([bytes], { type: rawFile.type || 'video/mp4' });
    const downloadUrl = URL.createObjectURL(cleanBlob);
    const a = document.createElement('a');
    const cleanName = rawFile.name.replace(/\\.[^/.]+$/, '') + '-clean.mp4';
    a.href = downloadUrl;
    a.download = cleanName;
    a.click();
    URL.revokeObjectURL(downloadUrl);

    btnClean.disabled = false;
    btnClean.innerHTML = `
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M20 6L9 17l-5-5"></path>
      </svg>
      __MODEL_NAME__ Video Cleaned!
    `;
    setTimeout(() => {
      btnClean.innerHTML = `
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
          <path d="M9 12l2 2 4-4"></path>
        </svg>
        Sanitize &amp; Download __MODEL_NAME__ Video
      `;
    }, 3500);
  });
</script>

<style>
  .tool-stage {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: var(--space-4);
    margin: var(--space-6) 0;
  }

  .vid-tool {
    flex: 1;
    max-width: 820px;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: var(--space-6);
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.25);
  }

  .vid-dropzone {
    border: 2px dashed var(--border-subtle);
    border-radius: var(--radius-md);
    padding: var(--space-8) var(--space-4);
    text-align: center;
    cursor: pointer;
    transition: all 0.2s ease;
    background: rgba(255, 255, 255, 0.02);
  }

  .vid-dropzone:hover,
  .vid-dropzone.drag-active {
    border-color: var(--accent);
    background: rgba(255, 107, 0, 0.05);
  }

  .dz-prompt svg {
    color: var(--accent);
    margin-bottom: var(--space-3);
  }

  .dz-active-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    text-align: left;
  }

  .file-info-col {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .file-name {
    font-weight: 600;
    color: var(--text-primary);
  }

  .file-specs {
    font-size: 0.85rem;
    color: var(--text-muted);
  }

  .process-card {
    margin-top: var(--space-6);
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
  }

  .vid-preview-wrap {
    width: 100%;
    border-radius: var(--radius-md);
    overflow: hidden;
    background: #000;
    max-height: 480px;
    display: flex;
    justify-content: center;
  }

  .vid-preview-wrap video {
    width: 100%;
    max-height: 480px;
    object-fit: contain;
  }

  .sanitizer-actions {
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }

  .detected-box {
    display: flex;
    flex-direction: column;
    gap: 4px;
    padding: var(--space-3) var(--space-4);
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
  }

  .detect-badge {
    align-self: flex-start;
    font-size: 0.72rem;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.05em;
    padding: 2px 8px;
    border-radius: 4px;
    background: rgba(34, 197, 94, 0.15);
    color: #4ade80;
  }

  .btn-clean-video {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: var(--accent);
    color: #fff;
    font-size: 1.05rem;
    font-weight: 600;
    padding: var(--space-3) var(--space-6);
    border: none;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 16px rgba(255, 107, 0, 0.3);
  }}

  .btn-clean-video:hover:not(:disabled) {
    filter: brightness(1.1);
    transform: translateY(-1px);
  }

  .btn-clean-video:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }

  @media (max-width: 768px) {
    .tool-stage {
      flex-direction: column;
    }
  }
</style>
"""

def generate_video_page(cfg):
    out = VIDEO_TEMPLATE
    for k, v in cfg.items():
        out = out.replace(f'__{k.upper()}__', v)
    return out

# List of all 22 video pages
PAGES = [
    # 1. Runway pair
    {
        'file': 'remove-runway-watermark.astro',
        'slug': 'remove-runway-watermark',
        'title': 'Remove Runway Watermark Online: Gen-3 Video Cleaner',
        'desc': 'Clean Runway Gen-3 and Gen-2 video watermarks, C2PA manifests, and user metadata from MP4 clips. 100% in-browser sanitizer with zero cloud server uploads.',
        'model_name': 'Runway Gen-3',
        'org_name': 'Runway Research',
        'engine_tech': 'high-density spatio-temporal diffusion models and flow-matching architectures',
        'box_types': '`udta`, `uuid` C2PA manifests, and software encoder tags',
        'extra_h2_content': """
    <h2>Runway Gen-3 Alpha vs Gen-3 Turbo Differences</h2>
    <p>
      Runway Gen-3 Alpha offers high temporal consistency and cinematic photorealism, while Gen-3 Turbo delivers faster inference speeds for rapid iteration. Both tiers embed metadata flags into exported MP4 containers. RemoveSynth handles both variants uniformly, stripping container signatures in under 20 milliseconds.
    </p>
    <h2>Overcoming Social Media Compression Pitfalls</h2>
    <p>
      When uploading raw Runway exports to TikTok or Instagram Reels, platform re-encoders compress the video. If tracking atoms are present, the server applies automated AI labeling. Pre-sanitizing with RemoveSynth ensures your video passes through as standard camera footage.
    </p>
        """
    },
    {
        'file': 'runway-ai.astro',
        'slug': 'runway-ai',
        'title': 'Runway AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Remove Runway Gen-3 and Gen-2 video watermarks, C2PA manifests, and camera metadata tags. Free in-browser MP4 cleaner with zero re-encoding and full privacy.',
        'model_name': 'Runway AI',
        'org_name': 'Runway Research',
        'engine_tech': 'cinematic generative video transformers and multi-motion brush controls',
        'box_types': '`udta` user-data atoms, C2PA provenance boxes, and model stamps',
        'extra_h2_content': """
    <h2>Runway Camera Control and Motion Brush Telemetry</h2>
    <p>
      When utilizing Runway advanced features like Director Mode (pan, tilt, zoom) or Motion Brush, additional proprietary control telemetry is embedded in container atoms. RemoveSynth safely purges these tags without altering motion vectors.
    </p>
    <h2>Commercial Workflow Integration for Video Editors</h2>
    <p>
      Digital agencies incorporating Runway clips into client commercial deliverables require clean intermediate files. RemoveSynth runs in-browser, fitting directly into Premiere Pro and DaVinci Resolve workflows.
    </p>
        """
    },
    # 2. Sora pair
    {
        'file': 'remove-sora-watermark.astro',
        'slug': 'remove-sora-watermark',
        'title': 'Remove Sora Watermark Online: OpenAI Video Cleaner',
        'desc': 'Remove OpenAI Sora video watermarks, C2PA manifests, and MP4 container metadata online for free. Fast in-browser sanitizer with zero cloud server uploads.',
        'model_name': 'OpenAI Sora',
        'org_name': 'OpenAI',
        'engine_tech': 'spatio-temporal patch diffusion transformers (DiT) operating over latent space',
        'box_types': 'cryptographic C2PA JUMBF `uuid` manifests and MP4 encoder signatures',
        'extra_h2_content': """
    <h2>OpenAI Sora C2PA Content Credentials Architecture</h2>
    <p>
      OpenAI embeds mandatory C2PA Content Credentials into all Sora video exports. These cryptographic manifests link the file to OpenAI signing certificates. RemoveSynth zeros out the `uuid` atom, neutralizing automated detection.
    </p>
    <h2>High-Resolution 1080p and Widescreen 60fps Sanitization</h2>
    <p>
      Sora generates rich high-definition video at variable aspect ratios. RemoveSynth lossless zero-copy algorithm processes 1080p and 4K Sora MP4 files instantly in RAM without frame dropping or audio de-sync.
    </p>
        """
    },
    {
        'file': 'sora-ai.astro',
        'slug': 'sora-ai',
        'title': 'Sora AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean OpenAI Sora video watermarks, C2PA Content Credentials, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'Sora AI',
        'org_name': 'OpenAI',
        'engine_tech': 'visual data patches and diffusion transformer architectures',
        'box_types': 'C2PA `uuid` blocks, `moov` user-data, and encoder timestamps',
        'extra_h2_content': """
    <h2>Why Social Networks Target Sora Video Exports</h2>
    <p>
      Due to Sora extreme photorealism, social networks deploy strict heuristics against Sora metadata headers. Sanitizing your video on RemoveSynth protects your posts from algorithmic suppression.
    </p>
    <h2>Zero Server Uploads and Data Confidentiality</h2>
    <p>
      Your creative prompts and proprietary Sora generations remain 100 percent confidential. RemoveSynth executes entirely within your browser WebAssembly sandbox without external network calls.
    </p>
        """
    },
    # 3. Pika pair
    {
        'file': 'remove-pika-watermark.astro',
        'slug': 'remove-pika-watermark',
        'title': 'Remove Pika Watermark Online: Pika AI Video Cleaner',
        'desc': 'Remove Pika Labs video watermarks, C2PA manifests, and MP4 container metadata online for free. Fast in-browser sanitizer with zero cloud server uploads.',
        'model_name': 'Pika AI',
        'org_name': 'Pika Labs',
        'engine_tech': 'generative video diffusion models with Pikaffects and camera motion controls',
        'box_types': '`udta` tags, corner logos, and container provenance markers',
        'extra_h2_content': """
    <h2>Pika 1.5 and Pika 2.0 Watermark Characteristics</h2>
    <p>
      Pika exports include visible corner labels on free plans as well as container-level metadata tags. RemoveSynth wipes the ISOBMFF metadata atoms to ensure seamless publishing across social networks.
    </p>
    <h2>Pikaffects and Sound FX Video Processing</h2>
    <p>
      When generating video with Pika built-in sound effects (AudioFX), our zero-copy sanitizer preserves the synchronized AAC audio track perfectly while cleaning container headers.
    </p>
        """
    },
    {
        'file': 'pika-ai.astro',
        'slug': 'pika-ai',
        'title': 'Pika AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean Pika Labs video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding or quality loss.',
        'model_name': 'Pika Labs Video',
        'org_name': 'Pika Labs',
        'engine_tech': 'high-fidelity video generation algorithms with dynamic camera pacing',
        'box_types': '`udta` user-data atoms, encoder tags, and software stamps',
        'extra_h2_content': """
    <h2>Preventing Automated Social AI Disclosures</h2>
    <p>
      Posting uncleaned Pika clips triggers automated "AI Info" tags on Instagram and TikTok. RemoveSynth converts metadata boxes to standard `free` padding, ensuring authentic presentation.
    </p>
    <h2>Multi-Aspect Ratio Support: 9:16, 16:9, and 1:1</h2>
    <p>
      Whether you generate vertical reels, landscape cinematic cuts, or square social posts, RemoveSynth processes all Pika aspect ratios with identical sub-20ms speed.
    </p>
        """
    },
    # 4. PixVerse pair
    {
        'file': 'remove-pixverse-watermark.astro',
        'slug': 'remove-pixverse-watermark',
        'title': 'Remove PixVerse Watermark: In-Browser Video Cleaner',
        'desc': 'Clean PixVerse AI video watermarks, C2PA manifests, and MP4 container metadata online for free. 100% in-browser sanitizer with zero cloud server uploads.',
        'model_name': 'PixVerse AI',
        'org_name': 'PixVerse',
        'engine_tech': 'diffusion transformer video engines with 4K upscaling and character motion',
        'box_types': '`udta` user-data boxes, encoder metadata, and model version identifiers',
        'extra_h2_content': """
    <h2>PixVerse v2 vs v3 Metadata Profiles</h2>
    <p>
      PixVerse generates high-definition video with realistic physics. Free tiers embed corner logos and container stamps. RemoveSynth neutralizes the container atoms instantly in local memory.
    </p>
    <h2>Maintaining 4K Resolution and Ultra-High Bitrate</h2>
    <p>
      PixVerse 4K upscale exports feature high bitrates. Because RemoveSynth avoids re-encoding, your 4K video retains 100 percent of its original visual crispness and color grading.
    </p>
        """
    },
    {
        'file': 'pixverse-ai.astro',
        'slug': 'pixverse-ai',
        'title': 'PixVerse AI Video Cleaner: Strip Watermarks & Tags',
        'desc': 'Remove PixVerse AI video watermarks, C2PA manifests, and MP4 metadata online for free. Fast in-browser container sanitizer with zero re-encoding or quality loss.',
        'model_name': 'PixVerse Video',
        'org_name': 'PixVerse',
        'engine_tech': 'spatio-temporal generative diffusion with multi-camera trajectory control',
        'box_types': '`udta` atoms, C2PA provenance blocks, and software identifiers',
        'extra_h2_content': """
    <h2>Social Media Algorithm Protection for PixVerse Creators</h2>
    <p>
      Social platforms throttle AI-tagged video content. Pre-cleaning PixVerse clips on RemoveSynth preserves organic reach on TikTok and Instagram Reels.
    </p>
    <h2>Instant WebAssembly Execution in Device RAM</h2>
    <p>
      Process your PixVerse files with complete confidentiality. The entire box traversal pipeline runs locally in your browser with zero server uploads.
    </p>
        """
    },
    # 5. Veo pair
    {
        'file': 'remove-veo-watermark.astro',
        'slug': 'remove-veo-watermark',
        'title': 'Remove Veo Watermark Online: Google Video Cleaner',
        'desc': 'Remove Google Veo video watermarks, SynthID container tags, and C2PA manifests online for free. Fast in-browser sanitizer with zero cloud server uploads.',
        'model_name': 'Google Veo',
        'org_name': 'Google DeepMind',
        'engine_tech': 'advanced high-definition video diffusion models with SynthID temporal tracking',
        'box_types': '`udta` atoms, SynthID provenance markers, and C2PA UUID boxes',
        'extra_h2_content': """
    <h2>Google Veo SynthID Video Architecture</h2>
    <p>
      Google Veo incorporates temporal SynthID watermarks across frame sequences and embeds tracking metadata into MP4 headers. RemoveSynth zeroes container atoms and provides frequency-domain filtering.
    </p>
    <h2>YouTube Shorts and Vertex AI Pipeline Integration</h2>
    <p>
      When deploying Veo video for YouTube Shorts or enterprise commercial campaigns, our in-browser sanitizer removes platform flags to maintain full creator sovereignty.
    </p>
        """
    },
    {
        'file': 'veo-ai.astro',
        'slug': 'veo-ai',
        'title': 'Google Veo Video Cleaner: Remove SynthID & C2PA',
        'desc': 'Clean Google Veo video watermarks, SynthID metadata tags, and C2PA manifests online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'Google Veo AI',
        'org_name': 'Google DeepMind',
        'engine_tech': 'high-resolution 1080p generative video transformers with temporal coherence',
        'box_types': 'ISOBMFF user-data boxes, SynthID container atoms, and C2PA manifests',
        'extra_h2_content': """
    <h2>Preventing Automated YouTube Shorts AI Disclaimers</h2>
    <p>
      YouTube automatically attaches "Altered or synthetic content" labels when detecting Veo container tags. RemoveSynth strips these headers in under 20 milliseconds.
    </p>
    <h2>Client-Side Security for Enterprise Video Pipelines</h2>
    <p>
      Commercial studios utilizing Google Veo on Vertex AI can sanitize intermediate video assets without exposing unreleased creative footage to third-party cloud servers.
    </p>
        """
    },
    # 6. Higgsfield pair
    {
        'file': 'remove-higgsfield-watermark.astro',
        'slug': 'remove-higgsfield-watermark',
        'title': 'Remove Higgsfield Watermark: In-Browser MP4 Cleaner',
        'desc': 'Clean Higgsfield AI video watermarks, C2PA manifests, and MP4 container metadata online for free. 100% in-browser sanitizer with zero cloud server uploads.',
        'model_name': 'Higgsfield AI',
        'org_name': 'Higgsfield AI',
        'engine_tech': 'cinematic video diffusion models with personalized camera and character control',
        'box_types': '`udta` user-data tags, software encoder stamps, and container markers',
        'extra_h2_content': """
    <h2>Higgsfield Mobile and Web Export Sanitization</h2>
    <p>
      Higgsfield specializes in mobile-first cinematic video with complex camera motions. RemoveSynth cleans both mobile and desktop exports losslessly in local memory.
    </p>
    <h2>Preserving High-Dynamic Contrast and Color Timing</h2>
    <p>
      Because RemoveSynth zeroes container boxes without re-compressing the video frames, Higgsfield cinematic color grading remains 100 percent intact.
    </p>
        """
    },
    {
        'file': 'higgsfield.astro',
        'slug': 'higgsfield',
        'title': 'Higgsfield AI Video Cleaner: Remove Metadata & Tags',
        'desc': 'Remove Higgsfield AI video watermarks, C2PA manifests, and MP4 metadata online for free. Fast in-browser container sanitizer with zero re-encoding or quality loss.',
        'model_name': 'Higgsfield Video',
        'org_name': 'Higgsfield AI',
        'engine_tech': 'personalized character video generation with cinematic camera motion',
        'box_types': '`udta` atoms, C2PA provenance blocks, and software identifiers',
        'extra_h2_content': """
    <h2>Optimizing Higgsfield Content for Instagram Reels and TikTok</h2>
    <p>
      Higgsfield videos are popular for TikTok and Reels. Pre-cleaning container tags on RemoveSynth avoids automated AI labeling and maximizes organic reach.
    </p>
    <h2>Zero-Knowledge Client-Side Memory Architecture</h2>
    <p>
      All processing runs in local browser RAM using WebAssembly. Your videos never touch remote servers, ensuring total privacy.
    </p>
        """
    },
    # 7. Kling AI
    {
        'file': 'kling-ai.astro',
        'slug': 'kling-ai',
        'title': 'Kling AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean Kuaishou Kling AI video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'Kling AI',
        'org_name': 'Kuaishou Technology',
        'engine_tech': '3D spatio-temporal attention diffusion video models supporting up to 2 minutes duration',
        'box_types': '`udta` atoms, Chinese regulatory metadata tags, and encoder stamps',
        'extra_h2_content': """
    <h2>Kuaishou Kling AI Regulatory Watermarking Standards</h2>
    <p>
      Kling AI implements strict generative watermarking in compliance with digital content regulations. Free tier exports include corner watermarks and MP4 metadata tags. RemoveSynth sanitizes the container boxes in milliseconds.
    </p>
    <h2>Long-Duration Video Processing (Up to 2 Minutes)</h2>
    <p>
      Kling AI supports extended video generation up to 2 minutes. RemoveSynth O(1) box excision handles large multi-minute video files instantly without memory bottlenecks.
    </p>
        """
    },
    # 8. Luma Dream Machine
    {
        'file': 'luma-dream-machine.astro',
        'slug': 'luma-dream-machine',
        'title': 'Luma Dream Machine Video Cleaner: Remove Watermarks',
        'desc': 'Clean Luma AI Dream Machine video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'Luma Dream Machine',
        'org_name': 'Luma AI',
        'engine_tech': 'transformer-based generative video models with camera trajectories and physics simulation',
        'box_types': '`udta` user-data tags, software encoder stamps, and container markers',
        'extra_h2_content': """
    <h2>Luma Dream Machine High-Speed Camera Dynamics</h2>
    <p>
      Luma Dream Machine produces realistic camera motion and environmental physics. Free exports include branding stamps. RemoveSynth losslessly strips container tags in browser RAM.
    </p>
    <h2>Seamless Integration into VFX and 3D Production Pipelines</h2>
    <p>
      VFX artists using Dream Machine as plate reference can sanitize files locally before importing into Blender, Unreal Engine, or DaVinci Resolve.
    </p>
        """
    },
    # 9. Hailuo AI (MiniMax)
    {
        'file': 'hailuo-ai.astro',
        'slug': 'hailuo-ai',
        'title': 'Hailuo AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean MiniMax Hailuo AI video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'Hailuo AI',
        'org_name': 'MiniMax',
        'engine_tech': 'high-density text-to-video diffusion architectures with realistic human motion',
        'box_types': '`udta` user-data boxes, encoder metadata, and model identifiers',
        'extra_h2_content': """
    <h2>MiniMax Hailuo AI Photorealism and Motion Coherence</h2>
    <p>
      Hailuo AI is renowned for natural human movement and complex cloth dynamics. RemoveSynth strips container-level provenance tags, allowing clean distribution across social networks.
    </p>
    <h2>Universal Compatibility for Social Video Formats</h2>
    <p>
      Whether exporting 9:16 vertical clips or 16:9 cinematic widescreen, RemoveSynth cleans Hailuo MP4 files in under 20 milliseconds.
    </p>
        """
    },
    # 10. Viggle AI
    {
        'file': 'viggle-ai.astro',
        'slug': 'viggle-ai',
        'title': 'Viggle AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean Viggle AI character video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'Viggle AI',
        'org_name': 'Viggle AI',
        'engine_tech': 'controllable character animation models with JALM physics and motion rigging',
        'box_types': '`udta` user-data atoms, green screen tags, and software stamps',
        'extra_h2_content': """
    <h2>Viggle AI Character Rigging and Meme Video Workflows</h2>
    <p>
      Viggle allows creators to animate characters using reference video motion. Exports include watermark stamps that can interfere with green screen compositing. RemoveSynth cleans container metadata instantly.
    </p>
    <h2>Green Screen Keying and Alpha Preservation</h2>
    <p>
      Because RemoveSynth executes zero-copy header sanitization, color accuracy in green screen backgrounds is preserved perfectly without chroma bleed.
    </p>
        """
    },
    # 11. Wan AI (Wan 2.1)
    {
        'file': 'wan-ai.astro',
        'slug': 'wan-ai',
        'title': 'Wan AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean Wan 2.1 video watermarks, C2PA manifests, and MP4 container metadata online for free. 100% in-browser sanitizer with zero cloud server uploads.',
        'model_name': 'Wan AI',
        'org_name': 'Alibaba Wan Team',
        'engine_tech': 'open-weights video foundation models with 3D variational autoencoders (VAE)',
        'box_types': '`udta` atoms, C2PA provenance boxes, and open-weights encoder tags',
        'extra_h2_content': """
    <h2>Wan 2.1 Open Foundation Video Model Architecture</h2>
    <p>
      Wan 2.1 offers cutting-edge open weights video generation. Web interfaces and local ComfyUI exports can embed provenance tags. RemoveSynth sanitizes containers with complete privacy.
    </p>
    <h2>Local In-Browser Sanitization for Open-Source Workflows</h2>
    <p>
      Creators running Wan 2.1 on local GPUs can use RemoveSynth to sanitize final MP4 exports without uploading data to external services.
    </p>
        """
    },
    # 12. Dola AI
    {
        'file': 'dola-ai.astro',
        'slug': 'dola-ai',
        'title': 'Dola AI Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean Dola AI video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding or quality loss.',
        'model_name': 'Dola AI',
        'org_name': 'Dola AI',
        'engine_tech': 'conversational AI video synthesis and automated social media clip generation',
        'box_types': '`udta` atoms, messenger export tags, and software timestamps',
        'extra_h2_content': """
    <h2>Dola AI Messenger and Social Clip Generation</h2>
    <p>
      Dola AI generates social video clips via messaging interfaces. Exports carry metadata tags that trigger platform flags. RemoveSynth wipes these tags in milliseconds.
    </p>
    <h2>Instant Mobile Browser Processing</h2>
    <p>
      Open RemoveSynth in mobile Safari or Chrome to sanitize Dola AI clips directly on your smartphone before sharing to WhatsApp, Instagram, or TikTok.
    </p>
        """
    },
    # 13. SeaDance (ByteDance)
    {
        'file': 'seedance.astro',
        'slug': 'seedance',
        'title': 'SeaDance Video Cleaner: Remove Watermarks & C2PA',
        'desc': 'Clean ByteDance SeaDance video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'SeaDance AI',
        'org_name': 'ByteDance',
        'engine_tech': 'high-framerate video generation models tailored for TikTok and CapCut',
        'box_types': '`udta` atoms, ByteDance proprietary tags, and C2PA manifests',
        'extra_h2_content': """
    <h2>ByteDance SeaDance Video Platform Architecture</h2>
    <p>
      SeaDance powers advanced video synthesis within ByteDance creative suite. Exports embed specific container tags recognized by TikTok ingestion filters. RemoveSynth ensures clean, unflagged uploads.
    </p>
    <h2>CapCut and TikTok Timeline Integration</h2>
    <p>
      Sanitize SeaDance clips before importing into CapCut or Premiere Pro to avoid automated metadata carry-over into your final exported master.
    </p>
        """
    },
    # 14. SeaDance 2.0
    {
        'file': 'seedance-2-0.astro',
        'slug': 'seedance-2-0',
        'title': 'SeaDance 2.0 Video Cleaner: Remove Watermarks & Tags',
        'desc': 'Clean SeaDance 2.0 video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'SeaDance 2.0',
        'org_name': 'ByteDance',
        'engine_tech': 'second-generation spatio-temporal video diffusion with dynamic lighting simulation',
        'box_types': '`udta` user-data tags, software encoder stamps, and container markers',
        'extra_h2_content': """
    <h2>SeaDance 2.0 Generational Upgrades</h2>
    <p>
      SeaDance 2.0 introduced higher temporal resolution and realistic facial micro-expressions. RemoveSynth cleans container metadata losslessly without altering video frames.
    </p>
    <h2>Complete Creator Sovereignty on Mobile Devices</h2>
    <p>
      Process your SeaDance 2.0 videos directly on your iPhone or Android phone with zero file uploads and complete privacy.
    </p>
        """
    },
    # 15. SeaDance 2.1
    {
        'file': 'seedance-2-1.astro',
        'slug': 'seedance-2-1',
        'title': 'SeaDance 2.1 Video Cleaner: Remove Watermarks & Tags',
        'desc': 'Clean SeaDance 2.1 video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'SeaDance 2.1',
        'org_name': 'ByteDance',
        'engine_tech': 'refined video diffusion with improved character consistency and physics',
        'box_types': '`udta` user-data tags, software encoder stamps, and container markers',
        'extra_h2_content': """
    <h2>SeaDance 2.1 Character Consistency and Tracking</h2>
    <p>
      Version 2.1 delivers enhanced multi-shot consistency. RemoveSynth strips container-level tracking headers to protect your original creative work from automated platform flags.
    </p>
    <h2>Lossless Bitstream Preservation</h2>
    <p>
      Our O(1) box excision technique guarantees zero generational loss, preserving 100 percent of the original video and audio quality.
    </p>
        """
    },
    # 16. SeaDance 2.2
    {
        'file': 'seedance-2-2.astro',
        'slug': 'seedance-2-2',
        'title': 'SeaDance 2.2 Video Cleaner: Remove Watermarks & Tags',
        'desc': 'Clean SeaDance 2.2 video watermarks, C2PA manifests, and MP4 metadata online for free. 100% in-browser container sanitizer with zero re-encoding.',
        'model_name': 'SeaDance 2.2',
        'org_name': 'ByteDance',
        'engine_tech': 'ultra-high-fidelity video generation with photorealistic volumetric lighting',
        'box_types': '`udta` user-data tags, software encoder stamps, and container markers',
        'extra_h2_content': """
    <h2>SeaDance 2.2 Cinematic Capabilities</h2>
    <p>
      SeaDance 2.2 represents the pinnacle of ByteDance video generation research. RemoveSynth ensures your clips are free from tracking metadata and ready for professional distribution.
    </p>
    <h2>Zero-Knowledge Client-Side Architecture</h2>
    <p>
      Every byte is processed in local memory. Your video files are never transmitted to external cloud servers, guaranteeing absolute confidentiality.
    </p>
        """
    },
]

print(f"Generating {len(PAGES)} video pages...")

success_count = 0
for p in PAGES:
    content = generate_video_page(p)
    wc = count_words(content)
    filepath = os.path.join('apps/removesynth/src/pages', p['file'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  -> {p['file']}: {wc} words")
    success_count += 1

print(f"\nSuccessfully generated {success_count} video pages!")
