from app.retrieval.retriever import Retriever


class AssessmentAgent:
    """
    Main conversational agent for recommending SHL assessments.
    """

    def __init__(self):
        self.retriever = Retriever()

    def extract_context(self, messages):
        """
        Combine all user messages into a single context string.
        """

        user_text = " ".join(
            message["content"]
            for message in messages
            if message["role"] == "user"
        )

        return user_text.lower()

    def needs_clarification(self, context: str) -> bool:
        """
        Decide whether enough information has been provided
        to recommend assessments.
        """

        roles = [
            "developer",
            "engineer",
            "manager",
            "analyst",
            "sales",
            "consultant",
            "intern",
            "graduate",
        ]

        skills = [
            "java",
            "python",
            "c++",
            "javascript",
            "react",
            "sql",
            "aws",
            "leadership",
            "communication",
        ]

        has_role = any(role in context for role in roles)
        has_skill = any(skill in context for skill in skills)

        return not (has_role or has_skill)

    def chat(self, messages):
        """
        Process the conversation and return the next response.
        """

        if not messages:
            return {
                "reply": "How can I help you find an SHL assessment today?",
                "recommendations": [],
                "end_of_conversation": False,
            }

        # Build conversation context
        context = self.extract_context(messages)

        # Ask for clarification if required
        if self.needs_clarification(context):
            return {
                "reply": (
                    "Could you tell me more about the role you're hiring for? "
                    "For example, the job title, required skills, or experience level."
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        # Retrieve assessments
        results = self.retriever.search(
            context,
            top_k=5,
        )

        recommendations = []

        for result in results:
            recommendations.append(
                {
                    "name": result["name"],
                    "url": result["url"],
                }
            )

        return {
            "reply": "Here are some SHL assessments that match your requirements.",
            "recommendations": recommendations,
            "end_of_conversation": False,
        }