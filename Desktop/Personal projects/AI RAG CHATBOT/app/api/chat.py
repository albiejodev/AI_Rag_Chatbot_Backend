from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.logger import get_logger, truncate
from app.schemas.chat_schema import ChatRequest
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)
logger = get_logger("api.chat")


@router.post("/")
async def chat(payload: ChatRequest):
    logger.info(
        "Chat request received question=%s",
        truncate(payload.question),
    )

    try:
        result = RAGService.ask(payload.session_id, payload.question,)
    except Exception:
        logger.exception(
            "Chat request failed question=%s",
            truncate(payload.question),
        )
        raise HTTPException(
            status_code=500,
            detail="Failed to process chat request",
        )

    logger.info(
        "Chat request completed sources=%s",
        len(result.get("sources", [])),
    )
    return result


@router.post('/stream')
async def chatStream(payload:ChatRequest):
    logger.info(
        "Stream request received question=%s",
        truncate(payload.question)
    )

    return StreamingResponse(
        RAGService.stream_answer(
            payload.session_id,
            payload.question
        ),
        media_type='text/plain'
    )
