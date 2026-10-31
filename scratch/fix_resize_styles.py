with open('apps/removesynth/src/pages/resize-image.astro', 'r', encoding='utf-8') as f:
    c = f.read()

styles_to_add = """
  .prose {
    max-width: var(--maxw);
    margin: 48px auto;
    padding: 0 16px 40px;
  }
  .prose h2 {
    font-size: 1.85rem;
    font-weight: 800;
    margin: 48px 0 18px;
    letter-spacing: -0.02em;
    color: var(--text);
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
    font-family: var(--mono);
  }
  .math-block {
    background: #0b111a;
    border: 1px solid var(--border);
    padding: 14px 18px;
    border-radius: var(--radius);
    font-family: var(--mono);
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
    background: var(--bg-elev);
    color: var(--text);
  }
"""

if '.prose {' not in c:
    c = c.replace('/* Guide card */', styles_to_add + '\n  /* Guide card */')

with open('apps/removesynth/src/pages/resize-image.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print('Added prose and math styles to resize-image.astro')
