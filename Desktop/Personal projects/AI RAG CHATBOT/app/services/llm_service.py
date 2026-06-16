from app.logger import get_logger

logger = get_logger("services.llm_service")

from app.config import (
    LLM_PROVIDER
)

from app.services.gemini_service import (
    GeminiService
)

from app.services.openai_service import (
    OpenAIService
)


class LLMService:

    @staticmethod
    def generate(
        prompt: str
    ):
        logger.info("Using llm provider=%s",LLM_PROVIDER)

        if LLM_PROVIDER == "openai":

            return OpenAIService.generate_response(
                prompt
            )

        return GeminiService.generate_response(
            prompt
        )