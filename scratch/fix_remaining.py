import os, re

pages_dir = r'd:\Nitin\removesynth\apps\removesynth\src\pages'

adjustments = {
    'social-media-safe-zones.astro': {
        'desc': 'Interactive safe zone simulator for Instagram Reels, TikTok, YouTube Shorts, and Stories. Preview overlays to prevent app UI from obstructing your text.' # 155
    },
    'remove-synthid-from-text.astro': {
        'desc': 'Neutralize Google DeepMind SynthID Text watermarks and AI writing patterns. Free in-browser tool to sanitize n-gram tournament chains and strip zero-width code.' # 159
    },
    'compress-image-for-discord.astro': {
        'title': 'Compress Image for Discord: Under 10MB & 25MB Free',
        'desc': 'Compress images to fit under Discord 10MB free tier and 25MB Nitro limits. Fast in-browser tool to resize and optimize JPG and PNG files with zero uploads.' # 155
    },
    'compress-image-for-whatsapp.astro': {
        'title': 'Compress Image for WhatsApp: Send High Quality Free',
        'desc': 'Compress photos for WhatsApp without aggressive blur or artifacting. Optimize image resolution and file size in your browser with zero cloud server uploads.' # 157
    },
    'how-to-remove-synthid.astro': {
        'title': 'How to Remove SynthID from Images: Complete Guide',
        'desc': 'Learn how to detect and remove Google DeepMind SynthID watermarks from AI images. Detailed technical guide covering frequency dispersion and metadata purging.' # 159
    },
    'image-converter.astro': {
        'title': 'Image Converter: Convert WebP, AVIF, HEIC & JPG Free',
        'desc': 'Convert between WebP, AVIF, HEIC, PNG, and JPG image formats directly in your web browser. Fast client-side image converter with zero cloud server file uploads.' # 160
    },
    'remove-c2pa-from-video.astro': {
        'title': 'Remove C2PA from Video: Clean MP4 & MOV Manifests',
        'desc': 'Remove C2PA Content Credentials and provenance manifests from MP4, WebM, and MOV video files. Lossless container sanitizer with zero re-encoding or quality loss.' # 160
    },
    'remove-synthid.astro': {
        'title': 'Remove SynthID Online Free: Images, Video & Audio',
        'desc': 'Neutralize Google DeepMind SynthID watermarks across AI images, video, and audio files. Free client-side tools with zero cloud uploads and full creator privacy.' # 159
    },
}

for fname, data in adjustments.items():
    path = os.path.join(pages_dir, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'title' in data:
        content = re.sub(r"const title\s*=\s*['\"`].*?['\"`];", f"const title = '{data['title']}';", content)
    if 'desc' in data:
        content = re.sub(r"const description\s*=\s*['\"`].*?['\"`];", f"const description =\n  '{data['desc']}';", content, flags=re.DOTALL)
    content = content.replace('—', '-').replace('–', '-')
    content = re.sub(r'[\U0001F300-\U0001FAFF]', '', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fine-tuned {fname}')

print('All fine-tuning done!')
