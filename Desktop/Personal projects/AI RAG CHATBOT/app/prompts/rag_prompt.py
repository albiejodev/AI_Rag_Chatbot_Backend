from langchain_core.prompts import PromptTemplate

rag_prompt = PromptTemplate.from_template(
    """
Conversation History:

{history}

Context:

{context}

Question:

{question}

Answer ONLY using the provided context.

If the answer is unavailable,
say so.
"""
)