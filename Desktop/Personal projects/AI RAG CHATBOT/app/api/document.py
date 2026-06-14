from fastapi import APIRouter, HTTPException

from app.db.chroma_db import ChromaDB
from app.logger import get_logger

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)
logger = get_logger("api.document")


@router.get("/")
async def get_documents():
    logger.info("List documents request received")

    try:
        documents = ChromaDB.get_documents()
    except Exception:
        logger.exception("List documents request failed")
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve documents",
        )

    logger.info("List documents completed count=%s", len(documents))
    return documents


@router.delete("/{document_id}")
async def delete_document(document_id: str):
    logger.info(
        "Delete document request received document_id=%s",
        document_id,
    )

    try:
        deleted = ChromaDB.delete_document(document_id)
    except Exception:
        logger.exception(
            "Delete document request failed document_id=%s",
            document_id,
        )
        raise HTTPException(
            status_code=500,
            detail="Failed to delete document",
        )

    if not deleted:
        logger.warning(
            "Delete document not found document_id=%s",
            document_id,
        )
        return {
            "message": "Document not found",
        }

    logger.info(
        "Delete document completed document_id=%s",
        document_id,
    )
    return {
        "message": "Document deleted successfully",
    }
