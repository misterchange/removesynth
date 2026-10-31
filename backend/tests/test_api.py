import shutil

import pytest
from fastapi.testclient import TestClient

from app import engine, main
from app.ratelimit import SlidingWindowLimiter

PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 64
JPEG = b"\xff\xd8\xff\xe0" + b"\x00" * 64
MP4 = b"\x00\x00\x00\x18ftypisom" + b"\x00" * 64


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(main, "limiter", SlidingWindowLimiter(100))
    return TestClient(main.app)


@pytest.fixture
def copy_engine(monkeypatch):
    """Stand-in engine that copies the input, so the API plumbing can be tested."""
    monkeypatch.setattr(engine, "process", lambda src, dst, media: shutil.copyfile(src, dst))


def upload(client, data, name="photo.png", **kw):
    return client.post("/process", files={"file": (name, data, "application/octet-stream")}, **kw)


def test_health(client):
    assert client.get("/health").json() == {"ok": True}


def test_engine_not_configured_returns_501(client):
    r = upload(client, PNG)
    assert r.status_code == 501
    assert "not configured" in r.text


@pytest.mark.parametrize(
    "data,name,mime,filename",
    [
        (PNG, "photo.png", "image/png", "photo-removesynth.png"),
        (JPEG, "photo.jpeg", "image/jpeg", "photo-removesynth.jpg"),
        (MP4, "clip.mp4", "video/mp4", "clip-removesynth.mp4"),
        (b"ID3\x04" + b"\x00" * 64, "song.mp3", "audio/mpeg", "song-removesynth.mp3"),
        (b"RIFF\x00\x00\x00\x00WAVEfmt " + b"\x00" * 64, "voice.wav", "audio/wav", "voice-removesynth.wav"),
        (b"\x00\x00\x00\x20ftypM4A " + b"\x00" * 64, "track.m4a", "audio/mp4", "track-removesynth.m4a"),
    ],
)
def test_success_returns_file(client, copy_engine, data, name, mime, filename):
    r = upload(client, data, name)
    assert r.status_code == 200
    assert r.headers["content-type"] == mime
    assert filename in r.headers["content-disposition"]
    assert r.content == data


def test_type_is_sniffed_not_trusted(client, copy_engine):
    r = upload(client, b"GIF89a" + b"\x00" * 64, "fake.png")
    assert r.status_code == 415


def test_empty_file(client):
    assert upload(client, b"").status_code == 400


def test_too_large(client, monkeypatch):
    monkeypatch.setattr(main.settings.__class__, "max_upload_bytes", property(lambda self: 100))
    assert upload(client, PNG + b"\x00" * 200).status_code == 413


def test_processing_error_is_422(client, monkeypatch):
    def fail(src, dst, media):
        raise engine.ProcessingError("Could not read this file.")

    monkeypatch.setattr(engine, "process", fail)
    r = upload(client, PNG)
    assert r.status_code == 422
    assert r.text == "Could not read this file."


def test_rate_limit(client, copy_engine, monkeypatch):
    monkeypatch.setattr(main, "limiter", SlidingWindowLimiter(2))
    assert upload(client, PNG).status_code == 200
    assert upload(client, PNG).status_code == 200
    r = upload(client, PNG)
    assert r.status_code == 429
    assert "retry-after" in r.headers


def test_cors_allows_site_origin(client, copy_engine):
    r = upload(client, PNG, headers={"Origin": "https://removesynth.com"})
    assert r.headers["access-control-allow-origin"] == "https://removesynth.com"


def test_cors_blocks_other_origin(client, copy_engine):
    r = upload(client, PNG, headers={"Origin": "https://evil.example"})
    assert "access-control-allow-origin" not in r.headers


@pytest.mark.parametrize("use_engine", [True, False])
def test_temp_files_are_deleted(client, monkeypatch, use_engine):
    created = []
    real_mkdtemp = main.tempfile.mkdtemp

    def tracking_mkdtemp(**kw):
        created.append(real_mkdtemp(**kw))
        return created[-1]

    monkeypatch.setattr(main.tempfile, "mkdtemp", tracking_mkdtemp)
    if use_engine:
        monkeypatch.setattr(engine, "process", lambda src, dst, media: shutil.copyfile(src, dst))
    upload(client, PNG)
    assert created and not any(main.Path(d).exists() for d in created)
