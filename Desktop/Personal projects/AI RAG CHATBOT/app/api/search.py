from fastapi import APIRouter, HTTPException

from app.db.chroma_db import ChromaDB
from app.logger import get_logger, truncate

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)
logger = get_logger("api.search")


@router.get("/")
async def search(query: str):
    logger.info("Search request received query=%s", truncate(query))

    try:
        results = ChromaDB.search(query)
    except Exception:
        logger.exception(
            "Search request failed query=%s",
            truncate(query),
        )
        raise HTTPException(
            status_code=500,
            detail="Failed to execute search",
        )

    result_count = len(results.get("documents", [[]])[0])
    logger.info(
        "Search request completed query=%s results=%s",
        truncate(query),
        result_count,
    )
    return results
