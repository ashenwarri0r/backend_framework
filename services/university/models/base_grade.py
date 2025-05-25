from pydantic import BaseModel, ConfigDict, Field

from .constants_for_models import Constants


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int = Field(ge=Constants.MIN_GRADE, le=Constants.MAX_GRADE)
