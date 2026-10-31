import openpyxl, sys, os, json

sys.stdout.reconfigure(encoding='utf-8')

# Load all keywords from FORMATTED.xlsx
wb = openpyxl.load_workbook(r'D:\Nitin\keyword_researcher\proxy-keywords\output\removesynth_seeds_keywords_2026-10-16T15-39-20_FORMATTED.xlsx')
ws_summary = wb['Tool summary']
summary_rows = list(ws_summary.iter_rows(values_only=True))[1:]

# Existing static pages in RemoveSynth
pages_dir = r'd:\Nitin\removesynth\apps\removesynth\src\pages'
static_pages = {f.replace('.astro', '') for f in os.listdir(pages_dir) if f.endswith('.astro')}

with open(r'd:\Nitin\removesynth\apps\removesynth\src\data\pages.json', 'r', encoding='utf-8') as f:
    prog_pages = json.load(f)

built = set(static_pages)
for k in prog_pages.keys():
    built.add(k)

# Add all format pairs and sizes
built.update([
    'jpg-to-png', 'png-to-jpg', 'webp-to-jpg', 'webp-to-png', 'avif-to-jpg', 'avif-to-png',
    'heic-to-png', 'jpg-to-webp', 'png-to-webp', 'image-compressor',
    'compress-image-to-20kb', 'compress-image-to-50kb', 'compress-image-to-100kb', 'compress-image-to-200kb',
    'youtube-thumbnail-resizer', 'geotag-photo', 'resize-image-for-instagram',
    'video-metadata-remover', 'compress-video-for-discord', 'exiftool-online', 'does-it-strip-metadata',
    'pdf-metadata-remover', 'photo-metadata-remover', 'audio-metadata-remover', 'docx-metadata-remover',
    'bulk-metadata-remover', 'anonymous-photo-cleaner', 'photoshop-metadata-cleaner',
    'pdf-resume-metadata-remover', 'invisible-character-remover', 'change-photo-date',
    'add-camera-exif', 'remove-metadata-iphone', 'remove-metadata-android',
    'remove-synthid', 'remove-synthid-from-images', 'remove-synthid-from-audio',
    'remove-synthid-from-video', 'remove-synthid-from-text', 'remove-c2pa-from-video',
    'compress-image-for-discord', 'compress-image-for-whatsapp', 'etsy-photo-cleaner',
    'what-is-synthid', 'what-is-ai-watermark'
])

# Tool mapping keywords
mapping = {
    'JPG to PDF': 'jpg-to-pdf',
    'Image compressor': 'image-compressor',
    'Resize image': 'resize-image',
    'HEIC to JPG': 'heic-to-jpg',
    'WebP to JPG': 'webp-to-jpg',
    'PNG to JPG': 'png-to-jpg',
    'AVIF to JPG': 'avif-to-jpg',
    'HEIC to PNG': 'heic-to-png',
    'WebP to PNG': 'webp-to-png',
    'JPG to PNG': 'jpg-to-png',
    'Instagram: remove location / resize for Instagram': 'resize-image-for-instagram',
    'JPG / PNG to WebP': 'jpg-to-webp',
    'Geotag photo (add / change GPS location)': 'geotag-photo',
    'WhatsApp: send HD / compress / remove location': 'compress-image-for-whatsapp',
    'Discord: compress for upload limit': 'compress-video-for-discord',
    'Video / MP4 metadata remover': 'video-metadata-remover',
    'Remove EXIF data': 'photo-metadata-remover',
    'What is SynthID / SynthID detector (info)': 'what-is-synthid',
    'AI text watermark remover (ChatGPT, Claude…)': 'remove-synthid-from-text',
    'Remove C2PA from AI videos (Sora, Veo, Firefly)': 'remove-c2pa-from-video',
    'PDF metadata remover': 'pdf-metadata-remover',
    'Marketplaces (Etsy/eBay): remove photo metadata before listing': 'etsy-photo-cleaner',
    'Remove GPS / location from photo': 'photo-metadata-remover',
    'Remove metadata from photo': 'photo-metadata-remover',
    'Remove SynthID': 'remove-synthid',
    'Add camera EXIF to image': 'add-camera-exif',
    'Remove author / metadata from PDF (resume, documents)': 'pdf-resume-metadata-remover',
    'Online EXIF stripper & ExifTool web alternative (Metadata2Go, Jimpl, ExifCleaner)': 'exiftool-online',
    'Remove date / time from photo': 'change-photo-date',
    'Remove photo metadata on iPhone': 'remove-metadata-iphone',
    'Remove photo metadata on Android': 'remove-metadata-android',
    'Audio / MP3 tag remover': 'audio-metadata-remover',
    'Word / DOCX metadata remover': 'docx-metadata-remover',
    'Remove AI detection from image': 'remove-synthid-from-images',
    'Remove camera serial number from photos': 'photo-metadata-remover',
    'Change / add date taken on photo': 'change-photo-date',
    'Remove location from video': 'video-metadata-remover',
    'Bulk metadata remover': 'bulk-metadata-remover',
    'Does [platform] remove metadata? (info pages)': 'does-it-strip-metadata',
    'Invisible character remover (text)': 'invisible-character-remover',
    'FLAC / WAV / M4A audio metadata & ID3 cleaner': 'audio-metadata-remover',
    'Document anonymizer & redaction metadata scrubber (Legal, Resume, FOIA)': 'pdf-resume-metadata-remover',
    'Photoshop & Lightroom document history / XMP ancestors cleaner': 'photoshop-metadata-cleaner',
    'Does [Messenger/Chat] strip metadata? (Signal, Telegram, Discord, iMessage, WhatsApp)': 'does-it-strip-metadata',
    'AI Video watermark & C2PA remover (Runway, Kling, Luma, Pika, Sora, Veo)': 'remove-c2pa-from-video',
    'Zero-width space & hidden unicode character cleaner': 'invisible-character-remover',
    'Anonymous photo posting tool (Reddit, 4chan, Marketplace safe share)': 'anonymous-photo-cleaner',
    'YouTube / TikTok: thumbnail and cover size': 'youtube-thumbnail-resizer',
    'C2PA / Content Credentials remover': 'remove-synthid',
    'AI metadata remover': 'remove-synthid',
    'XMP remover': 'photo-metadata-remover',
    'Stable Diffusion / ComfyUI PNG metadata remover': 'photo-metadata-remover'
}

print("=== REMAINING UNCOVERED OR PARTIALLY COVERED CLUSTERS ===")
uncovered_clusters = []
for r in summary_rows:
    tool_name = r[0]
    if not tool_name: continue
    matched_slug = mapping.get(tool_name)
    if not matched_slug:
        uncovered_clusters.append({
            'tool': tool_name,
            'group': r[1],
            'batch': r[2],
            'keywords': r[3],
            'easy_vol': r[9],
            'top_keyword': r[11]
        })

for u in uncovered_clusters:
    print(f"[{u['group']}] {u['tool']} | KWs: {u['keywords']} | Vol: {u['easy_vol']} | Top: {u['top_keyword']}")
