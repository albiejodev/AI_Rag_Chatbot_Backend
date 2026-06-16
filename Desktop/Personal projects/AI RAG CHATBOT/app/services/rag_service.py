from app.db.chroma_db import ChromaDB
from app.logger import get_logger, truncate
from app.services.gemini_service import GeminiService
from app.services.chat_memory_service import ChatMemoryService
from app.services.retriever_service import (RetrieverService)
from app.services.chain_service import (ChainService)

logger = get_logger("services.rag_service")


class RAGService:

    @staticmethod
    def ask(session_id: str, question: str):
        logger.info(
            "RAG pipeline started question=%s",
            truncate(question),
        )

        history = ChatMemoryService.get_messages(session_id)

        conversation_history = ""

        for message in history:
            conversation_history += f"{message['role']}: {message['content']}\n"

        results = RetrieverService.retrieve(question)

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
                sources.append(
                    {
                        "file_name": metadata.get("file_name"),
                        "page": metadata.get("page"),
                    }
                )

        context = "\n\n".join(documents)

        prompt = f"""
        Conversation History:

        {conversation_history}

        Context:

        {context}

        Current Question:

        {question}

        Answer ONLY using the context.

        If the answer is not available,
        say so.
        """

        ChatMemoryService.add_message(
            session_id=session_id,
            role="user",
            content=question,
        )
        answer = ChainService.run(
                history=conversation_history,
                context=context,
                question=question
        )

        ChatMemoryService.add_message(
            session_id=session_id,
            role="assistant",
            content=answer,
        )

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

    
    @staticmethod
    def stream_answer(
        session_id: str,
        question: str
    ):

        results = RetrieverService.retrieve(question)

        documents = results["documents"][0]

        if not documents:

            yield "No relevant information found."
            return

        context = "\n\n".join(
            documents
        )

        prompt = f"""
        Context:

        {context}

        Question:

        {question}

        Answer using the context.
        """

        for token in GeminiService.stream_response(
            prompt
        ):
            yield token

