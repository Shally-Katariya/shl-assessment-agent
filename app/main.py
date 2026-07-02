from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.assessment_agent import AssessmentAgent


app = FastAPI(
    title="SHL Assessment Recommender",
    description="Conversational AI agent for recommending SHL assessments",
    version="1.0.0",
)

agent = AssessmentAgent()


class ChatRequest(BaseModel):
    messages: list[dict]


@app.get("/")
def root():
    return {
        "message": "SHL Assessment Recommender API",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post("/chat")
def chat(request: ChatRequest):
    """
    Main conversational endpoint.
    """

    return agent.chat(request.messages)