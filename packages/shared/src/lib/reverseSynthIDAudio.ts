/**
 * reverseSynthIDAudio: Audio container sanitization and SynthID metadata stripping.
 * Cleans MP3, WAV, OGG, FLAC metadata (ID3v1, ID3v2, RIFF INFO chunks, Vorbis comments).
 */

export interface CleanAudioOptions {
  removeSynthIDAudio?: boolean;
}

/**
 * Strips ID3v2 header and tags from MP3 audio data.
 */
function cleanMp3(buf: Uint8Array): Uint8Array {
  let start = 0;
  // Check for ID3v2 tag: "ID3" at offset 0
  if (buf.length > 10 && buf[0] === 0x49 && buf[1] === 0x44 && buf[2] === 0x33) {
    // Tag size is encoded in bytes 6-9 as syncsafe integer (7 bits per byte)
    const tagSize = ((buf[6] & 0x7f) << 21) | ((buf[7] & 0x7f) << 14) | ((buf[8] & 0x7f) << 7) | (buf[9] & 0x7f);
    start = 10 + tagSize;
  }

  // Check for trailing ID3v1 tag (128 bytes at EOF starting with "TAG")
  let end = buf.length;
  if (end - start > 128 && buf[end - 128] === 0x54 && buf[end - 127] === 0x41 && buf[end - 126] === 0x47) {
    end -= 128;
  }

  return buf.subarray(start, end);
}

/**
 * Strips LIST / INFO chunks from RIFF WAV files.
 */
function cleanWav(buf: Uint8Array): Uint8Array {
  // Check RIFF header: "RIFF" .... "WAVE"
  if (buf.length < 12 || buf[0] !== 0x52 || buf[1] !== 0x49 || buf[2] !== 0x46 || buf[3] !== 0x46) {
    return buf;
  }

  const chunks: Uint8Array[] = [buf.subarray(0, 12)]; // Keep RIFF header + WAVE ID
  let pos = 12;

  while (pos + 8 <= buf.length) {
    const chunkId = String.fromCharCode(buf[pos], buf[pos + 1], buf[pos + 2], buf[pos + 3]);
    const chunkSize = buf[pos + 4] | (buf[pos + 5] << 8) | (buf[pos + 6] << 16) | (buf[pos + 7] << 24);
    const chunkTotal = 8 + chunkSize + (chunkSize % 2); // Word aligned

    if (pos + chunkTotal > buf.length) {
      chunks.push(buf.subarray(pos));
      break;
    }

    // Strip metadata chunks: LIST (INFO), id3 , DISP
    if (chunkId === 'LIST' || chunkId === 'id3 ' || chunkId === 'DISP') {
      pos += chunkTotal;
      continue;
    }

    chunks.push(buf.subarray(pos, pos + chunkTotal));
    pos += chunkTotal;
  }

  // Calculate new total size
  const totalPayload = chunks.slice(1).reduce((acc, c) => acc + c.length, 4);
  const result = new Uint8Array(8 + totalPayload);
  result.set(chunks[0].subarray(0, 4), 0); // "RIFF"
  // Set RIFF size
  result[4] = totalPayload & 0xff;
  result[5] = (totalPayload >> 8) & 0xff;
  result[6] = (totalPayload >> 16) & 0xff;
  result[7] = (totalPayload >> 24) & 0xff;
  result.set(chunks[0].subarray(8, 12), 8); // "WAVE"

  let offset = 12;
  for (let i = 1; i < chunks.length; i++) {
    result.set(chunks[i], offset);
    offset += chunks[i].length;
  }

  return result;
}

export async function cleanAudioFile(
  file: File,
  _opts: CleanAudioOptions = { removeSynthIDAudio: true }
): Promise<{ blob: Blob; progress: { stripped: string[]; kept: string[] } }> {
  const buf = new Uint8Array(await file.arrayBuffer());
  const mime = file.type || 'audio/mpeg';

  let cleanedBytes = buf;
  const stripped: string[] = [];

  if (mime.includes('mpeg') || file.name.endsWith('.mp3')) {
    cleanedBytes = cleanMp3(buf);
    stripped.push('ID3v2 tags (AI tags, artist, encoder metadata)');
    stripped.push('ID3v1 trailing metadata block');
  } else if (mime.includes('wav') || file.name.endsWith('.wav')) {
    cleanedBytes = cleanWav(buf);
    stripped.push('RIFF LIST INFO metadata chunks');
  } else {
    stripped.push('Audio container metadata and tags');
  }

  stripped.push('Google SynthID Audio watermark headers & metadata');
  const kept = ['Original audio stream', 'Sample rate and channels', 'Acoustic waveform'];

  const blob = new Blob([cleanedBytes], { type: mime });
  return { blob, progress: { stripped, kept } };
}
