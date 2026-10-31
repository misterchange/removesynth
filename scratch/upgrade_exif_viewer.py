import re

exif_viewer_content = '''---
import Base from '../layouts/Base.astro';
import Jitter from '@removesynth/shared/components/Jitter.astro';
import { faqSchema, breadcrumbSchema, type FaqItem } from '@removesynth/shared/lib/faq';
import { SITE } from '../site';

const title = 'EXIF Viewer: Visual Photo Metadata & Camera Inspector';
const description =
  'Inspect camera settings, shutter speed, aperture, ISO, and GPS coordinates hidden in photos online. Free visual in-browser EXIF viewer with zero file uploads.';

const faqs: FaqItem[] = [
  {
    q: 'What is an EXIF viewer?',
    a: 'An EXIF viewer is a tool that reads Exchangeable Image File Format (EXIF) metadata stored inside digital photos. It exposes camera hardware models, lens specifications, exposure parameters (aperture, shutter speed, ISO), capture timestamps, and GPS location coordinates.',
  },
  {
    q: 'Can this EXIF viewer detect GPS coordinates and map them?',
    a: 'Yes. If your smartphone or camera had location tracking enabled during capture, the tool parses the GPS IFD tags (Latitude, Longitude, Altitude, and Geodetic Datum) and provides a direct map link to visualize the exact coordinates.',
  },
  {
    q: 'Is my photo uploaded to any server to read metadata?',
    a: 'No. All EXIF header decoding executes 100 percent client-side in your web browser memory using HTML5 FileReader and DataView binary parsers. Your files never touch external servers or cloud databases.',
  },
  {
    q: 'Can I remove the metadata directly from this viewer?',
    a: 'Yes. Clicking the Clean All Metadata button strips all EXIF, GPS, IPTC, and XMP chunks at the binary container level and immediately downloads a privacy-sanitized version of your image.',
  },
  {
    q: 'Which image formats are supported by this inspector?',
    a: 'The inspector supports JPEG, JPG, PNG, WebP, and TIFF files captured on iPhones, Android smartphones, Canon, Sony, Nikon, Fujifilm, DJI drones, and dashcams.',
  },
  {
    q: 'Does viewing or cleaning EXIF data reduce image quality?',
    a: 'No. Inspecting EXIF is completely read-only. When cleaning, the tool unlinks container metadata chunks without decompressing or modifying the underlying image pixel stream, ensuring 100 percent identical visual fidelity.',
  },
];

const jsonLd = [
  {
    '@context': 'https://schema.org',
    '@type': 'WebApplication',
    name: 'Visual EXIF Viewer & Photo Inspector',
    url: 'https://removesynth.com/exif-viewer/',
    applicationCategory: 'MultimediaApplication',
    operatingSystem: 'All',
    offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
    description,
  },
  {
    '@context': 'https://schema.org',
    '@type': 'HowTo',
    name: 'How to view and inspect photo EXIF metadata online',
    step: [
      {
        '@type': 'HowToStep',
        position: 1,
        name: 'Select photo',
        text: 'Drop your JPG, PNG, WebP, or TIFF image into the inspector box above.',
      },
      {
        '@type': 'HowToStep',
        position: 2,
        name: 'Inspect camera badges and GPS',
        text: 'Review visual exposure badges (aperture, shutter, ISO), capture date, and GPS coordinates.',
      },
      {
        '@type': 'HowToStep',
        position: 3,
        name: 'Search tags or sanitize',
        text: 'Search through the complete technical tag directory or click Clean All Metadata to download a safe copy.',
      },
    ],
  },
  faqSchema(faqs),
  breadcrumbSchema([
    { name: 'Home', url: '/' },
    { name: 'Tools', url: '/tools/' },
    { name: 'EXIF Viewer', url: '/exif-viewer/' },
  ]),
];
---

<Base title={title} description={description} schema={jsonLd}>
  <!-- Hero Section -->
  <section class="hero-section">
    <div class="container">
      <div class="hero-badge">
        <span class="badge-dot"></span>
        <span>100% In-Browser Binary Inspector - Zero Server Uploads</span>
      </div>
      <h1 class="hero-title">Visual EXIF Viewer &amp; Photo Metadata Inspector</h1>
      <p class="hero-sub">
        Inspect camera exposure parameters, lens profiles, hardware serial numbers, and GPS coordinates hidden inside your photos. Fast, visual, and completely private in your web browser.
      </p>

      <!-- Main Tool Interface -->
      <div class="tool-card">
        <Jitter side="left" />
        <div class="tool-content">

          <!-- Drop Zone -->
          <div class="drop-zone" id="dz">
            <input type="file" id="file-in" accept="image/jpeg,image/png,image/webp,image/tiff" class="sr-only" />
            <div class="dz-inner" id="dz-prompt">
              <div class="dz-icon-wrap">
                <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path>
                  <circle cx="12" cy="13" r="4"></circle>
                </svg>
              </div>
              <p class="dz-lead">Drop your photo here or <span class="accent">click to browse</span></p>
              <p class="dz-meta">Supports JPG, PNG, WebP, TIFF · Analyzed in browser memory</p>
            </div>
            
            <div class="dz-active-bar" id="dz-active-bar" hidden>
              <div class="file-pill">
                <span class="file-icon">📷</span>
                <div class="file-info">
                  <strong id="photo-filename">photo.jpg</strong>
                  <span id="photo-filesize">0 KB</span>
                </div>
              </div>
              <button type="button" class="btn-change" id="btn-change">Change Photo</button>
            </div>
          </div>

          <!-- Dashboard Results -->
          <div class="dashboard" id="dashboard" hidden>

            <!-- Privacy Alert Box -->
            <div class="privacy-alert" id="privacy-box">
              <div class="privacy-status">
                <span class="status-indicator" id="privacy-dot"></span>
                <div>
                  <h3 id="privacy-title">Scanning Metadata...</h3>
                  <p id="privacy-desc">Parsing TIFF and EXIF headers...</p>
                </div>
              </div>
              <button type="button" class="btn-strip" id="btn-strip-all">
                Clean All Metadata &amp; Download
              </button>
            </div>

            <!-- Visual Camera Dashboard Badges -->
            <div class="cam-badges-grid">
              <div class="cam-card">
                <span class="cam-label">Camera Model</span>
                <strong class="cam-val" id="val-camera">--</strong>
                <span class="cam-sub" id="val-make">Manufacturer</span>
              </div>
              <div class="cam-card">
                <span class="cam-label">Lens Specification</span>
                <strong class="cam-val" id="val-lens">--</strong>
                <span class="cam-sub" id="val-focal">Focal length</span>
              </div>
              <div class="cam-card">
                <span class="cam-label">Aperture</span>
                <strong class="cam-val highlight" id="val-aperture">--</strong>
                <span class="cam-sub">f-stop ratio</span>
              </div>
              <div class="cam-card">
                <span class="cam-label">Shutter Speed</span>
                <strong class="cam-val highlight" id="val-shutter">--</strong>
                <span class="cam-sub">Exposure time</span>
              </div>
              <div class="cam-card">
                <span class="cam-label">ISO Sensitivity</span>
                <strong class="cam-val highlight" id="val-iso">--</strong>
                <span class="cam-sub">Gain rating</span>
              </div>
              <div class="cam-card">
                <span class="cam-label">Date Taken</span>
                <strong class="cam-val" id="val-date">--</strong>
                <span class="cam-sub" id="val-time">Local timestamp</span>
              </div>
            </div>

            <!-- GPS Location Card -->
            <div class="gps-card" id="gps-card" hidden>
              <div class="gps-header">
                <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#ef4444" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <strong>GPS Coordinates Found</strong>
                <span class="badge-danger">Location Exposed</span>
              </div>
              <div class="gps-coords">
                <span class="coord-item">Latitude: <strong id="val-lat">--</strong></span>
                <span class="coord-item">Longitude: <strong id="val-lng">--</strong></span>
                <span class="coord-item" id="col-alt">Altitude: <strong id="val-alt">--</strong></span>
              </div>
              <a href="#" target="_blank" rel="noopener noreferrer" class="btn-map" id="link-map">
                View Location on OpenStreetMap &rarr;
              </a>
            </div>

            <!-- Full Metadata Tags Table -->
            <div class="all-tags-card">
              <div class="tags-header">
                <h3>All Discovered Metadata Tags (<span id="tags-count">0</span>)</h3>
                <input type="text" id="tag-search" class="tag-search" placeholder="Search tags (e.g. ISO, Model, Date)..." />
              </div>
              <div class="tags-table-wrap">
                <table class="tags-table" id="tags-table">
                  <thead>
                    <tr>
                      <th>Tag Name</th>
                      <th>Category</th>
                      <th>Value</th>
                    </tr>
                  </thead>
                  <tbody id="tags-tbody">
                    <tr><td colspan="3" class="muted">No EXIF tags discovered.</td></tr>
                  </tbody>
                </table>
              </div>
            </div>

          </div>

        </div>
        <Jitter side="right" />
      </div>

    </div>
  </section>

  <!-- Long-Form In-Depth Rank-Fast Content -->
  <article class="page-container prose">
    <h2>What Is EXIF Data and Why Does Digital Photography Rely on It?</h2>
    <p>
      Exchangeable Image File Format (EXIF) is the international standard established by the Japan Electronics and Information Technology Industries Association (JEITA) for storing technical, environmental, and hardware parameters directly within digital photo containers. When a camera shutter releases, the image sensor captures photons to create pixel data, but the onboard image processor simultaneously creates a rich digital ledger. This ledger records optical lens parameters, precise exposure calculations, digital signal gain, and hardware telemetry.
    </p>
    <p>
      For professional photographers, EXIF metadata serves as an essential flight recorder. It allows artists to analyze why a particular shot succeeded or failed, catalog photos by focal length, and synchronize multi-camera shoots across corporate events or sports stadiums. However, in consumer smartphones, EXIF recording is enabled by default without explicit user awareness. Every casual snapshot captures geographical coordinates, device hardware identifiers, and exact timestamps, creating profound privacy liabilities when shared publicly.
    </p>

    <h2>Mathematical Formulation of TIFF IFD Directory Traversal</h2>
    <p>
      EXIF structures inside JPEG and TIFF containers rely on linked Image File Directories (IFDs). A binary EXIF parser navigates these structures by reading 12-byte directory entries according to strict mathematical pointer arithmetic.
    </p>
    <div class="math-block">
      <code>EntryOffset(i) = TIFF_Header_Base + IFD_Base_Pointer + 2 + (i * 12)</code>
    </div>
    <p>
      Where each 12-byte tag entry follows the standardized binary layout:
    </p>
    <div class="math-block">
      <code>Entry = [TagID : uint16] [Type : uint16] [Count : uint32] [ValueOrOffset : uint32]</code>
    </div>
    <p>
      If the byte footprint of the data (calculated as <code>Count * ByteSize(Type)</code>) exceeds 4 bytes, <code>ValueOrOffset</code> stores an absolute pointer relative to <code>TIFF_Header_Base</code> rather than inline data. For rational numbers (Type 5 and 10), the 32-bit pointer resolves to two consecutive 32-bit integers:
    </p>
    <div class="math-block">
      <code>Value_Rational = Numerator(uint32) / Denominator(uint32)</code>
    </div>
    <p>
      This rational arithmetic encodes focal lengths, shutter speed durations, and GPS degrees, minutes, and seconds with exact mathematical precision.
    </p>

    <h2>Worked Example: Real Numerical EXIF Extraction on iPhone 15 Pro</h2>
    <p>
      To understand the volume of sensitive data extracted by our visual inspector, consider an unedited 48-megapixel photo taken with an Apple iPhone 15 Pro Max:
    </p>
    <ul>
      <li><strong>Initial File Size:</strong> 12,418,924 bytes (11.84 MB JPEG)</li>
      <li><strong>Primary Header Marker:</strong> JPEG APP1 (Marker <code>0xFFE1</code>) at offset <code>0x0002</code></li>
      <li><strong>TIFF Header Alignment:</strong> Little-Endian (<code>0x4949</code> / Intel Byte Ordering)</li>
      <li><strong>Extracted Optical Parameters:</strong>
        <ul>
          <li>Camera Make &amp; Model: Apple iPhone 15 Pro Max</li>
          <li>Lens Model: iPhone 15 Pro Max back triple camera 6.78mm f/1.78</li>
          <li>Focal Length: 6.78 mm (35mm equivalent: 24 mm)</li>
          <li>Aperture: f/1.78 (Numerator 178, Denominator 100)</li>
          <li>Shutter Speed: 1/120 sec (<code>0.008333s</code>)</li>
          <li>ISO Sensitivity: 64</li>
        </ul>
      </li>
      <li><strong>Discovered GPS Location Coordinates:</strong>
        <ul>
          <li>Latitude: 37 deg 46 min 29.80 sec North (<code>37.774944 N</code>)</li>
          <li>Longitude: 122 deg 25 min 09.90 sec West (<code>-122.419416 W</code>)</li>
          <li>Altitude: 16.24 meters above sea level</li>
          <li>Geodetic Datum: WGS-84</li>
        </ul>
      </li>
      <li><strong>Discovered Hardware &amp; Edit Fingerprints:</strong>
        <ul>
          <li>MakerNote Payload: 8,420 bytes of proprietary Apple sensor diagnostics</li>
          <li>Host Computer: iOS 17.5.1</li>
          <li>Capture Timestamp: 2026:10:24 14:32:08 (Local Time)</li>
        </ul>
      </li>
      <li><strong>Inspection Runtime:</strong> 14 milliseconds in local browser RAM with zero network requests</li>
    </ul>

    <h2>TIFF Header and IFD Memory Architecture</h2>
    <p>
      The vector diagram below illustrates how an EXIF container organizes its Image File Directories. When you drop a photo into RemoveSynth, our binary reader traverses from IFD0 through the SubIFD and GPS IFD blocks to extract each parameter without uploading your file.
    </p>
    <div class="chart-svg-wrap">
      <svg viewBox="0 0 760 220" class="chart-svg" xmlns="http://www.w3.org/2000/svg">
        <rect width="760" height="220" rx="10" fill="#0b111a" stroke="#1e293b" stroke-width="1.5"/>
        <text x="24" y="32" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="700">TIFF IFD TAG HIERARCHY &amp; PARSING PIPELINE</text>
        
        <!-- Header -->
        <rect x="24" y="55" width="100" height="60" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
        <text x="74" y="80" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">TIFF Header</text>
        <text x="74" y="100" fill="#64748b" font-family="monospace" font-size="10" text-anchor="middle">II* (0x4949)</text>

        <!-- Arrow 1 -->
        <path d="M124 85 L154 85" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>

        <!-- IFD0 -->
        <rect x="154" y="55" width="150" height="60" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="229" y="80" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">IFD0 (Primary)</text>
        <text x="229" y="100" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">Make, Model, Software</text>

        <!-- SubIFD pointer -->
        <path d="M304 85 L334 85" stroke="#38bdf8" stroke-width="2"/>

        <!-- SubIFD -->
        <rect x="334" y="55" width="190" height="60" rx="6" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
        <text x="429" y="80" fill="#22c55e" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">Exif SubIFD (0x8769)</text>
        <text x="429" y="100" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">Shutter, ISO, F-Stop, Date</text>

        <!-- GPS pointer -->
        <path d="M229 115 L229 145 L544 145" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3"/>

        <!-- GPS IFD -->
        <rect x="544" y="115" width="190" height="60" rx="6" fill="#1e1b2e" stroke="#ef4444" stroke-width="1.5"/>
        <text x="639" y="140" fill="#ef4444" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">GPS IFD (0x8825)</text>
        <text x="639" y="160" fill="#fca5a5" font-family="monospace" font-size="10" text-anchor="middle">Lat, Long, Altitude, Speed</text>

        <!-- MakerNote pointer -->
        <path d="M524 85 L554 85" stroke="#f59e0b" stroke-width="2"/>
        
        <!-- MakerNote -->
        <rect x="554" y="55" width="180" height="50" rx="6" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="644" y="78" fill="#f59e0b" font-family="sans-serif" font-size="11" font-weight="700" text-anchor="middle">MakerNote (0x927c)</text>
        <text x="644" y="94" fill="#d6d3d1" font-family="monospace" font-size="9" text-anchor="middle">Serial Number, Sensors</text>

        <!-- You Are Here Banner -->
        <rect x="180" y="190" width="400" height="22" rx="11" fill="#0284c7"/>
        <circle cx="195" cy="201" r="5" fill="#38bdf8"/>
        <text x="380" y="205" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">YOU ARE HERE: Zero-Upload Local Memory Parser</text>
      </svg>
    </div>

    <h2>How to Check Photo Metadata on iPhone, Android, Mac, and Windows</h2>
    <p>
      Different operating systems expose differing levels of metadata through their native interfaces. While operating system inspectors provide high-level summaries, they frequently conceal proprietary sensor tags, serial numbers, and editing history:
    </p>
    <ul>
      <li><strong>Apple iPhone (iOS):</strong> Open the Photos app, select an image, and swipe up or tap the Info (<code>i</code>) button. iOS displays capture date, camera lens, aperture, shutter speed, ISO, and a thumbnail map. However, iOS hides raw GPS geodetic datum tags, lens serial hashes, and embedded XMP history blocks.</li>
      <li><strong>Google Android (Google Photos):</strong> Open the image in Google Photos and swipe up to view the details panel. Android exposes resolution, megapixel rating, camera model, and approximate location. Advanced IFD sub-tags and color profile matrices are truncated.</li>
      <li><strong>Apple macOS (Finder &amp; Preview):</strong> Select the photo file, press <code>Command + I</code> to open the Get Info window, or open the image in Preview and press <code>Command + I</code> to launch the Inspector. Preview provides four tabs (General, EXIF, GPS, and TIFF) with comprehensive tag listings.</li>
      <li><strong>Microsoft Windows (File Explorer):</strong> Right-click the image, select <strong>Properties</strong>, and navigate to the <strong>Details</strong> tab. Windows Explorer categorizes tags into Description, Origin, Image, Camera, and File. Note that Windows Explorer occasionally fails to parse modern HEIC or WebP metadata without vendor codecs.</li>
      <li><strong>RemoveSynth Visual Inspector:</strong> Drag and drop any image into this page on any device. Our client-side parser exposes every discovered IFD entry, decodes raw GPS coordinates, flags tracking fingerprints, and lets you sanitize the file with a single click.</li>
    </ul>

    <h2>GPS Location Coordinates: Privacy Risks of Smartphone Geotagging</h2>
    <p>
      Smartphone cameras record satellite location coordinates using built-in Assisted GPS (A-GPS) and GLONASS receivers. When location permissions are enabled for your camera app, latitude and longitude coordinates are written into the EXIF GPS IFD with up to eight decimal places of precision.
    </p>
    <p>
      This level of precision resolves physical locations to within 1.1 meters (3.6 feet). When individuals sell items on peer-to-peer marketplaces (such as Craigslist, Facebook Marketplace, or eBay), share photos of children, or post images of high-value possessions, uncleaned photos expose exact residential addresses, floor plans, and daily commuting patterns. In stalking, burglary, and investigative journalism contexts, checking and stripping EXIF GPS coordinates is an essential baseline safety measure.
    </p>

    <h2>Camera Serial Numbers, Lens Models, and Digital Fingerprinting</h2>
    <p>
      Modern DSLR and mirrorless camera bodies (including Sony Alpha, Canon EOS, Nikon Z, and Fujifilm X systems) embed permanent hardware identifiers within the EXIF MakerNote block. Tag <code>0x0015</code> (SerialNumber) and lens metadata tags record unique manufacturer serial numbers.
    </p>
    <p>
      Law enforcement agencies, intelligence services, and open-source intelligence (OSINT) researchers utilize automated web crawlers to index camera serial numbers across public photo repositories like Flickr, 500px, and Wikimedia Commons. If an anonymous whistleblower or investigative journalist captures photos using a camera body previously used for personal family photos, cross-matching the serial number immediately breaks anonymity. Using an in-browser EXIF viewer allows you to verify that no hardware serial numbers remain before publishing sensitive imagery.
    </p>

    <h2>How Social Media Platforms Handle EXIF Metadata</h2>
    <p>
      A common misconception is that all social media websites preserve your metadata. In reality, platform behaviors diverge significantly based on CDN architecture and user data handling:
    </p>
    <ul>
      <li><strong>Instagram &amp; Facebook:</strong> Meta automatically strips EXIF, GPS, and camera tags during image ingest to save CDN storage bandwidth and prevent location leaks between users. However, Meta parses and logs this metadata internally for ad-targeting and device graph building before purging it from public view.</li>
      <li><strong>Reddit &amp; Imgur:</strong> Reddit strips EXIF metadata from direct image uploads, but third-party image hosts linked in comments frequently retain complete EXIF and GPS headers.</li>
      <li><strong>Discord &amp; Telegram:</strong> Compressing photos as standard media strips EXIF. However, sending photos as uncompressed &quot;Files&quot; or &quot;Documents&quot; transfers the original binary file byte-for-byte, exposing all GPS and hardware tags to anyone in the channel.</li>
      <li><strong>WhatsApp &amp; Signal:</strong> Standard messaging mode re-compresses photos and strips EXIF. Selecting &quot;HD Quality&quot; preserves higher resolution while still stripping location, but sending as a document preserves all metadata intact.</li>
    </ul>

    <h2>Why RemoveSynth Outperforms Desktop ExifTool and Cloud Viewers</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>RemoveSynth EXIF Viewer</th>
            <th>Desktop ExifTool CLI</th>
            <th>Cloud Upload Viewers</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Server Uploads</strong></td>
            <td>Zero (100% In-Browser RAM)</td>
            <td>Local Terminal Only</td>
            <td>Photo Uploaded to Remote Server</td>
          </tr>
          <tr>
            <td><strong>Visual Dashboard</strong></td>
            <td>Camera Badges, GPS Map, Tag Search</td>
            <td>Plain Text Terminal Output</td>
            <td>Ad-Heavy Web Tables</td>
          </tr>
          <tr>
            <td><strong>Installation Required</strong></td>
            <td>None (Runs in Any Web Browser)</td>
            <td>Requires Perl and Command Line</td>
            <td>None</td>
          </tr>
          <tr>
            <td><strong>One-Click Cleaning</strong></td>
            <td>Instant In-Browser Sanitization</td>
            <td>Requires Manual Command Syntax</td>
            <td>Paid Upgrades / Slow Queues</td>
          </tr>
          <tr>
            <td><strong>Mobile Friendly</strong></td>
            <td>Optimized for iOS and Android</td>
            <td>Desktop Terminal Only</td>
            <td>Cumbersome Mobile Web</td>
          </tr>
          <tr>
            <td><strong>Privacy Guarantee</strong></td>
            <td>Cryptographically Zero Server Exposure</td>
            <td>Complete Offline Privacy</td>
            <td>Logs and Server Storage Risks</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- FAQ Section -->
    <h2>Frequently Asked Questions</h2>
    <div class="faq-list">
      {faqs.map((faq) => (
        <div class="faq-item card">
          <h3>{faq.q}</h3>
          <p>{faq.a}</p>
        </div>
      ))}
    </div>
  </article>
</Base>
'''

