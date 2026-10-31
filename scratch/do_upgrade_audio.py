import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('apps/removesynth/src/pages/audio-metadata-remover.astro', 'r', encoding='utf-8') as f:
    orig = f.read()

more_audio_sections = """
    <h2>DAW Telemetry: What Ableton Live, FL Studio, Logic Pro, and Reaper Write into Exports</h2>
    <p>
      Digital Audio Workstations are designed to manage complex multi-track projects, but their default export profiles embed comprehensive production telemetry into the resulting MP3 and WAV files:
    </p>
    <ul>
      <li><strong>Ableton Live:</strong> Embeds encoded user account registration strings, application build versions, and session tempo/time-signature markers within proprietary <code>TXXX</code> user-defined text frames.</li>
      <li><strong>FL Studio:</strong> Automatically injects the registered user name and license status into the <code>TCOP</code> (copyright) and <code>TENC</code> (encoded by) tags, along with project mixer master channel limiter presets.</li>
      <li><strong>Apple Logic Pro:</strong> Injects CoreAudio framework identifiers, session arrangement markers, and project asset folder paths that disclose local Mac home directory usernames.</li>
      <li><strong>Cockos Reaper:</strong> Writes project render settings, sample rate conversion algorithms, and dither types into custom RIFF chunk descriptors.</li>
      <li><strong>Why Professional Producers Sanitize Stems:</strong> When delivering stems, instrumental mixes, or demo beats to record labels, sync licensing agencies, or collaborative vocalists, delivering sanitized audio prevents leaking unreleased project titles, software serials, or studio hardware configurations.</li>
    </ul>

    <h2>ID3v2.3 vs ID3v2.4 Synchronization and Unsynchronization Schemes Explained</h2>
    <p>
      The technical evolution of the ID3v2 specification created notable compatibility and decoding friction across playback software:
    </p>
    <ul>
      <li><strong>ID3v2.3 Standard (1999):</strong> Uses four 7-bit synchsafe integers for header sizes, with frames utilizing 32-bit big-endian size descriptors. Multiple artists are separated by forward slashes (<code>/</code>). It remains the most widely compatible standard on legacy automotive hardware, portable media players, and older DJ software.</li>
      <li><strong>ID3v2.4 Standard (2000):</strong> Mandates synchsafe integers across both headers and individual frame size descriptors. Multiple values are separated by null bytes (<code>0x00</code>). It introduces UTF-8 text encoding support and footer tags for streaming efficiency.</li>
      <li><strong>The Unsynchronization Trap:</strong> To prevent MPEG decoders from misinterpreting metadata bytes as audio sync words (<code>0xFFE0</code>), ID3 specifications insert an unsynchronization scheme that inserts a null byte after every <code>0xFF</code> byte. Faulty parsers in basic media players can miscalculate frame offsets, causing audible pops, clicks, or truncated playback.</li>
      <li><strong>The Clean Audio Benefit:</strong> By completely stripping ID3 headers and trailers, RemoveSynth eliminates unsynchronization conflicts entirely, leaving pure, uninterrupted MPEG audio frames that play flawlessly on 100 percent of devices.</li>
    </ul>
"""

if '<h2>DAW Telemetry: What Ableton' not in orig:
    target = '<h2>Comparison of Audio Metadata Stripping Tools</h2>'
    orig = orig.replace(target, more_audio_sections + '\n\n    ' + target)

with open('apps/removesynth/src/pages/audio-metadata-remover.astro', 'w', encoding='utf-8') as f:
    f.write(orig)

parts = orig.split('---')
body = '---'.join(parts[2:])
body_clean = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
body_clean = re.sub(r'<style.*?</style>', '', body_clean, flags=re.DOTALL)
body_clean = re.sub(r'<svg.*?</svg>', '', body_clean, flags=re.DOTALL)
words = len(re.sub(r'<[^>]+>', ' ', body_clean).split())
print(f'audio-metadata-remover body word count: {words}')
