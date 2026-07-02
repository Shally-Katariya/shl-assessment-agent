from app.agents.assessment_agent import AssessmentAgent


def main():
    agent = AssessmentAgent()

    # Test 1
    print("=" * 60)
    print("TEST 1: Vague Query")
    print("=" * 60)

    response = agent.chat([
        {
            "role": "user",
            "content": "I need an assessment"
        }
    ])

    print(response)

    # Test 2
    print("\n" + "=" * 60)
    print("TEST 2: Java Developer")
    print("=" * 60)

    response = agent.chat([
        {
            "role": "user",
            "content": "Need Java developer assessment"
        }
    ])

    print(response)

    # Test 3
    print("\n" + "=" * 60)
    print("TEST 3: Multi-turn Conversation")
    print("=" * 60)

    response = agent.chat([
        {
            "role": "user",
            "content": "Hiring Java Developer"
        },
        {
            "role": "assistant",
            "content": "What experience level?"
        },
        {
            "role": "user",
            "content": "3 years"
        }
    ])

    print(response)


if __name__ == "__main__":
    main()