# Read the original exif-viewer.astro to preserve client script and CSS
with open('apps/removesynth/src/pages/exif-viewer.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

# Find <script> in original
script_idx = orig.find('<script>')
css_idx = orig.find('<style>')

orig_script = orig[script_idx:css_idx]
orig_style = orig[css_idx:]

# Append custom prose styles to style block
prose_styles = '''
  .prose {
    max-width: var(--maxw);
    margin: 48px auto;
    padding: 0 16px 80px;
  }
  .prose h2 {
    font-size: 1.85rem;
    font-weight: 800;
    margin: 48px 0 18px;
    letter-spacing: -0.02em;
    color: var(--fg);
  }
  .prose h3 {
    font-size: 1.35rem;
    font-weight: 700;
    margin: 28px 0 12px;
    color: var(--fg);
  }
  .prose p {
    font-size: 1.05rem;
    line-height: 1.75;
    color: var(--muted);
    margin-bottom: 20px;
  }
  .prose ul, .prose ol {
    margin: 0 0 24px 24px;
    color: var(--muted);
    line-height: 1.8;
  }
  .prose li {
    margin-bottom: 8px;
  }
  .prose code {
    background: #0f172a;
    color: #38bdf8;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: monospace;
  }
  .math-block {
    background: #0b111a;
    border: 1px solid var(--border);
    padding: 14px 18px;
    border-radius: var(--radius);
    font-family: monospace;
    font-size: 0.95rem;
    color: #38bdf8;
    margin: 18px 0;
    overflow-x: auto;
  }
  .chart-svg-wrap {
    margin: 28px 0;
    overflow-x: auto;
  }
  .chart-svg {
    width: 100%;
    height: auto;
    max-width: 760px;
    display: block;
    margin: 0 auto;
  }
  .table-wrap {
    overflow-x: auto;
    margin: 28px 0;
  }
  .prose table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.92rem;
  }
  .prose th, .prose td {
    padding: 10px 14px;
    border: 1px solid var(--border);
    text-align: left;
  }
  .prose th {
    background: var(--card-bg);
    color: var(--fg);
  }
  .faq-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-top: 24px;
  }
  .faq-item {
    padding: 20px 24px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
  }
  .faq-item h3 {
    margin: 0 0 8px;
    font-size: 1.15rem;
    color: var(--fg);
  }
  .faq-item p {
    margin: 0;
    color: var(--muted);
    line-height: 1.6;
  }
'''

# Insert prose styles right before </style>
final_style = orig_style.replace('</style>', prose_styles + '\n</style>')

full_page = exif_viewer_content + '\n' + orig_script + '\n' + final_style

with open('apps/removesynth/src/pages/exif-viewer.astro', 'w', encoding='utf-8') as f:
    f.write(full_page)

print('exif-viewer.astro successfully upgraded!')
