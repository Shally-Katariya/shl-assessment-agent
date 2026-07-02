from app.models.conversation import ConversationContext


def main():
    context = ConversationContext()

    print(context.model_dump())

    context.intent = "recommend"
    context.role = "Java Developer"
    context.experience = "3 years"
    context.skills.extend(["Java", "Spring Boot"])
    context.assessment_types.append("Technical")

    print()
    print(context.model_dump())


if __name__ == "__main__":
    main()