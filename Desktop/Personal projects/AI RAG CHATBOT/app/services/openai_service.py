from openai import OpenAI

from app.config import (
    OPENAI_API_KEY,
    LLM_MODEL
)


class OpenAIService:

    client = OpenAI(
        api_key=OPENAI_API_KEY
    )

    @classmethod
    def generate_response(
        cls,
        prompt: str
    ):

        response = cls.client.responses.create(
            model=LLM_MODEL,
            input=prompt
        )

        return response.output_text