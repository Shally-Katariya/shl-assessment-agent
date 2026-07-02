class ConversationAnalyzer:
    """
    Extract structured hiring requirements from a conversation.
    """

    def analyze(self, messages):
        """
        Analyze conversation history and extract context.
        """

        context = {
            "conversation": "",
            "role": None,
            "skills": [],
            "experience": None,
            "job_level": None,
            "assessment_type": [],
            "must_have": [],
        }

        # Combine all user messages
        user_messages = []

        for message in messages:
            if message["role"] == "user":
                user_messages.append(message["content"])

        context["conversation"] = " ".join(user_messages)

        return context