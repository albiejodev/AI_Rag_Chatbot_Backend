import uuid

import chromadb

from app.logger import get_logger, truncate
from app.services.embedding_service import EmbeddingService

logger = get_logger("db.chroma_db")


class ChromaDB:

    client = chromadb.PersistentClient(path="chroma_data")
    collection = client.get_or_create_collection(name="documents")

    @classmethod
    def add_chunks(cls, chunks):
        logger.info("Adding chunks to ChromaDB chunk_count=%s", len(chunks))

        embeddings = EmbeddingService.get_embedding_model()

        for index, chunk in enumerate(chunks):
            vector = embeddings.embed_query(chunk.page_content)

            cls.collection.add(
                ids=[str(uuid.uuid4())],
                documents=[chunk.page_content],
                embeddings=[vector],
                metadatas=[chunk.metadata],
            )

            if (index + 1) % 10 == 0 or index == len(chunks) - 1:
                logger.debug(
                    "Chunk embedding progress embedded=%s total=%s",
                    index + 1,
                    len(chunks),
                )

        logger.info(
            "Chunks stored in ChromaDB chunk_count=%s",
            len(chunks),
        )

    @classmethod
    def search(cls, query: str, top_k: int = 3):
        logger.debug(
            "ChromaDB search started query=%s top_k=%s",
            truncate(query),
            top_k,
        )

        embeddings = EmbeddingService.get_embedding_model()
        query_vector = embeddings.embed_query(query)

        results = cls.collection.query(
            query_embeddings=[query_vector],
            n_results=top_k,
        )

        result_count = len(results.get("documents", [[]])[0])
        logger.debug(
            "ChromaDB search completed query=%s results=%s",
            truncate(query),
            result_count,
        )
        return results

    @classmethod
    def get_documents(cls):
        logger.debug("Fetching unique documents from ChromaDB")

        data = cls.collection.get()
        metadatas = data["metadatas"]

        unique_documents = {}

        for metadata in metadatas:
            document_id = metadata.get("document_id")

            if document_id:
                unique_documents[document_id] = {
                    "document_id": document_id,
                    "file_name": metadata.get("file_name"),
                }

        documents = list(unique_documents.values())
        logger.debug(
            "Fetched unique documents from ChromaDB count=%s",
            len(documents),
        )
        return documents

    @classmethod
    def delete_document(cls, document_id: str):
        logger.info(
            "Deleting document from ChromaDB document_id=%s",
            document_id,
        )

        results = cls.collection.get(
            where={
                "document_id": document_id,
            },
        )

        ids = results["ids"]

        if not ids:
            logger.warning(
                "No chunks found for document_id=%s",
                document_id,
            )
            return False

        cls.collection.delete(ids=ids)

        logger.info(
            "Deleted document from ChromaDB document_id=%s chunk_count=%s",
            document_id,
            len(ids),
        )
        return True
