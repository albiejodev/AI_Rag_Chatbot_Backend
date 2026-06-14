from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.logger import get_logger

logger = get_logger("services.chunk_service")


class ChunkService:

    @staticmethod
    def create_chunks(documents):
        logger.info(
            "Chunking started document_count=%s",
            len(documents),
        )

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )

        chunks = text_splitter.split_documents(documents)

        logger.info(
            "Chunking completed document_count=%s chunk_count=%s",
            len(documents),
            len(chunks),
        )
        return chunks
