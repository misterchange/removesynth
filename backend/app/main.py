import shutil
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse, Response

from . import engine
from .config import settings
from .media import sniff
from .ratelimit import SlidingWindowLimiter

app = FastAPI(title="RemoveSynth API", docs_url=None, redoc_url=None, openapi_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
    max_age=600,
)

limiter = SlidingWindowLimiter(settings.rate_limit_per_minute)
CHUNK = 1024 * 1024


@app.exception_handler(HTTPException)
async def plain_errors(_: Request, exc: HTTPException):
    # The site shows the response body to the user, so keep errors as short plain text.
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code, headers=exc.headers)


def client_ip(request: Request) -> str:
    if settings.trust_proxy:
        forwarded = request.headers.get("cf-connecting-ip") or request.headers.get("x-forwarded-for", "")
        if forwarded:
            return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/process")
async def process(request: Request, file: UploadFile = File(...)):
    allowed, retry_after = limiter.allow(client_ip(request))
    if not allowed:
        raise HTTPException(429, "Too many requests. Please wait a minute and try again.", {"Retry-After": str(retry_after)})

    workdir = Path(tempfile.mkdtemp(prefix="rs-"))
    try:
        src = workdir / "input"
        size = 0
        head = b""
        with src.open("wb") as out:
            while chunk := await file.read(CHUNK):
                if not head:
                    head = chunk[:32]
                size += len(chunk)
                if size > settings.max_upload_bytes:
                    raise HTTPException(413, f"File is larger than {settings.max_upload_mb} MB.")
                out.write(chunk)
        if size == 0:
            raise HTTPException(400, "The uploaded file is empty.")

        media = sniff(head)
        if media is None:
            raise HTTPException(415, "Unsupported file type. Use PNG, JPG, WebP, MP4, WebM, MOV, MP3, WAV, M4A, OGG or FLAC.")

        src = src.rename(workdir / f"input{media.ext}")
        dst = workdir / f"output{media.ext}"
        try:
            await run_in_threadpool(engine.process, src, dst, media)
        except engine.EngineNotConfigured as e:
            raise HTTPException(501, str(e))
        except engine.ProcessingError as e:
            raise HTTPException(422, str(e))

        if not dst.is_file() or dst.stat().st_size == 0:
            raise HTTPException(500, "Processing produced no output.")

        stem = Path(file.filename or "file").stem[:100] or "file"
        data = dst.read_bytes()
        return Response(
            data,
            media_type=media.mime,
            headers={
                "Content-Disposition": f'attachment; filename="{stem}-removesynth{media.ext}"',
                "Cache-Control": "no-store",
            },
        )
    finally:
        await file.close()
        shutil.rmtree(workdir, ignore_errors=True)
