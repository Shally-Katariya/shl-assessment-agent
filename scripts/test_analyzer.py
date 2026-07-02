from app.conversation.analyzer import ConversationAnalyzer


def main():
    analyzer = ConversationAnalyzer()

    messages = [
        {
            "role": "user",
            "content": "Hiring Java Developer"
        },
        {
            "role": "assistant",
            "content": "Experience?"
        },
        {
            "role": "user",
            "content": "3 years"
        }
    ]

    context = analyzer.analyze(messages)

    print(context)


if __name__ == "__main__":
    main()