"""Processing engine hook.

The API calls `process()` for every validated upload. This file is intentionally left
without an implementation: plug your own engine in here. Until then the API answers
uploads with 501 Not Implemented, and the site shows that message to the user.
"""

from pathlib import Path

from .media import MediaType


class EngineNotConfigured(Exception):
    pass


class ProcessingError(Exception):
    """Raise this from your engine for a failure the user should see (e.g. unreadable file)."""


def process(src: Path, dst: Path, media: MediaType) -> None:
    """Read the upload at `src` and write the result to `dst` in the same format as `media`.

    `dst` already has the right extension. Raise ProcessingError for user-facing failures.
    """
    raise EngineNotConfigured("Processing engine is not configured on this server.")
