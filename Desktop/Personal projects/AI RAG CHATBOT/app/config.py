import os

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "gemini"
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "gpt-4.1-mini"
)