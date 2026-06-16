from fastapi import APIRouter
from app.cache.redis_client import (
    redis_client
)
from app.services.chat_memory_service import (
    ChatMemoryService
)

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)


@router.get("/{session_id}")
def get_memory(session_id: str):

    return ChatMemoryService.get_messages(
        session_id
    )


@router.delete("/{session_id}")
def delete_memory(session_id: str):

    key = f"chat:{session_id}"

    redis_client.delete(key)

    return {
        "message": "Memory deleted"
    }