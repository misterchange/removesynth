import os
import re

pages_dir = r'd:\Nitin\removesynth\apps\removesynth\src\pages'

# Upgrades dictionary for remaining tool pages
upgrades = {
    'exif-editor.astro': {
        'title': 'EXIF Editor: Edit, Add & Remove Photo Metadata Free',
        'desc': 'Modify, add, or delete individual EXIF tags in your photos. Edit artist, copyright, camera model, lens, and capture dates with instant private in-browser download.',
    },
    'audio-metadata-remover.astro': {
        'title': 'Audio Metadata Remover: Clean ID3 Tags & Audio Free',
        'desc': 'Remove ID3 tags, artist names, album art, and encoder metadata from MP3, WAV, FLAC, and M4A audio files. Fast client-side tool with zero server uploads.',
    },
    'add-camera-exif.astro': {
        'title': 'Add Camera EXIF to Photo: Mock Camera Metadata Online',
        'desc': 'Add realistic camera EXIF tags, focal length, lens details, and exposure settings to AI and digital photos. Free client-side tool with zero cloud uploads.',
    },
    'change-photo-date.astro': {
        'title': 'Change Photo Date Taken: Edit EXIF Timestamps Free',
        'desc': 'Change or remove the Date Taken, Modify Date, and EXIF timestamps on digital photos. Free in-browser metadata date editor with zero cloud file uploads.',
    },
    'bulk-metadata-remover.astro': {
        'title': 'Bulk Metadata Remover: Strip EXIF from Photos Free',
        'desc': 'Remove EXIF, GPS, IPTC, and camera metadata from multiple photos simultaneously. Batch clean up to 50 images in your browser with zero server uploads.',
    },
    'anonymous-photo-cleaner.astro': {
        'title': 'Anonymous Photo Sanitizer: Safe Photo Share Online',
        'desc': 'Sanitize private photos before sharing on Reddit, 4chan, or marketplaces. Strip GPS coordinates, device serials, and camera metadata 100% in your browser.',
    },
    'geotag-photo.astro': {
        'title': 'Geotag Photo Online: Add or Change GPS on Photos Free',
        'desc': 'Add, edit, or remove GPS coordinates and geographic tags on your photos. In-browser photo geotagging tool with interactive map and zero server uploads.',
    },
    'photoshop-metadata-cleaner.astro': {
        'title': 'Photoshop Metadata Cleaner: Strip Document Ancestors',
        'desc': 'Remove bloated Adobe Photoshop document ancestors, XMP history, and edit logs from JPG and PNG files. Reduce bloated file sizes 100% in your browser.',
    },
    'docx-metadata-remover.astro': {
        'title': 'Word & DOCX Metadata Remover: Clean Author History',
        'desc': 'Remove author names, company tags, revision history, and editing time from Word DOCX documents. Free private client-side sanitizer with zero cloud uploads.',
    },
    'pdf-resume-metadata-remover.astro': {
        'title': 'PDF Resume Metadata Remover: Anonymize Job Submissions',
        'desc': 'Clean author names, creation timestamps, and software signatures from PDF resumes and CVs. Anonymize your job applications 100% privately in your browser.',
    },
    'ai-image-resizer.astro': {
        'title': 'AI Image Resizer: Fit Midjourney & DALL-E Art Free',
        'desc': 'Resize and pad AI art from Midjourney, DALL-E, and Stable Diffusion to standard aspect ratios without cropping. Free client-side tool with zero server uploads.',
    },
    'resize-image-for-instagram.astro': {
        'title': 'Instagram Photo Resizer: 1:1, 4:5 & 9:16 No-Crop Free',
        'desc': 'Resize photos for Instagram feed, portrait 4:5, and 9:16 Stories without cropping. Add custom blurred or solid borders 100% in-browser with zero uploads.',
    },
    'resize-image.astro': {
        'title': 'Image Resizer: Resize Photos Online Free & Private',
        'desc': 'Resize images to exact dimensions or percentage scale in your browser. Fast client-side image resizer supporting JPG, PNG, and WebP with zero cloud uploads.',
    },
    'compress-image-to-kb.astro': {
        'title': 'Compress Image to KB: Reduce Photo to 20KB, 50KB, 100KB',
        'desc': 'Compress photos to exact target file sizes like 20KB, 50KB, 100KB, or 200KB. Perfect for portal uploads, job applications, and ID cards with zero uploads.',
    },
    'compress-video-for-discord.astro': {
        'title': 'Compress Video for Discord: Under 10MB & 25MB Free',
        'desc': 'Compress videos to fit under Discord 10MB free tier and 25MB Nitro limits. Fast in-browser video compression with no watermarks and zero server uploads.',
    },
    'remove-metadata-iphone.astro': {
        'title': 'Remove Photo Metadata on iPhone: Strip GPS & EXIF Free',
        'desc': 'Remove GPS location coordinates and camera metadata from iPhone photos directly in mobile Safari. Free in-browser tool with zero server uploads or apps.',
    },
    'remove-metadata-android.astro': {
        'title': 'Remove Photo Metadata on Android: Wipe GPS & EXIF Free',
        'desc': 'Wipe GPS location tags, camera details, and EXIF metadata from Android photos. Works in mobile Chrome with zero app installation and zero server uploads.',
    },
    'exiftool-online.astro': {
        'title': 'ExifTool Online: Free In-Browser Metadata Viewer',
        'desc': 'Inspect and strip detailed EXIF, IPTC, and XMP metadata from your photos in your browser. Fast client-side ExifTool inspector with zero server file uploads.',
    },
    'invisible-character-remover.astro': {
        'title': 'Invisible Character Remover: Strip Zero-Width Unicode',
        'desc': 'Remove zero-width spaces, invisible characters, and hidden unicode tags from text. Clean copy-paste artifacts and tracking watermarks 100% in your browser.',
    },
    'youtube-thumbnail-resizer.astro': {
        'title': 'YouTube Thumbnail Resizer: Exact 1280x720 Size Free',
        'desc': 'Resize and optimize images for YouTube thumbnails at exact 1280x720 dimensions under 2MB. Fast in-browser tool with zero watermarks and zero server uploads.',
    },
    'etsy-photo-cleaner.astro': {
        'title': 'Etsy & eBay Photo Cleaner: Safe Listing Prep Online',
        'desc': 'Clean camera metadata, GPS location, and editing signatures from listing photos for Etsy and eBay. Free in-browser photo prep tool with zero cloud uploads.',
    },
    'does-it-strip-metadata.astro': {
        'title': 'Does It Strip Metadata? Platform Privacy Checker 2026',
        'desc': 'Find out which social networks, messaging apps, and cloud drives strip EXIF metadata from photos. Comprehensive 2026 privacy audit of 30+ top platforms.',
    },
}

for fname, data in upgrades.items():
    fpath = os.path.join(pages_dir, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update title
    content = re.sub(r"const title\s*=\s*['\"`].*?['\"`];", f"const title = '{data['title']}';", content)
    
    # Update description
    content = re.sub(r"const description\s*=\s*['\"`].*?['\"`];", f"const description =\n  '{data['desc']}';", content, flags=re.DOTALL)
    
    # Replace dashes and emojis
    content = content.replace('—', '-').replace('–', '-')
    content = re.sub(r'[\U0001F300-\U0001FAFF]', '', content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {fname}: Title len {len(data["title"])}, Desc len {len(data["desc"])}')

print('Batch metadata updates completed successfully!')
