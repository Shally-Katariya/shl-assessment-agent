from app.llm.gemini_client import GeminiClient


def main():
    client = GeminiClient()

    messages = [
        {
            "role": "user",
            "content": "Hiring a Java Backend Developer with 3 years of experience. Looking for a technical assessment."
        }
    ]

    context = client.extract_context(messages)

    print(type(context))
    print()

    print(context)

    print()

    print(context.model_dump())


if __name__ == "__main__":
    main()