from enum import Enum


class Intent(str, Enum):
    RECOMMEND = "recommend"
    COMPARE = "compare"
    REFINE = "refine"
    EXPLAIN = "explain"
    GREETING = "greeting"


class JobLevel(str, Enum):
    GRADUATE = "Graduate"
    ENTRY = "Entry-Level"
    MID = "Mid"
    SENIOR = "Senior"
    MANAGER = "Manager"
    EXECUTIVE = "Executive"


class AssessmentType(str, Enum):
    TECHNICAL = "Technical"
    PERSONALITY = "Personality"
    COGNITIVE = "Cognitive"
    BEHAVIORAL = "Behavioral"
    SITUATIONAL = "Situational Judgment"