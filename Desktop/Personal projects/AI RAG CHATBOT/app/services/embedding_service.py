from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import GOOGLE_API_KEY
from app.logger import get_logger

logger = get_logger("services.embedding_service")


class EmbeddingService:

    _embeddings = None

    @classmethod
    def get_embedding_model(cls):
        if cls._embeddings is None:
            logger.info("Initializing embedding model model=gemini-embedding-001")
            cls._embeddings = GoogleGenerativeAIEmbeddings(
                model="gemini-embedding-001",
                google_api_key=GOOGLE_API_KEY,
            )

        return cls._embeddings
