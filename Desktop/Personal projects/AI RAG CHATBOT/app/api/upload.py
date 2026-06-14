import os
import uuid

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.db.chroma_db import ChromaDB
from app.logger import get_logger
from app.services.chunk_service import ChunkService
from app.services.pdf_service import PDFService

router = APIRouter(
    prefix="/upload",
    tags=["upload"],
)
logger = get_logger("api.upload")


@router.get("/")
async def test_upload_route():
    logger.debug("Upload route health check")
    return {
        "message": "Upload route is working",
    }


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    logger.info(
        "PDF upload started filename=%s content_type=%s",
        file.filename,
        file.content_type,
    )

    try:
        os.makedirs("uploads", exist_ok=True)
        file_path = os.path.join("uploads", file.filename)

        file_bytes = await file.read()
        with open(file_path, "wb") as pdf_file:
            pdf_file.write(file_bytes)

        logger.debug(
            "PDF saved path=%s size_bytes=%s",
            file_path,
            len(file_bytes),
        )

        documents = PDFService.extract_pdf(file_path)
        document_id = str(uuid.uuid4())

        for document in documents:
            document.metadata["document_id"] = document_id
            document.metadata["file_name"] = file.filename

        chunks = ChunkService.create_chunks(documents)

        for chunk in chunks:
            chunk.metadata["document_id"] = document_id
            chunk.metadata["file_name"] = file.filename

        ChromaDB.add_chunks(chunks)
    except Exception:
        logger.exception(
            "PDF upload failed filename=%s",
            file.filename,
        )
        raise HTTPException(
            status_code=500,
            detail="Failed to process uploaded PDF",
        )

    logger.info(
        "PDF upload completed document_id=%s pages=%s chunks=%s filename=%s",
        document_id,
        len(documents),
        len(chunks),
        file.filename,
    )

    return {
        "pages": len(documents),
        "chunks": len(chunks),
        "status": "stored in chromadb",
    }
