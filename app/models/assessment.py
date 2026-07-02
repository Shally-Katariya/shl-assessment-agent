from pydantic import BaseModel
from typing import List


class Assessment(BaseModel):
    entity_id: str
    name: str
    link: str
    description: str
    job_levels: List[str]
    languages: List[str]
    duration: str
    adaptive: str
    keys: List[str]