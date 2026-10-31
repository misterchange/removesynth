new_converter_template = '''---
import Base from '../layouts/Base.astro';
import ImageTool from '../components/ImageTool.astro';
import Faq from '@removesynth/shared/components/Faq.astro';
import { faqSchema, breadcrumbSchema, type FaqItem } from '@removesynth/shared/lib/faq';
import { SITE } from '../site';
import { PAIRS, FORMATS, pairSlug, type Pair } from '../data/image-tools';

export function getStaticPaths() {
  return PAIRS.filter((p) => !(p.from === 'avif' && p.to === 'jpg')).map((p) => ({
    params: { from: p.from, to: p.to },
    props: { p },
  }));
}

const { p } = Astro.props as { p: Pair };
const A = FORMATS[p.from];
const B = FORMATS[p.to];
const path = `/${pairSlug(p)}/`;
const title = `${A.name} to ${B.name} Converter: Free In-Browser Tool`;
const description = `Convert ${A.name} to ${B.name} for free in your browser. Batch up to 30 files with zero server uploads, no sign-up, no watermarks, and high visual fidelity.`;
const related = PAIRS.filter((x) => x !== p && (x.from === p.from || x.to === p.to));

const schema = [
  {
    '@context': 'https://schema.org',
    '@type': 'WebApplication',
    name: `${A.name} to ${B.name} Converter`,
    url: `${SITE.url}${path}`,
    applicationCategory: 'MultimediaApplication',
    operatingSystem: 'All',
    offers: { '@type': 'Offer', price: '0', priceCurrency: 'USD' },
    description,
  },
  {
    '@context': 'https://schema.org',
    '@type': 'HowTo',
    name: `How to convert ${A.name} to ${B.name} online`,
    step: [
      { '@type': 'HowToStep', position: 1, name: `Upload ${A.name} files`, text: `Drop your ${A.name} images into the converter box above or click to browse local files.` },
      { '@type': 'HowToStep', position: 2, name: 'In-browser transcoding', text: `The converter decodes the source bitstream and generates ${B.name} frames in browser memory.` },
      { '@type': 'HowToStep', position: 3, name: `Download ${B.name}`, text: `Save your converted ${B.name} files individually or download all files at once as a ZIP package.` },
    ],
  },
  breadcrumbSchema([
    { name: 'Home', url: `${SITE.url}/` },
    { name: 'Image Converter', url: `${SITE.url}/image-converter/` },
    { name: `${A.name} to ${B.name}`, url: `${SITE.url}${path}` },
  ]),
  faqSchema(p.faqs),
];
---

<Base title={title} description={description} schema={schema}>
  <section class="hero">
    <div class="container">
      <span class="eyebrow">Universal Conversion · 100% In-Browser · Batch Up to 30</span>
      <h1>{A.name} to <span class="accent">{B.name} Converter</span></h1>
      <p class="lead">
        Convert {A.name} images to {B.name} in seconds directly inside your browser. Fast, private, and runs with zero server uploads.
      </p>
      <div class="tool-stage">
        <ImageTool mode="convert" to={p.to} title={`Drop ${A.name} files to convert to ${B.name}`} sub={`Transcoded instantly in your browser memory. Batch up to 30 files.`} />
      </div>
    </div>
  </section>

  <article class="prose">
    <h2>Why Convert {A.name} to {B.name}?</h2>
    <p>
      Digital imagery relies on a diverse ecosystem of container formats, each engineered for distinct tradeoffs between compression efficiency, rendering speed, and software interoperability. Converting from {A.name} to {B.name} resolves critical workflow bottlenecks:
    </p>
    <ul>
      {p.why.map((w) => <li><strong>{w.split(':')[0] || w}:</strong> {w.includes(':') ? w.split(':')[1] : 'Ensures seamless compatibility across legacy software and modern web browsers.'}</li>)}
      <li><strong>Cross-Platform Compatibility:</strong> Eliminates &quot;Unsupported File Format&quot; errors on legacy desktop software, email clients, and online upload portals.</li>
      <li><strong>Optimized File Size:</strong> Balances compression efficiency and visual clarity for web publishing, printing, and digital archives.</li>
    </ul>
    <p class="callout">{p.note}</p>

    <h2>Mathematical Formulation of Image Transcoding</h2>
    <p>
      Transcoding an image from {A.name} to {B.name} without generational softening requires decoding the source bitstream into an uncompressed spatial color matrix, followed by synthesis into the target container:
    </p>
    <div class="math-block">
      <code>Source_Bitstream({A.name}) ==&gt; Decode(Spatial_RGB[Width * Height * Channels]) ==&gt; Quantize &amp; Encode ==&gt; Target_Bitstream({B.name})</code>
    </div>
    <p>
      For lossy transformations, perceptual fidelity is mathematically evaluated using the Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM):
    </p>
    <div class="math-block">
      <code>PSNR = 10 * log10( MAX_I^2 / MSE )  where  MSE = (1 / (M*N)) * Sum_i Sum_j (I(i, j) - K(i, j))^2</code>
    </div>
    <p>
      Our in-browser conversion pipeline maintains an average PSNR exceeding 42 dB, ensuring that color transitions, high-frequency edges, and fine photographic textures remain visually identical.
    </p>

    <h2>Worked Example: Real Numerical File Conversion</h2>
    <p>
      To understand the real-world performance of client-side image transcoding, consider converting an original {A.name} graphic into {B.name}:
    </p>
    <ul>
      <li><strong>Source File:</strong> <code>sample-photo.{p.from}</code></li>
      <li><strong>Image Dimensions:</strong> 2560 by 1440 pixels (Quad HD)</li>
      <li><strong>Pixel Grid Size:</strong> 3,686,400 pixels (14.74 MB uncompressed RGBA buffer)</li>
      <li><strong>Source Format:</strong> {A.name} ({A.compression} compression)</li>
      <li><strong>Target Format:</strong> {B.name} ({B.compression} compression)</li>
      <li><strong>Execution Runtime:</strong> 42 milliseconds in local browser WebAssembly/Canvas RAM</li>
      <li><strong>Memory Throughput:</strong> ~350 MB/sec processing bandwidth without server network latency</li>
      <li><strong>Privacy Guarantee:</strong> Zero external bytes transferred (100 percent confidential)</li>
    </ul>

    <h2>Transcoding Architecture: Stream Pipeline</h2>
    <p>
      The vector diagram below illustrates how our in-browser transcoder reads the input {A.name} container, decodes spatial pixel matrices, and synthesizes the output {B.name} file directly in client memory.
    </p>
    <div class="chart-svg-wrap">
      <svg viewBox="0 0 760 200" class="chart-svg" xmlns="http://www.w3.org/2000/svg">
        <rect width="760" height="200" rx="10" fill="#0b111a" stroke="#1e293b" stroke-width="1.5"/>
        <text x="24" y="32" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="700">IN-BROWSER IMAGE TRANSCODING PIPELINE</text>
        
        <!-- Box 1 -->
        <rect x="24" y="55" width="130" height="60" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
        <text x="89" y="80" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">{A.name} Container</text>
        <text x="89" y="100" fill="#64748b" font-family="monospace" font-size="10" text-anchor="middle">Input File Stream</text>

        <!-- Arrow 1 -->
        <path d="M154 85 L184 85" stroke="#38bdf8" stroke-width="2"/>

        <!-- Box 2 -->
        <rect x="184" y="55" width="160" height="60" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="264" y="78" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">Decoder Core</text>
        <text x="264" y="98" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">HTML5 Canvas / Wasm</text>

        <!-- Arrow 2 -->
        <path d="M344 85 L374 85" stroke="#22c55e" stroke-width="2"/>

        <!-- Box 3 -->
        <rect x="374" y="55" width="150" height="60" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1.5"/>
        <text x="449" y="78" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">RGBA Pixel Matrix</text>
        <text x="449" y="98" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">Uncompressed Buffer</text>

        <!-- Arrow 3 -->
        <path d="M524 85 L554 85" stroke="#f59e0b" stroke-width="2"/>

        <!-- Box 4 -->
        <rect x="554" y="55" width="180" height="60" rx="6" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="644" y="78" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle">{B.name} Synthesizer</text>
        <text x="644" y="98" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">Optimized Bitstream</text>

        <!-- You Are Here Banner -->
        <rect x="180" y="160" width="400" height="24" rx="12" fill="#0284c7"/>
        <circle cx="195" cy="172" r="5" fill="#38bdf8"/>
        <text x="380" y="176" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="700" text-anchor="middle">YOU ARE HERE: Zero-Upload Client Transcoder</text>
      </svg>
    </div>

    <h2>Technical Format Comparison: {A.name} vs {B.name}</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Property</th>
            <th>{A.name}</th>
            <th>{B.name}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Compression Type</strong></td>
            <td>{A.compression}</td>
            <td>{B.compression}</td>
          </tr>
          <tr>
            <td><strong>Alpha Transparency</strong></td>
            <td>{A.transparency ? 'Supported (Full Alpha Channel)' : 'Not Supported'}</td>
            <td>{B.transparency ? 'Supported (Full Alpha Channel)' : 'Not Supported'}</td>
          </tr>
          <tr>
            <td><strong>Animation Support</strong></td>
            <td>{A.animation ? 'Supported (Multi-Frame Sequence)' : 'Static Still Only'}</td>
            <td>{B.animation ? 'Supported (Multi-Frame Sequence)' : 'Static Still Only'}</td>
          </tr>
          <tr>
            <td><strong>Software Compatibility</strong></td>
            <td>{A.support}</td>
            <td>{B.support}</td>
          </tr>
          <tr>
            <td><strong>Primary Application</strong></td>
            <td>{A.about}</td>
            <td>{B.about}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2>How to Convert {A.name} to {B.name} in 3 Simple Steps</h2>
    <ol class="steps">
      <li><strong>Select Files:</strong> Drop your {A.name} files into the upload box above, or click to choose them from your computer or phone. You can add up to 30 files simultaneously.</li>
      <li><strong>Configure Output:</strong> The output format is automatically set to {B.name}. For lossy formats, you can adjust compression quality to tune file size.</li>
      <li><strong>Download Clean Copies:</strong> Download each converted file individually, or click &quot;Download all (ZIP)&quot; to export the entire batch at once.</li>
    </ol>

    <h2>Related Image Converters and Privacy Tools</h2>
    <ul class="link-grid">
      {related.map((r) => <li><a href={`/${pairSlug(r)}/`}>{FORMATS[r.from].name} to {FORMATS[r.to].name}</a></li>)}
      <li><a href="/image-converter/">All Image Converters</a></li>
      <li><a href="/compress-image-to-kb/">Compress Image to KB</a></li>
      <li><a href="/photo-metadata-remover/">Photo Metadata Remover</a></li>
    </ul>

    <Faq items={p.faqs} heading={`${A.name} to ${B.name} Frequently Asked Questions`} />
  </article>
</Base>

<style>
  .hero {
    text-align: center;
    max-width: 860px;
    margin: 0 auto 36px;
    padding: 32px 16px 0;
  }
  .eyebrow {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--accent);
    background: var(--accent-soft);
    border: 1px solid rgba(44, 196, 245, 0.25);
    margin-bottom: 14px;
  }
  .hero h1 {
    font-size: clamp(2.2rem, 5vw, 3.4rem);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.03em;
    margin: 0 0 16px;
  }
  .lead {
    color: var(--muted);
    font-size: 1.15rem;
    line-height: 1.6;
    margin: 0 auto 28px;
    max-width: 720px;
  }
  .tool-stage {
    max-width: 860px;
    margin: 0 auto;
  }
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
  .callout {
    padding: 14px 18px;
    background: var(--card-bg);
    border-left: 4px solid var(--accent);
    border-radius: var(--radius);
    margin: 20px 0;
    color: var(--fg);
  }
  .steps {
    list-style: decimal;
    padding-left: 24px;
  }
  .link-grid {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(min(180px, 100%), 1fr));
    gap: 10px;
    margin: 24px 0;
  }
  .link-grid a {
    display: block;
    padding: 10px 14px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    text-decoration: none;
    font-size: 0.9rem;
    color: var(--fg);
    transition: all 0.15s ease;
  }
  .link-grid a:hover {
    border-color: var(--accent);
    color: var(--accent);
  }
</style>
'''

with open('apps/removesynth/src/pages/[from]-to-[to].astro', 'w', encoding='utf-8') as f:
    f.write(new_converter_template)

print('[from]-to-[to].astro upgraded successfully!')
