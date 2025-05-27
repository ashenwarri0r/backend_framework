from enum import StrEnum

from pydantic import BaseModel, ConfigDict

class SubjectEnum(StrEnum):
    MATHS = "Mathematics"
    PHYSICS = "Physics"
    HISTORY = "History"
    BIOLOGY = "Biology"
    GEOGRAPHY = "Geography"


class BaseTeacher(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    subject: SubjectEnum