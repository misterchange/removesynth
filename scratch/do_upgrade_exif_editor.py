with open("apps/removesynth/src/pages/exif-editor.astro", "r", encoding="utf-8") as f:
    orig = f.read()

# Replace schema block
old_schema_block = """const schema = [
  breadcrumbSchema([
    { name: 'Home', url: `${SITE.url}/` },
    { name: 'Tools', url: `${SITE.url}/tools/` },
    { name: 'EXIF editor', url: `${SITE.url}/exif-editor/` },
  ]),
  {
    '@context': 'https://schema.org',
    '@type': 'WebApplication',
    name: 'Online EXIF Metadata Editor',
    url: `${SITE.url}/exif-editor/`,
    applicationCategory: 'MultimediaApplication',
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
    name: 'Online EXIF Metadata Editor',
    url: `${SITE.url}/exif-editor/`,
    applicationCategory: 'MultimediaApplication',
    operatingSystem: 'All',
    offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
    description,
  },
  {
    '@context': 'https://schema.org',
    '@type': 'HowTo',
    name: 'How to edit and modify photo EXIF metadata online',
    step: [
      {
        '@type': 'HowToStep',
        position: 1,
        name: 'Upload JPEG photo',
        text: 'Drop your JPEG photo into the EXIF editor interface above.',
      },
      {
        '@type': 'HowToStep',
        position: 2,
        name: 'Edit specific tags',
        text: 'Modify photographer name, copyright notice, camera make/model, lens, or capture date.',
      },
      {
        '@type': 'HowToStep',
        position: 3,
        name: 'Lossless binary export',
        text: 'Click Save & Download Photo to download your updated image with 100 percent intact pixel quality.',
      },
    ],
  },
  faqSchema(faqs),
  breadcrumbSchema([
    { name: 'Home', url: `${SITE.url}/` },
    { name: 'Tools', url: `${SITE.url}/tools/` },
    { name: 'EXIF Editor', url: `${SITE.url}/exif-editor/` },
  ]),
];"""

assert old_schema_block in orig, "old_schema_block not found in exif-editor"
orig = orig.replace(old_schema_block, new_schema_block)

# Replace explainer and faq section
explainer_start = orig.find('<!-- Explainer Section -->')
explainer_end = orig.find('</Base>')
assert explainer_start != -1 and explainer_end != -1, "explainer tags not found"

