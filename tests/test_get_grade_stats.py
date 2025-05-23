import random

from faker import Faker

from logger.logger import Logger
from services.university.models.grade_request import GradeRequest
from services.university.models.grade_statistic_request import GradesStatsRequest
from services.university.university_service import UniversityService

faker = Faker()

GRADE_1 = random.randint(0,5)
GRADE_2 = random.randint(0,5)
GRADES = [GRADE_1, GRADE_2]
CORRECT_COUNT = len(GRADES)
CORRECT_MIN = min(GRADES)
CORRECT_MAX = max(GRADES)
CORRECT_AVG = sum(GRADES) / CORRECT_COUNT

class TestGetGradeStats:
    def test_get_grade_stats(self, university_api_utils_admin, student, teacher):
        university_service = UniversityService(api_utils=university_api_utils_admin)

        grade = GradeRequest(student_id=student.id, teacher_id=teacher.id, grade=GRADE_1)
        university_service.add_grade(grade_request=grade)
        grade_2 = GradeRequest(student_id=student.id, teacher_id=teacher.id, grade=GRADE_2)
        university_service.add_grade(grade_request=grade_2)

        stats_request = GradesStatsRequest(student_id=student.id)
        stats_response = university_service.receive_grades_stats(stats_request)

        assert stats_response.count == CORRECT_COUNT, \
            (f"Фактическое количество оценок: {stats_response.count}, "
             f"Ожидаемое количество оценок: {CORRECT_COUNT}")

        assert stats_response.min == CORRECT_MIN, \
            (f"Фактическое количество оценок: {stats_response.min}, "
             f"Ожидаемое количество оценок: {CORRECT_MIN}")

        assert stats_response.max == CORRECT_MAX, \
            (f"Фактическое количество оценок: {stats_response.max}, "
             f"Ожидаемое количество оценок: {CORRECT_MAX}")

        assert stats_response.avg == CORRECT_AVG, \
            (f"Фактическое количество оценок: {stats_response.avg}, "
             f"Ожидаемое количество оценок: {CORRECT_AVG}")
