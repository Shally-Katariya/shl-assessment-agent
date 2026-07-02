from app.llm.gemini_client import GeminiClient
from app.models.enums import Intent
from app.retrieval.retriever import Retriever


class AssessmentAgent:
    """
    Main orchestration layer for the SHL Assessment Agent.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.gemini = GeminiClient()

    def can_recommend(self, context):
        """
        Decide whether enough information is available
        to perform semantic search.
        """

        return (
            context.role is not None
            or len(context.skills) > 0
        )

    def chat(self, messages):
        """
        Process a conversation and return recommendations.
        """

        if not messages:
            return {
                "reply": "How can I help you find an SHL assessment today?",
                "recommendations": [],
                "end_of_conversation": False,
            }

        # -------------------------------------------------
        # Step 1 : Extract structured context using Gemini
        # -------------------------------------------------
        context = self.gemini.extract_context(messages)

        # -------------------------------------------------
        # Step 2 : Ask clarification only if absolutely needed
        # -------------------------------------------------
        if not self.can_recommend(context):

            field = (
                context.missing_fields[0]
                if context.missing_fields
                else "role"
            )

            clarification_questions = {
                "role": "What role are you hiring for?",
                "experience": "What experience level are you hiring for?",
                "assessment_type": (
                    "Are you looking for a technical, personality, "
                    "cognitive, or behavioral assessment?"
                ),
                "skills": "Which key skills should be assessed?",
            }

            return {
                "reply": clarification_questions.get(
                    field,
                    "Could you provide a little more information?"
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        # -------------------------------------------------
        # Step 3 : Handle recommendation requests
        # -------------------------------------------------
        if context.intent == Intent.RECOMMEND:

            query_parts = []

            if context.role:
                query_parts.append(context.role)

            query_parts.extend(context.skills)

            if context.experience:
                query_parts.append(context.experience)

            if context.job_level:
                query_parts.append(context.job_level.value)

            query_parts.extend(
                assessment.value
                for assessment in context.assessment_types
            )

            query_parts.extend(context.must_have)

            search_query = " ".join(query_parts)

            results = self.retriever.search(
                search_query,
                top_k=5,
            )

            recommendations = []

            for result in results:
                recommendations.append(
                    {
                        "name": result["name"],
                        "url": result["url"],
                        "score": round(result["score"], 3),
                        "categories": result["categories"],
                        "adaptive": result["adaptive"],
                        "duration": result["duration"]
                        if result["duration"]
                        else "Not specified",
                        "job_levels": result["job_levels"],
                    }
                )

            return {
                "reply": "I found these SHL assessments based on your hiring requirements.",
                "recommendations": recommendations,
                "end_of_conversation": False,
            }

        # -------------------------------------------------
        # Future intents
        # -------------------------------------------------
        if context.intent == Intent.COMPARE:
            return {
                "reply": "Assessment comparison will be available soon.",
                "recommendations": [],
                "end_of_conversation": False,
            }

        if context.intent == Intent.REFINE:
            return {
                "reply": "Recommendation refinement will be available soon.",
                "recommendations": [],
                "end_of_conversation": False,
            }

        if context.intent == Intent.EXPLAIN:
            return {
                "reply": "Recommendation explanation will be available soon.",
                "recommendations": [],
                "end_of_conversation": False,
            }

        if context.intent == Intent.GREETING:
            return {
                "reply": (
                    "Hello! I can help you find the most suitable SHL "
                    "assessment for your hiring needs."
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }

        return {
            "reply": (
                "I'm not sure how to help with that yet. "
                "Try describing the role you're hiring for."
            ),
            "recommendations": [],
            "end_of_conversation": False,
        }