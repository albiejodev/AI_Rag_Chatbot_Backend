from google import genai

from app.config import GOOGLE_API_KEY
from app.logger import get_logger, truncate

logger = get_logger("services.gemini_service")


class GeminiService:

    @staticmethod
    def generate_response(prompt: str):
        logger.debug(
            "Gemini request started prompt_length=%s prompt_preview=%s",
            len(prompt),
            truncate(prompt),
        )

        client = genai.Client(
            api_key=GOOGLE_API_KEY,
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        logger.debug(
            "Gemini request completed response_length=%s",
            len(response.text),
        )
        return response.text

    
    @staticmethod
    def stream_response(prompt: str):
        
        logger.debug(
            "Gemini streaming started prompt_length=%s prompt_preview=%s",
            len(prompt),
            truncate(prompt),
        )

        client = genai.Client(
            api_key=GOOGLE_API_KEY,
        )

        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        for chunk in response:

            if chunk.text:
                yield chunk.text

        logger.debug(
            "Gemini streaming completed response_length=%s",
            len(response.text),
        )
        return response.text
