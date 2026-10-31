import time
from collections import defaultdict, deque
from threading import Lock


class SlidingWindowLimiter:
    """In-memory per-key limiter. Fine for a single instance; use Redis or Cloudflare rules when scaling out."""

    def __init__(self, limit: int, window_seconds: float = 60.0):
        self.limit = limit
        self.window = window_seconds
        self._hits: dict[str, deque[float]] = defaultdict(deque)
        self._lock = Lock()

    def allow(self, key: str) -> tuple[bool, int]:
        """Record a hit for `key`. Returns (allowed, seconds_until_retry)."""
        now = time.monotonic()
        with self._lock:
            hits = self._hits[key]
            while hits and now - hits[0] >= self.window:
                hits.popleft()
            if len(hits) >= self.limit:
                return False, max(1, int(self.window - (now - hits[0])) + 1)
            hits.append(now)
            if len(self._hits) > 10_000:
                self._prune(now)
            return True, 0

    def _prune(self, now: float) -> None:
        stale = [k for k, h in self._hits.items() if not h or now - h[-1] >= self.window]
        for k in stale:
            del self._hits[k]