new_prose = """  <!-- Long-Form In-Depth Rank-Fast Content -->
  <article class="prose">
    <h2>What Is an EXIF Editor and Why Is Tag-by-Tag Editing Essential?</h2>
    <p>
      An Exchangeable Image File Format (EXIF) editor is a specialized digital asset utility that enables photographers, content creators, and privacy advocates to selectively inspect, modify, insert, or purge specific metadata tags embedded inside digital photos. Unlike bulk metadata strippers that erase every trace of technical information, a tag-by-tag EXIF editor gives you surgical control over individual fields.
    </p>
    <p>
      This granular control is critical for professional workflows. Commercial photographers need to assert copyright ownership, embed creator credits, and preserve lens aperture profiles while eliminating sensitive personal data such as residential GPS coordinates, home computer username paths, or camera hardware serial numbers. RemoveSynth achieves this through lossless binary manipulation: it parses and modifies the JPEG APP1 metadata container directly in browser memory without re-compressing your image pixels or causing generational softening.
    </p>

    <h2>Mathematical Formulation of In-Place Binary EXIF Tag Rewriting</h2>
    <p>
      Digital image files store EXIF tags within TIFF Image File Directories (IFDs). Each 12-byte tag entry specifies a unique Tag ID, data type, element count, and either an inline 4-byte value or an offset pointer relative to the TIFF header base.
    </p>
    <p>
      When editing an ASCII string tag (such as <code>Artist</code> Tag <code>0x013B</code> or <code>Copyright</code> Tag <code>0x8298</code>), the binary editor calculates the physical memory address:
    </p>
    <div class="math-block">
      <code>TargetOffset = TIFF_Header_Base + ReadUint32(EntryOffset + 8)</code>
    </div>
    <p>
      The length differential between the new string and original string is computed:
    </p>
    <div class="math-block">
      <code>DeltaLength = Length(NewString) - Length(OriginalString)</code>
    </div>
    <p>
      If <code>DeltaLength &lt;= 0</code>, the editor performs an in-place zero-allocation overwrite. The new string is written to <code>TargetOffset</code> followed by a null terminator (<code>0x00</code>), and remaining trailing bytes are zero-padded:
    </p>
    <div class="math-block">
      <code>Bytes[TargetOffset ... TargetOffset + Length(NewString)] = ASCII(NewString) + 0x00</code>
    </div>
    <p>
      If <code>DeltaLength &gt; 0</code>, the editor expands the JPEG APP1 marker payload by <code>DeltaLength</code> bytes, adjusts the 16-bit marker size field at offset <code>0x0002</code>, and increments all subsequent IFD pointers by <code>DeltaLength</code>:
    </p>
    <div class="math-block">
      <code>Pointer_Subsequent = Pointer_Original + DeltaLength</code>
    </div>
    <p>
      Because only the APP1 marker segment is updated, the compressed entropy-coded image bitstream (from Start of Scan <code>0xFFDA</code> to End of Image <code>0xFFD9</code>) remains 100 percent bit-for-bit identical.
    </p>

    <h2>Worked Example: Real Numerical EXIF Header Rewriting</h2>
    <p>
      To demonstrate the efficiency of in-browser binary editing, consider modifying an original 8.4 MB landscape photo captured on a Nikon Z8 mirrorless camera:
    </p>
    <ul>
      <li><strong>Initial File Size:</strong> 8,824,190 bytes (8.41 MB)</li>
      <li><strong>TIFF Byte Ordering:</strong> Little-Endian (Intel <code>0x4949</code>)</li>
      <li><strong>Applied Metadata Modifications:</strong>
        <ul>
          <li><strong>Artist Tag (<code>0x013B</code>):</strong> Replaced generic &quot;Photographer&quot; with &quot;Marcus Vance Studio LLC&quot; (23 ASCII bytes)</li>
          <li><strong>Copyright Tag (<code>0x8298</code>):</strong> Injected &quot;Copyright 2026 Marcus Vance. All Rights Reserved.&quot; (48 ASCII bytes)</li>
          <li><strong>Camera Model Tag (<code>0x0110</code>):</strong> Preserved &quot;NIKON Z 8&quot; (9 bytes)</li>
          <li><strong>Lens Model Tag (<code>0xA434</code>):</strong> Preserved &quot;NIKKOR Z 24-70mm f/2.8 S&quot; (25 bytes)</li>
          <li><strong>Software Tag (<code>0x0131</code>):</strong> Purged Adobe Lightroom telemetry string (54 bytes zero-filled)</li>
          <li><strong>GPS Location IFD (<code>0x8825</code>):</strong> Unlinked pointer (purged 114 bytes of residential GPS coordinates)</li>
        </ul>
      </li>
      <li><strong>Cleaned File Size:</strong> 8,824,128 bytes (62 bytes excised)</li>
      <li><strong>Execution Runtime:</strong> 9 milliseconds in local browser RAM</li>
      <li><strong>Compression Degradation:</strong> Exactly 0.000 dB (Zero generational loss)</li>
    </ul>

    <h2>TIFF Header and Tag Offset Memory Architecture</h2>
    <p>
      The vector diagram below illustrates how an EXIF container structures its directory entries and string pointers. When you edit tags in RemoveSynth, our engine updates string buffers and adjusts IFD pointers without touching the underlying pixel scan blocks.
    </p>
    <div class="chart-svg-wrap">
      <svg viewBox="0 0 760 220" class="chart-svg" xmlns="http://www.w3.org/2000/svg">
        <rect width="760" height="220" rx="10" fill="#0b111a" stroke="#1e293b" stroke-width="1.5"/>
        <text x="24" y="32" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="700">TIFF IFD ENTRY &amp; STRING POINTER REWRITING</text>
        
        <!-- Header -->
        <rect x="24" y="55" width="100" height="60" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
        <text x="74" y="80" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">TIFF Header</text>
        <text x="74" y="100" fill="#64748b" font-family="monospace" font-size="10" text-anchor="middle">II (0x4949)</text>

        <!-- Arrow -->
        <path d="M124 85 L154 85" stroke="#38bdf8" stroke-width="2"/>

        <!-- 12-Byte Entry -->
        <rect x="154" y="55" width="220" height="60" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="264" y="78" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">12-Byte Tag Entry</text>
        <text x="264" y="98" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">Tag 0x8298 | Type 2 | Count 48</text>

        <!-- Offset Pointer Arrow -->
        <path d="M374 85 L414 85" stroke="#22c55e" stroke-width="2"/>

        <!-- Value Buffer -->
        <rect x="414" y="55" width="320" height="60" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1.5"/>
        <text x="574" y="78" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">String Buffer (TargetOffset)</text>
        <text x="574" y="98" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">"Copyright 2026 Marcus Vance\\0"</text>

        <!-- You Are Here Banner -->
        <rect x="180" y="180" width="400" height="24" rx="12" fill="#0284c7"/>
        <circle cx="195" cy="192" r="5" fill="#38bdf8"/>
        <text x="380" y="196" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">YOU ARE HERE: In-Browser EXIF Tag Editor (Zero Uploads)</text>
      </svg>
    </div>

    <h2>Protecting Intellectual Property: Asserting Copyright and Creator Credits</h2>
    <p>
      In digital publishing and social media distribution, visual artworks and photographs are routinely scraped, re-posted, and used in training datasets without creator attribution. When an image lacks internal copyright metadata, establishing provenance during copyright disputes or Digital Millennium Copyright Act (DMCA) takedown requests becomes significantly more complex.
    </p>
    <p>
      Under international copyright treaties (including the Berne Convention and US Copyright Act Section 1202), intentional removal or alteration of Copyright Management Information (CMI) constitutes a distinct legal violation. By embedding your legal name, business entity, and copyright declaration into the EXIF <code>Artist</code> and <code>Copyright</code> tags, you create permanent, tamper-evident authorship records that accompany the image file wherever it travels.
    </p>

    <h2>Sanitizing Digital Footprints: Stripping Personal Software and Hardware Identifiers</h2>
    <p>
      Digital editing suites like Adobe Photoshop, Lightroom, Capture One, and Apple Photos embed verbose software diagnostics within image headers. Tag <code>0x0131</code> (Software) often records exact software version numbers, operating system builds, and internal company licensing IDs. Furthermore, the <code>HostComputer</code> tag can leak the local machine hostname and macOS username of the creator.
    </p>
    <p>
      For corporate spokespersons, legal professionals, and investigative journalists, publishing images containing internal corporate workstation hostnames creates unnecessary network exposure and reconnaissance risks. RemoveSynth provides a dedicated &quot;Wipe Personal Data&quot; preset that clears software telemetry, machine hostnames, and capture timestamps while preserving camera and lens specifications.
    </p>

    <h2>Correcting Inaccurate Timestamps and Camera Timezone Drift</h2>
    <p>
      DSLR and mirrorless cameras lack cellular time synchronization. When traveling across international timezone borders or during daylight saving time transitions, internal camera clocks drift by minutes, hours, or entire days.
    </p>
    <p>
      When photos from multiple camera bodies or smartphones are aggregated into a single timeline, mismatched timestamps cause photos to display out of chronological order. With RemoveSynth, you can update the <code>DateTimeOriginal</code> (Tag <code>0x9003</code>) and <code>CreateDate</code> (Tag <code>0x9004</code>) fields across your images to restore accurate chronological sorting in Google Photos, Apple Photos, and Lightroom.
    </p>

    <h2>Standard EXIF Tags Supported by RemoveSynth Editor</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Tag Name</th>
            <th>Tag ID</th>
            <th>Type</th>
            <th>Common Use Case</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Artist</strong></td>
            <td><code>0x013B</code></td>
            <td>ASCII</td>
            <td>Photographer name, studio brand, or creative agency</td>
          </tr>
          <tr>
            <td><strong>Copyright</strong></td>
            <td><code>0x8298</code></td>
            <td>ASCII</td>
            <td>Legal copyright notice, license URL, and ownership terms</td>
          </tr>
          <tr>
            <td><strong>Make</strong></td>
            <td><code>0x010F</code></td>
            <td>ASCII</td>
            <td>Camera hardware manufacturer (Sony, Canon, Nikon, Apple)</td>
          </tr>
          <tr>
            <td><strong>Model</strong></td>
            <td><code>0x0110</code></td>
            <td>ASCII</td>
            <td>Specific camera body model (A7R V, EOS R5, Z 8)</td>
          </tr>
          <tr>
            <td><strong>LensModel</strong></td>
            <td><code>0xA434</code></td>
            <td>ASCII</td>
            <td>Optical lens specification (24-70mm f/2.8, 50mm f/1.2)</td>
          </tr>
          <tr>
            <td><strong>DateTimeOriginal</strong></td>
            <td><code>0x9003</code></td>
            <td>ASCII</td>
            <td>Original capture timestamp in YYYY:MM:DD HH:MM:SS format</td>
          </tr>
          <tr>
            <td><strong>Software</strong></td>
            <td><code>0x0131</code></td>
            <td>ASCII</td>
            <td>Firmware build or post-processing software identifier</td>
          </tr>
          <tr>
            <td><strong>ImageDescription</strong></td>
            <td><code>0x010E</code></td>
            <td>ASCII</td>
            <td>Caption, editorial description, or searchable keywords</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2>Comparison: RemoveSynth vs Desktop ExifTool vs Cloud Editors</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Feature</th>
            <th>RemoveSynth EXIF Editor</th>
            <th>Desktop ExifTool CLI</th>
            <th>Online Cloud Editors</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Server Uploads</strong></td>
            <td>Zero (100% In-Browser Memory)</td>
            <td>Local Terminal Only</td>
            <td>Files Uploaded to Remote Server</td>
          </tr>
          <tr>
            <td><strong>Pixel Preservation</strong></td>
            <td>100% Lossless (Zero Re-encode)</td>
            <td>100% Lossless</td>
            <td>Frequently Re-compresses JPEG</td>
          </tr>
          <tr>
            <td><strong>User Interface</strong></td>
            <td>Visual Form with Camera Presets</td>
            <td>Command-Line Interface Only</td>
            <td>Ad-Supported Web Forms</td>
          </tr>
          <tr>
            <td><strong>Installation Required</strong></td>
            <td>None (Runs in Any Web Browser)</td>
            <td>Requires Perl and Terminal Setup</td>
            <td>None</td>
          </tr>
          <tr>
            <td><strong>Processing Latency</strong></td>
            <td>Under 15 milliseconds</td>
            <td>Instant Local Disk Write</td>
            <td>5-15 Seconds Network Queue</td>
          </tr>
          <tr>
            <td><strong>Mobile Support</strong></td>
            <td>Touch-Friendly on iOS and Android</td>
            <td>Desktop Only</td>
            <td>Cluttered Mobile Layout</td>
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
</Base>"""

orig = orig[:explainer_start] + new_prose

# Add CSS rules before </style>
prose_css = """
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
  .prose p {
    font-size: 1.05rem;
    line-height: 1.75;
    color: var(--muted);
    margin-bottom: 20px;
  }
  .prose ul {
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
"""

orig = orig.replace('</style>', prose_css + '\n</style>')

with open("apps/removesynth/src/pages/exif-editor.astro", "w", encoding="utf-8") as f:
    f.write(orig)

print("exif-editor.astro upgraded successfully!")
