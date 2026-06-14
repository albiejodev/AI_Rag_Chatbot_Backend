from app.db.chroma_db import ChromaDB
from app.logger import get_logger, truncate
from app.services.gemini_service import GeminiService

logger = get_logger("services.rag_service")


class RAGService:

    @staticmethod
    def ask(question: str):
        logger.info(
            "RAG pipeline started question=%s",
            truncate(question),
        )

        results = ChromaDB.search(
            question,
            top_k=5,
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        logger.debug(
            "RAG retrieval completed chunks=%s",
            len(documents),
        )

        seen = set()
        sources = []

        for metadata in metadatas:
            key = (
                metadata.get("file_name"),
                metadata.get("page"),
            )

            if key not in seen:
                seen.add(key)
                sources.append({
                    "file_name": metadata.get("file_name"),
                    "page": metadata.get("page"),
                })

        context = "\n\n".join(documents)

        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context,
say:
'I could not find that information in the document.'
"""

        answer = GeminiService.generate_response(prompt)

        logger.info(
            "RAG pipeline completed question=%s sources=%s answer_length=%s",
            truncate(question),
            len(sources),
            len(answer),
        )

        return {
            "answer": answer,
            "sources": sources,
        }
