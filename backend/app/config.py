import os
from dataclasses import dataclass, field


def _list(name: str, default: str) -> list[str]:
    raw = os.getenv(name, default)
    if raw.strip() == "*":
        return ["*"]
    return [v.strip() for v in raw.split(",") if v.strip()]


@dataclass(frozen=True)
class Settings:
    allowed_origins: list[str] = field(
        default_factory=lambda: _list(
            "ALLOWED_ORIGINS",
            "*",
        )
    )
    max_upload_mb: int = int(os.getenv("MAX_UPLOAD_MB", "50"))
    rate_limit_per_minute: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "10"))
    # Trust X-Forwarded-For / CF-Connecting-IP only when running behind a proxy you control.
    trust_proxy: bool = os.getenv("TRUST_PROXY", "false").lower() == "true"

    @property
    def max_upload_bytes(self) -> int:
        return self.max_upload_mb * 1024 * 1024


settings = Settings()
