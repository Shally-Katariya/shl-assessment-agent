import os

from dotenv import load_dotenv
from google import genai

from app.llm.prompts import SYSTEM_PROMPT


load_dotenv()


class GeminiClient:
    """
    Wrapper around the Gemini API.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash"