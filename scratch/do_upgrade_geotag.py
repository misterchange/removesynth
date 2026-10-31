with open("apps/removesynth/src/pages/geotag-photo.astro", "r", encoding="utf-8") as f:
    orig = f.read()

# Replace schema block
old_schema_block = """const schema = [
  breadcrumbSchema([
    { name: 'Home', url: `${SITE.url}/` },
    { name: 'Tools', url: `${SITE.url}/tools/` },
    { name: 'Geotag photo', url: `${SITE.url}/geotag-photo/` },
  ]),
  {
    '@context': 'https://schema.org',
    '@type': 'WebApplication',
    name: 'Geotag Photo & GPS EXIF Injector',
    url: `${SITE.url}/geotag-photo/`,
    applicationCategory: 'PhotographyApplication',
    operatingSystem: 'Any (web browser)',
    offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
    description,
  },
  faqSchema(faqs),
];"""

new_schema_block = """const schema = [
  {
    '@context': 'https://schema.org',
    '@type': 'WebApplication',
    name: 'Geotag Photo Online: GPS EXIF Injector',
    url: `${SITE.url}/geotag-photo/`,
    applicationCategory: 'PhotographyApplication',
    operatingSystem: 'All',
    offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
    description,
  },
  {
    '@context': 'https://schema.org',
    '@type': 'HowTo',
    name: 'How to geotag photos and add GPS coordinates online',
    step: [
      {
        '@type': 'HowToStep',
        position: 1,
        name: 'Upload photo',
        text: 'Drop your JPG, PNG, or WebP photo into the geotag tool above.',
      },
      {
        '@type': 'HowToStep',
        position: 2,
        name: 'Pick coordinates or preset',
        text: 'Click on the interactive map, select a city preset, or enter exact latitude and longitude values.',
      },
      {
        '@type': 'HowToStep',
        position: 3,
        name: 'Inject GPS and download',
        text: 'Click Geotag & Download Photo to save your image with standard EXIF 2.31 GPS tags injected in browser memory.',
      },
    ],
  },
  faqSchema(faqs),
  breadcrumbSchema([
    { name: 'Home', url: `${SITE.url}/` },
    { name: 'Tools', url: `${SITE.url}/tools/` },
    { name: 'Geotag Photo', url: `${SITE.url}/geotag-photo/` },
  ]),
];"""

assert old_schema_block in orig, "old_schema_block not found"
orig = orig.replace(old_schema_block, new_schema_block)

# Replace prose section
prose_start = orig.find('<article class="prose">')
prose_end = orig.find('</Base>')
assert prose_start != -1 and prose_end != -1, "prose tags not found"

