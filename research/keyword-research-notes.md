# RemoveSynth keyword research notes

Seed table: `seed-keywords.csv` (open in Excel; UTF-8 with BOM). Regenerate with `python build_seeds.py`.
Cells hold 1–3 seeds separated by ` | `; a trailing `?` means I'm unsure locals phrase it that way.

## Scope

RemoveSynth = removal and conversion tools: photo/file privacy cleaners, image converters, SynthID removal,
plus platform and AI-app pages built on those tools (privacy and format angles).

Group G ("AI-label removal (research)") lists seeds for AI-label / C2PA / "AI info" removal, "remove AI
detection", AI-app metadata and watermark removal, PNG prompt stripping and adding camera EXIF. They're there
to size demand only; building those tools is a separate decision. Competitor brand names are left out as targets.

Label names differ by language, so the local seeds use each platform's own wording: Instagram's "AI info" is
"Informações de IA" (pt), "Información de IA" (es), "KI-Info" (de), "Yapay zeka bilgisi" (tr),
"Thông tin về AI" (vi), "AI情報" (ja). Check the exact current label text in each language's app.

## Countries & why

| Country | Language people search in | Why |
|---|---|---|
| United States | English | Highest-value traffic; most AI-image users; competitor traffic leader |
| India | English (tech terms), Hinglish in Latin script for how-to questions | Huge volume for free tools; "compress image to 50kb / resize photo for form" demand from exam and government forms |
| Indonesia | Bahasa Indonesia; format names stay English ("heic to jpg" is also typed as-is) | Large mobile-first market, low competition for local-language tool pages |
| Brazil | Portuguese (pt-BR) | Big internet population, strong free-tool demand, fewer native-language tools |
| Mexico (+ LatAm, Spain) | Spanish; Mexico uses "quitar", Spain uses "quitar"/"eliminar" — check both | Covers ~20 countries with one language; your Spanish SynthID keyword shows real demand |
| Germany | German; tech words often English ("Metadaten", "EXIF", "HEIC") | Privacy-conscious audience → metadata/GPS removal fits; we already have DE pages |
| Philippines | English and Taglish | Heavy social/marketplace users (Shopee, Lazada), English search makes pages reusable |
| Turkey | Turkish; formats in Latin ("heic jpg çevirme") | Large search market, weaker competition in Turkish |
| Vietnam | Vietnamese (with diacritics; also typed without them, e.g. "xoa metadata anh") | Fast-growing, low competition; check unaccented variants too |
| Japan | Japanese; format names in Latin ("heic jpg 変換") | High-value market; privacy (位置情報) searches are common |

Also worth a later pass: United Kingdom, Canada, Australia (same English seeds), France, Italy, Russia, South Korea.

## Research order (look these up first)

1. **US + India, Batch 1 tools** — biggest volume, English seeds work in both. Tells you which tools to build first.
2. **"remove synthid" family in all 10 countries** — your core niche; confirms which languages are worth translating first.
3. **Converters (HEIC/WebP/AVIF → JPG) in Indonesia, Brazil, Mexico, Turkey, Vietnam** — high volume, local-language pages face weaker competition than English.
4. **Privacy (remove location / metadata) in Germany and Japan** — privacy-minded markets.
5. **Platform presets (Instagram, WhatsApp, Discord) in India, Philippines, Indonesia, Brazil.**
6. **AI-app pages** last — lower and less predictable volume; only build the ones that show real demand.

For each seed, record: volume, keyword difficulty, CPC, top 3 ranking URLs, and whether the SERP shows tools (good) or articles/videos (harder for a tool page).

## Competitors to look at in Ahrefs/Semrush (verify each)

- Privacy / metadata: removeailabel.com (its privacy tools), jimpl.com, verexif.com, metadata2go.com, exif.tools, imgonline.com.ua, thexifer.net
- Converters: heictojpg.com, cloudconvert.com, convertio.co, freeconvert.com, ezgif.com, iloveimg.com, img2go.com
- Compress / resize: tinypng.com, squoosh.app, imageresizer.com, imagecompressor.com, (India) pi7.org-style "compress to kb" sites
- SynthID: removesynthid.io, removesynthid.com, synthidremove.com

Use their "top pages" and "organic keywords" reports to find seeds this list misses.

## Watch-outs

- **Thin / scaled content:** removeailabel's 7,800 machine-translated pages work today but are exactly what Google's scaled-content policy targets. Translate only pages that show demand, and write each one properly.
- **Search intent mismatch:** "jpg to png transparent" users want background removal; "remove date from photo" often means a visible date stamp. Check the SERP before building.
- **Very competitive heads:** "jpg to pdf", "compress image", "resize image" are dominated by big brands. Target the long tail first (kb sizes, platform presets, specific formats).
- **Brand terms:** don't put Instagram, WhatsApp, Gemini etc. in your domain or logo; using them descriptively in page titles is normal.
- **AI-app pages:** stick to export/format/privacy help. Pages promising to strip AI labels from a specific app's output are out of scope.
- **SynthID:** pages must stay honest about what the tool does; never claim affiliation with Google.
