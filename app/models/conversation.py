from typing import Optional

from pydantic import BaseModel, Field

from app.models.enums import (
    AssessmentType,
    Intent,
    JobLevel,
)


class ConversationContext(BaseModel):
    """
    Structured understanding of the hiring conversation.
    """

    # User's intent
    intent: Intent = Intent.RECOMMEND

    # Hiring details
    role: Optional[str] = None
    experience: Optional[str] = None
    job_level: Optional[JobLevel] = None

    # Extracted information
    skills: list[str] = Field(default_factory=list)
    assessment_types: list[AssessmentType] = Field(default_factory=list)
    must_have: list[str] = Field(default_factory=list)

    # Missing information
    missing_fields: list[str] = Field(default_factory=list)

    # Combined conversation
    conversation: str = ""