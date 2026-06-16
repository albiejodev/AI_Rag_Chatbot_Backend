import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from app.api.chat import router as chat_router
from app.api.debug import router as debug_router
from app.api.document import router as document_router
from app.api.search import router as search_router
from app.api.upload import router as upload_router
from app.logger import get_logger, setup_logging

logger = get_logger("main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("Application starting title=%s", app.title)
    yield
    logger.info("Application shutting down")


app = FastAPI(
    title="AI RAG Chatbot",
    lifespan=lifespan,
)

app.include_router(upload_router)
app.include_router(debug_router)
app.include_router(search_router)
app.include_router(chat_router)
app.include_router(document_router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    client_host = request.client.host if request.client else "unknown"

    logger.info(
        "Request started method=%s path=%s client=%s",
        request.method,
        request.url.path,
        client_host,
    )

    try:
        response = await call_next(request)
    except Exception:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.exception(
            "Request failed method=%s path=%s duration_ms=%.2f",
            request.method,
            request.url.path,
            duration_ms,
        )
        raise

    duration_ms = (time.perf_counter() - start) * 1000
    logger.info(
        "Request completed method=%s path=%s status=%s duration_ms=%.2f",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


@app.get("/")
async def health_check():
    logger.debug("Health check requested")
    return {
        "status": "healthy",
    }