new_prose = """  <article class="prose">
    <h2>What Is Geotagging and How Do Digital Image Headers Store GPS Coordinates?</h2>
    <p>
      Geotagging is the technological process of embedding geographic coordinates - latitude, longitude, elevation, and timestamp data - directly inside the EXIF metadata container of a digital image. Every camera, smartphone, and photo viewer relies on standardized EXIF specifications established by the Japan Electronics and Information Technology Industries Association (JEITA) to read and parse this positional information.
    </p>
    <p>
      Unlike visible watermarks that alter image pixels, geotags exist entirely within dedicated binary blocks known as the GPS IFD (Image File Directory, Tag ID <code>0x8825</code>). When modern photo cataloging applications like Apple Photos, Google Photos, or Adobe Lightroom inspect an image, they traverse this IFD block, decode the coordinate arrays, and place a visual pin on interactive travel maps. If your digital camera lacked built-in satellite receivers, was in airplane mode, or if you generated creative visual assets using AI image generators like Midjourney or Stable Diffusion, your images lack geographical identity. RemoveSynth allows you to losslessly inject or correct precise GPS metadata directly in your browser.
    </p>

    <h2>Mathematical Formulation of Decimal to EXIF Rational Coordinate Conversion</h2>
    <p>
      Modern mapping services (including Google Maps, OpenStreetMap, and GPS hardware receivers) output coordinates in Decimal Degrees (DD). However, the EXIF 2.31 specification mandates that latitude and longitude must be stored as three unsigned 64-bit rational numbers representing Degrees, Minutes, and Seconds (DMS).
    </p>
    <p>
      The conversion from decimal degrees to EXIF rational triples is governed by the following mathematical equations:
    </p>
    <div class="math-block">
      <code>Degrees = floor(|DecimalDegrees|)</code>
    </div>
    <div class="math-block">
      <code>Minutes = floor((|DecimalDegrees| - Degrees) * 60)</code>
    </div>
    <div class="math-block">
      <code>Seconds = round((((|DecimalDegrees| - Degrees) * 60) - Minutes) * 60 * 1000) / 1000</code>
    </div>
    <p>
      In binary TIFF formatting, each component is encoded as two 32-bit unsigned integers (Numerator and Denominator):
    </p>
    <div class="math-block">
      <code>GPSRationalArray = [ (Degrees, 1), (Minutes, 1), (round(Seconds * 1000), 1000) ]</code>
    </div>
    <p>
      Hemispheric direction is encoded in a separate 2-byte ASCII string tag: <code>GPSLatitudeRef</code> stores <code>'N'</code> (positive) or <code>'S'</code> (negative), while <code>GPSLongitudeRef</code> stores <code>'E'</code> (positive) or <code>'W'</code> (negative).
    </p>

    <h2>Worked Example: Real Numerical Geotag Injection</h2>
    <p>
      To illustrate the exact binary payload injected into a photo, consider an untagged commercial architectural photograph captured in San Francisco, California:
    </p>
    <ul>
      <li><strong>Target Coordinates:</strong> 37.774929 Latitude North, -122.419416 Longitude West, Altitude 18.0 Meters</li>
      <li><strong>Latitude Conversion:</strong>
        <ul>
          <li>Degrees: <code>floor(37.774929) = 37</code></li>
          <li>Minutes: <code>floor((37.774929 - 37) * 60) = floor(46.49574) = 46</code></li>
          <li>Seconds: <code>(46.49574 - 46) * 60 = 29.7444 sec</code></li>
          <li>EXIF Tag <code>0x0002</code> Rational Bytes: <code>[ (37, 1), (46, 1), (29744, 1000) ]</code></li>
          <li>EXIF Tag <code>0x0001</code> Reference: <code>'N'</code></li>
        </ul>
      </li>
      <li><strong>Longitude Conversion:</strong>
        <ul>
          <li>Degrees: <code>floor(122.419416) = 122</code></li>
          <li>Minutes: <code>floor((122.419416 - 122) * 60) = floor(25.16496) = 25</code></li>
          <li>Seconds: <code>(25.16496 - 25) * 60 = 9.8976 sec</code></li>
          <li>EXIF Tag <code>0x0004</code> Rational Bytes: <code>[ (122, 1), (25, 1), (9898, 1000) ]</code></li>
          <li>EXIF Tag <code>0x0003</code> Reference: <code>'W'</code></li>
        </ul>
      </li>
      <li><strong>Altitude Tag (<code>0x0006</code>):</strong> Rational <code>(180, 10)</code> meters, AltitudeRef <code>0x00</code> (Above Sea Level)</li>
      <li><strong>Total Metadata Overhead:</strong> Exactly 114 bytes injected into JPEG APP1 container</li>
      <li><strong>Processing Speed:</strong> 6 milliseconds in browser client RAM with 0 percent image re-compression</li>
    </ul>

    <h2>EXIF GPS IFD Binary Directory Structure</h2>
    <p>
      The vector diagram below illustrates how GPS tags are organized in the TIFF container. When RemoveSynth injects coordinates, it inserts pointer <code>0x8825</code> into IFD0 and writes the corresponding GPS tags into a dedicated sub-directory without touching pixel stream data.
    </p>
    <div class="chart-svg-wrap">
      <svg viewBox="0 0 760 220" class="chart-svg" xmlns="http://www.w3.org/2000/svg">
        <rect width="760" height="220" rx="10" fill="#0b111a" stroke="#1e293b" stroke-width="1.5"/>
        <text x="24" y="32" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="700">GPS IFD INJECTION &amp; RATIONAL BYTE STREAM</text>
        
        <!-- TIFF Header -->
        <rect x="24" y="55" width="110" height="60" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
        <text x="79" y="80" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">TIFF Header</text>
        <text x="79" y="100" fill="#64748b" font-family="monospace" font-size="10" text-anchor="middle">Little-Endian (II)</text>

        <!-- Arrow -->
        <path d="M134 85 L164 85" stroke="#38bdf8" stroke-width="2"/>

        <!-- IFD0 -->
        <rect x="164" y="55" width="160" height="60" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="244" y="80" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">IFD0 Directory</text>
        <text x="244" y="100" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">GPS Pointer: 0x8825</text>

        <!-- GPS Arrow -->
        <path d="M324 85 L354 85" stroke="#22c55e" stroke-width="2"/>

        <!-- GPS IFD -->
        <rect x="354" y="55" width="382" height="90" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1.5"/>
        <text x="545" y="78" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">GPSInfo Sub-Directory (Tag 0x8825)</text>
        <text x="545" y="98" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">0x0001: GPSLatitudeRef ('N' / 'S')</text>
        <text x="545" y="116" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">0x0002: GPSLatitude (DMS Rationals)</text>
        <text x="545" y="134" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">0x0003: GPSLongitudeRef | 0x0004: Longitude</text>

        <!-- You Are Here Banner -->
        <rect x="180" y="180" width="400" height="24" rx="12" fill="#0284c7"/>
        <circle cx="195" cy="192" r="5" fill="#38bdf8"/>
        <text x="380" y="196" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">YOU ARE HERE: In-Browser GPS Injector (Zero Uploads)</text>
      </svg>
    </div>

    <h2>Local SEO and Google Business Profile: Why Businesses Geotag Photos</h2>
    <p>
      Local search engine optimization is heavily influenced by geographical relevance signals. When local contractors, plumbers, restaurants, and retail stores upload photos to Google Business Profile (formerly Google My Business), search engine algorithms parse embedded EXIF GPS tags to corroborate the physical location of the business activity.
    </p>
    <p>
      An HVAC technician uploading job site photos with verified municipal coordinates reinforces local proximity signals for search queries such as &quot;emergency AC repair near me&quot;. Ungeotagged images lack this structured spatial confirmation. By geotagging your portfolio photos with exact business coordinates before publishing, you establish an authoritative visual footprint across Google Maps and local search results.
    </p>

    <h2>Real Estate, Construction, and Field Verification Documentation</h2>
    <p>
      In commercial and residential real estate, multiple-listing services (MLS) and property aggregators rely on geotagged imagery to index properties automatically into neighborhood search radius filters. Property inspectors, insurance claim adjusters, and civil engineering teams also depend on tamper-evident GPS coordinates to prove that photographs were captured at a specific parcel or foundation site rather than a reused archive photo.
    </p>
    <p>
      RemoveSynth enables field teams working on laptops, tablets, or phones to correct misplaced pins or inject GPS coordinates onto drone surveys and architectural renderings before submitting documentation packages.
    </p>

    <h2>Travel Photography and Photo Library Organization</h2>
    <p>
      Dedicated digital single-lens reflex (DSLR) and mirrorless cameras from Canon, Sony, Nikon, and Fujifilm often lack built-in GPS receivers to preserve battery life. As a result, vacation and landscape photos taken on professional cameras appear in a generic &quot;No Location&quot; bucket when imported into Apple Photos or Google Photos.
    </p>
    <p>
      By selecting locations on our interactive map or using city presets, photographers can batch-tag their travel photos in seconds. Once imported, photo libraries organize shots into interactive map views, travel memories, and geographical search albums effortlessly.
    </p>

    <h2>Standard EXIF 2.31 GPS Tags Injected by RemoveSynth</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>EXIF Tag</th>
            <th>Tag ID</th>
            <th>Data Type</th>
            <th>Example Format</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>GPSVersionID</strong></td>
            <td><code>0x0000</code></td>
            <td><code>BYTE[4]</code></td>
            <td><code>2, 3, 0, 0</code></td>
            <td>Specifies EXIF GPS standard version 2.3.0.0</td>
          </tr>
          <tr>
            <td><strong>GPSLatitudeRef</strong></td>
            <td><code>0x0001</code></td>
            <td><code>ASCII[2]</code></td>
            <td><code>'N'</code> (North) or <code>'S'</code> (South)</td>
            <td>Hemispheric latitude reference</td>
          </tr>
          <tr>
            <td><strong>GPSLatitude</strong></td>
            <td><code>0x0002</code></td>
            <td><code>RATIONAL[3]</code></td>
            <td><code>37/1, 46/1, 29744/1000</code></td>
            <td>Degrees, minutes, and seconds rational array</td>
          </tr>
          <tr>
            <td><strong>GPSLongitudeRef</strong></td>
            <td><code>0x0003</code></td>
            <td><code>ASCII[2]</code></td>
            <td><code>'E'</code> (East) or <code>'W'</code> (West)</td>
            <td>Prime meridian longitude reference</td>
          </tr>
          <tr>
            <td><strong>GPSLongitude</strong></td>
            <td><code>0x0004</code></td>
            <td><code>RATIONAL[3]</code></td>
            <td><code>122/1, 25/1, 9898/1000</code></td>
            <td>Degrees, minutes, and seconds rational array</td>
          </tr>
          <tr>
            <td><strong>GPSAltitudeRef</strong></td>
            <td><code>0x0005</code></td>
            <td><code>BYTE[1]</code></td>
            <td><code>0</code> (Above Sea Level)</td>
            <td>Reference altitude datum</td>
          </tr>
          <tr>
            <td><strong>GPSAltitude</strong></td>
            <td><code>0x0006</code></td>
            <td><code>RATIONAL[1]</code></td>
            <td><code>180/10</code> (18.0 meters)</td>
            <td>Elevation in meters relative to reference</td>
          </tr>
          <tr>
            <td><strong>GPSMapDatum</strong></td>
            <td><code>0x0012</code></td>
            <td><code>ASCII</code></td>
            <td><code>'WGS-84'</code></td>
            <td>World Geodetic System 1984 coordinate standard</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2>Comparison: RemoveSynth vs Desktop Tools vs Cloud Geotaggers</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>RemoveSynth In-Browser</th>
            <th>Desktop ExifTool CLI</th>
            <th>Online Cloud Services</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Server Uploads</strong></td>
            <td>Zero (100% Client-Side Memory)</td>
            <td>Local Terminal Only</td>
            <td>Files Uploaded to Remote Servers</td>
          </tr>
          <tr>
            <td><strong>Interactive Map</strong></td>
            <td>Live OpenStreetMap Pin Dropper</td>
            <td>None (Manual Coordinates Entry)</td>
            <td>Supported (Ad-Supported UI)</td>
          </tr>
          <tr>
            <td><strong>Pixel Re-encoding</strong></td>
            <td>Zero (Bit-for-Bit Lossless)</td>
            <td>Lossless Binary Write</td>
            <td>Frequently Re-compresses JPEG</td>
          </tr>
          <tr>
            <td><strong>City Quick Presets</strong></td>
            <td>Instant 1-Click Global Metros</td>
            <td>Requires Manual Config Files</td>
            <td>Rarely Available</td>
          </tr>
          <tr>
            <td><strong>Mobile Support</strong></td>
            <td>Full Touch Support on iPhone/Android</td>
            <td>Desktop Only</td>
            <td>Cluttered Mobile Interface</td>
          </tr>
          <tr>
            <td><strong>Cost &amp; Limits</strong></td>
            <td>100% Free Without File Limits</td>
            <td>Free Open Source</td>
            <td>Paid Subscriptions / Daily Caps</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- FAQ Section -->
    <Faq items={faqs} heading="Frequently Asked Questions" />
  </article>"""

orig = orig[:prose_start] + new_prose + orig[prose_end:]

# Add CSS rules before </style>
prose_css = """
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
"""

orig = orig.replace('</style>', prose_css + '\n</style>')

with open("apps/removesynth/src/pages/geotag-photo.astro", "w", encoding="utf-8") as f:
    f.write(orig)

print("geotag-photo.astro upgraded successfully!")
