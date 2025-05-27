from pydantic import BaseModel, model_validator
from typing import Optional

class GradesStatsRequest(BaseModel):
    student_id: Optional[int] = None
    teacher_id: Optional[int] = None
    group_id: Optional[int] = None

    @model_validator(mode='after')
    def check_at_least_one(self):
        if all(v is None for v in self.model_dump().values()):
            raise ValueError("Должен быть указан хотя бы один параметр")
        return self