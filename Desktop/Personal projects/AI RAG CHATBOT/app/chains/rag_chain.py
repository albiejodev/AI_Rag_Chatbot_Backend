from langchain_openai import ChatOpenAI
from app.config import (
    OPENAI_API_KEY,
    LLM_MODEL,
)
from app.prompts.rag_prompt import (
    rag_prompt
)



llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=LLM_MODEL,
)


chain = ( rag_prompt | llm )



def run_chain(
    history,
    context,
    question,
):

    response = chain.invoke(
        {
            "history": history,
            "context": context,
            "question": question,
        }
    )

    return response.content