from fastapi import APIRouter, HTTPException

from app.db.chroma_db import ChromaDB
from app.logger import get_logger

router = APIRouter(
    prefix="/debug",
    tags=["Debug"],
)
logger = get_logger("api.debug")


@router.get("/")
async def debug_db():
    logger.info("Debug DB stats request received")

    try:
        count = ChromaDB.collection.count()
    except Exception:
        logger.exception("Debug DB stats request failed")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve database stats",
        )

    logger.info("Debug DB stats completed stored_chunks=%s", count)
    return {
        "stored_chunks": count,
    }
