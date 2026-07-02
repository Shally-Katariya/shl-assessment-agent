from typing import Optional

from pydantic import BaseModel, Field


class ConversationContext(BaseModel):
    role: Optional[str] = None
    experience: Optional[str] = None
    job_level: Optional[str] = None

    skills: list[str] = Field(default_factory=list)

    assessment_types: list[str] = Field(default_factory=list)

    must_have: list[str] = Field(default_factory=list)

    missing_fields: list[str] = Field(default_factory=list)