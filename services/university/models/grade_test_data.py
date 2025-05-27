from dataclasses import dataclass


@dataclass
class GradeTestData:
    student_id: int
    grades: list[int]

    @property
    def expected_count(self) -> int:
        return len(self.grades)

    @property
    def expected_min(self) -> int:
        return min(self.grades)

    @property
    def expected_max(self) -> int:
        return max(self.grades)

    @property
    def expected_avg(self) -> float:
        return sum(self.grades) / len(self.grades)
