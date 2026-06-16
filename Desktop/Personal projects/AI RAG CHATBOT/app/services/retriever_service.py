from app.db.chroma_db import ChromaDB


class RetrieverService:

    @staticmethod
    def retrieve(
        question: str,
        top_k: int = 5
    ):

        results = ChromaDB.search(
            question,
            top_k
        )

        return results