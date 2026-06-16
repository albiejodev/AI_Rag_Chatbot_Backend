from app.chains.rag_chain import (
    run_chain
)


class ChainService:

    @staticmethod
    def run(
        history,
        context,
        question,
    ):

        return run_chain(
            history,
            context,
            question,
        )