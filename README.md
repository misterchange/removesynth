# RemoveSynth + CheckAIorNot

One repo, two Astro sites on Cloudflare Pages, plus the RemoveSynth processing API.

```
apps/removesynth/     removesynth.com   SynthID remover, privacy tools, generator pages, DE/ES pages
apps/checkaiornot/    checkaiornot.com  AI metadata checker, platform pages, SynthID detector guide
packages/shared/      metadata engine (inspect/clean), Checker/ToolDrop/Faq components, base styles, explainer data
backend/              FastAPI processing API for RemoveSynth
```

Both sites share the design in `packages/shared/src/styles/base.css`; CheckAIorNot overrides the accent colours in `apps/checkaiornot/src/styles/theme.css`. Cross-site links use `packages/shared/src/sites.ts`.

## Develop

```bash
npm install
npm run dev:removesynth
npm run dev:checkaiornot
npm test
npm run build
```

Each site deploys as its own Cloudflare Pages project. Keep the root directory at the repo root (so the shared workspace package is installed), then:

| Project | Build command | Output directory |
|---|---|---|
| removesynth | `npm run build -w removesynth` | `apps/removesynth/dist` |
| checkaiornot | `npm run build -w checkaiornot` | `apps/checkaiornot/dist` |

---

## RemoveSynth details

Static Astro site deployed to Cloudflare Pages. The upload tool calls a separate processing backend that you configure.

## Develop

```bash
npm install
npm run dev
```

Copy `.env.example` to `.env` and set `PUBLIC_API_URL` to point the upload UI at your backend.

## Pages

| URL | File | Target keyword |
|---|---|---|
| `/` | `src/pages/index.astro` | removesynth, SynthID remover (brand) |
| `/remove-synthid/` | `src/pages/remove-synthid.astro` | remove synthid |
| `/what-is-synthid/` | `src/pages/what-is-synthid.astro` | what is synthid |
| `/how-to-remove-synthid/` | `src/pages/how-to-remove-synthid.astro` | how to remove synthid |
| `/blog/` | `src/pages/blog/` + `src/content/blog/*.md` | long-tail |

To add a blog post, create a Markdown file in `src/content/blog/` with `title`, `description` and `pubDate` frontmatter.

Every page has a title, meta description, canonical URL, Open Graph tags and JSON-LD (FAQPage, HowTo, BreadcrumbList, BlogPosting). The sitemap is generated at `/sitemap-index.xml`.

## Backend contract

The upload UI (`src/components/Uploader.astro`) sends:

```
POST {PUBLIC_API_URL}/process
Content-Type: multipart/form-data
field: file
```

and expects:

- `200` with the processed file as the body and the right `Content-Type` (e.g. `image/png`, `video/mp4`)
- any non-2xx status with a plain-text error message, which is shown to the user

The backend must send CORS headers allowing `https://removesynth.com` (and `http://localhost:4321` for local dev).

## Deploy to Cloudflare Pages

**Git integration (recommended):** connect the repo in the Cloudflare dashboard → Pages, with:

- Build command: `npm run build`
- Output directory: `dist`
- Environment variables: `PUBLIC_API_URL`, `PUBLIC_MAX_UPLOAD_MB`, and `NODE_VERSION=22`

**CLI:**

```bash
npx wrangler login
npm run deploy
```

Security and cache headers are set in `public/_headers`.
