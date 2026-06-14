from langchain_community.document_loaders import PyPDFLoader

from app.logger import get_logger

logger = get_logger("services.pdf_service")


class PDFService:

    @staticmethod
    def extract_pdf(file_path: str):
        logger.info("PDF extraction started path=%s", file_path)

        loader = PyPDFLoader(file_path)
        documents = loader.load()

        logger.info(
            "PDF extraction completed path=%s page_count=%s",
            file_path,
            len(documents),
        )
        return documents
