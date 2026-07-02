from app.llm.gemini_client import GeminiClient


def main():
    client = GeminiClient()

    print("Gemini client initialized successfully.")
    print(f"Model: {client.model}")


if __name__ == "__main__":
    main()