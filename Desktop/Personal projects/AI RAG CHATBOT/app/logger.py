import logging
import os
import sys
from logging.handlers import RotatingFileHandler

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = os.getenv(
    "LOG_FORMAT",
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", str(10 * 1024 * 1024)))
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", "5"))

_CONFIGURED = False


def setup_logging() -> logging.Logger:
    """Configure application logging once at startup."""
    global _CONFIGURED

    level = getattr(logging, LOG_LEVEL, logging.INFO)
    root_logger = logging.getLogger("rag-app")

    if _CONFIGURED:
        return root_logger

    root_logger.setLevel(level)
    root_logger.propagate = False

    formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    if LOG_FILE:
        log_dir = os.path.dirname(LOG_FILE)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=LOG_MAX_BYTES,
            backupCount=LOG_BACKUP_COUNT,
            encoding="utf-8",
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    _CONFIGURED = True
    root_logger.info(
        "Logging initialized level=%s file=%s",
        LOG_LEVEL,
        LOG_FILE or "disabled",
    )
    return root_logger


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a namespaced child logger under rag-app."""
    if name is None:
        return logging.getLogger("rag-app")

    normalized = name.removeprefix("app.")
    return logging.getLogger(f"rag-app.{normalized}")


def truncate(text: str, max_len: int = 120) -> str:
    """Truncate long strings for safe log output."""
    if len(text) <= max_len:
        return text
    return f"{text[:max_len]}..."
