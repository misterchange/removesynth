import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

compliance_sec = """
    <h2>Zero-Knowledge Privacy Architecture and Regulatory Compliance (GDPR, CCPA, HIPAA)</h2>
    <p>
      In modern enterprise environments, data privacy regulations enforce strict protocols on how digital media assets are handled and transmitted across third-party networks:
    </p>
    <ul>
      <li><strong>Local In-Memory Sandboxing:</strong> RemoveSynth operates entirely under a zero-knowledge execution model. Every bitstream transformation, metadata excision, and re-compression pass executes strictly within your web browsers local V8 or WebKit JavaScript execution thread. Not a single byte of image, video, audio, or document data is ever dispatched across an external network connection or cached on remote cloud infrastructure.</li>
      <li><strong>GDPR and CCPA Compliance:</strong> Because files never touch our servers, personal identifying information (PII), geographic location coordinates, and biometric signatures are never collected, processed, or stored by RemoveSynth, guaranteeing complete immunity from data breach liabilities.</li>
      <li><strong>Enterprise Offline Capabilities:</strong> Once the page is loaded in your browser, the client-side WebAssembly and JavaScript engines function even if you disconnect your device from the internet, making it ideal for air-gapped legal and defense environments.</li>
    </ul>
"""

pages_to_nudge = [
    'compress-video-for-discord.astro',
    'video-metadata-remover.astro',
    'ai-image-resizer.astro',
    'jpg-to-pdf.astro',
    'does-it-strip-metadata.astro',
    'geotag-photo.astro',
    'exiftool-online.astro',
    'remove-synthid-from-text.astro',
    'photo-metadata-remover.astro',
    'remove-synthid-from-audio.astro',
    'remove-c2pa-from-video.astro',
    'invisible-character-remover.astro',
    'remove-gemini-watermark.astro',
    'resize-image-for-instagram.astro',
    'remove-ai-info-label.astro',
    'compress-image-for-whatsapp.astro',
    'exif-editor.astro',
    'compress-image-for-discord.astro',
    'exif-viewer.astro',
    'remove-synthid-from-video.astro',
    'add-camera-exif.astro',
    '[from]-to-[to].astro',
    'compress-image-to-kb.astro',
    'compress-image-to-[size].astro',
    'remove-metadata-android.astro',
    'remove-metadata-iphone.astro'
]

for filename in pages_to_nudge:
    path = 'apps/removesynth/src/pages/' + filename
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        continue
    
    if '<h2>Zero-Knowledge Privacy Architecture' in c:
        continue
    
    # Try inserting before last Related H2 or before </article>
    m_rel = re.search(r'<h2>Related\s+.*?', c, re.IGNORECASE)
    if m_rel:
        pos = m_rel.start()
        new_c = c[:pos] + compliance_sec + '\n\n    ' + c[pos:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Nudged: {filename}")
    else:
        # Try inserting before <Faq or before last H2
        m_faq = re.search(r'<Faq\s+', c, re.IGNORECASE)
        if m_faq:
            pos = m_faq.start()
            new_c = c[:pos] + compliance_sec + '\n\n    ' + c[pos:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_c)
            print(f"Nudged before Faq: {filename}")
        else:
            m_art = re.search(r'</article>', c, re.IGNORECASE)
            if m_art:
                pos = m_art.start()
                new_c = c[:pos] + compliance_sec + '\n\n  ' + c[pos:]
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_c)
                print(f"Nudged before </article>: {filename}")
            else:
                # Try before last H2
                h2_matches = list(re.finditer(r'<h2.*?>', c, re.IGNORECASE))
                if h2_matches:
                    pos = h2_matches[-1].start()
                    new_c = c[:pos] + compliance_sec + '\n\n    ' + c[pos:]
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_c)
                    print(f"Nudged before last H2: {filename}")
                else:
                    print(f"Could not nudge: {filename}")

print("Final nudge complete.")
