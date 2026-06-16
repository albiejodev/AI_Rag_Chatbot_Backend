import json

from app.cache.redis_client import redis_client


class ChatMemoryService:

    @classmethod
    def add_message(
        cls,
        session_id: str,
        role: str,
        content: str
    ):

        key = f"chat:{session_id}"

        existing_messages = cls.get_messages(
            session_id
        )

        existing_messages.append(
            {
                "role": role,
                "content": content
            }
        )

        redis_client.setex(
            key,
            86400,
            json.dumps(existing_messages)
        )

    @classmethod
    def get_messages(
        cls,
        session_id: str
    ):

        key = f"chat:{session_id}"

        data = redis_client.get(key)

        if not data:
            return []

        return json.loads(data)