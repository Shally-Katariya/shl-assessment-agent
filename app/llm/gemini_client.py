import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.llm.prompts import SYSTEM_PROMPT
from app.models.conversation import ConversationContext


load_dotenv()


class GeminiClient:
    """
    Wrapper around the Gemini API.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found.")

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash"
        
    def extract_context(self, messages):
        """
        Analyze the conversation and return a structured
        ConversationContext.
        """

        conversation = []

        for message in messages:
            conversation.append(
                f"{message['role'].upper()}: {message['content']}"
            )

        conversation_text = "\n".join(conversation)

        response = self.client.models.generate_content(
            model=self.model,
            contents=conversation_text,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                response_mime_type="application/json",
                response_schema=ConversationContext,
                temperature=0,
            ),
        )

        return response.parsed    