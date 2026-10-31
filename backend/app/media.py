"""Identify uploads by their file signature (magic bytes), not the client-supplied Content-Type."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MediaType:
    mime: str
    ext: str
    kind: str  # "image" | "video" | "audio"


PNG = MediaType("image/png", ".png", "image")
JPEG = MediaType("image/jpeg", ".jpg", "image")
WEBP = MediaType("image/webp", ".webp", "image")
MP4 = MediaType("video/mp4", ".mp4", "video")
MOV = MediaType("video/quicktime", ".mov", "video")
WEBM = MediaType("video/webm", ".webm", "video")
MP3 = MediaType("audio/mpeg", ".mp3", "audio")
WAV = MediaType("audio/wav", ".wav", "audio")
M4A = MediaType("audio/mp4", ".m4a", "audio")
OGG = MediaType("audio/ogg", ".ogg", "audio")
FLAC = MediaType("audio/flac", ".flac", "audio")


def sniff(head: bytes) -> MediaType | None:
    """Return the media type for the first bytes of a file, or None if unsupported."""
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return PNG
    if head.startswith(b"\xff\xd8\xff"):
        return JPEG
    if head[:4] == b"RIFF":
        if head[8:12] == b"WEBP":
            return WEBP
        if head[8:12] == b"WAVE":
            return WAV
        return None
    if head.startswith(b"\x1a\x45\xdf\xa3"):
        return WEBM
    if head[4:8] == b"ftyp":
        brand = head[8:12]
        if brand == b"qt  ":
            return MOV
        if brand in (b"M4A ", b"M4B "):
            return M4A
        return MP4
    if head.startswith(b"ID3") or (len(head) > 1 and head[0] == 0xFF and head[1] & 0xE0 == 0xE0):
        return MP3
    if head.startswith(b"OggS"):
        return OGG
    if head.startswith(b"fLaC"):
        return FLAC
    return None
