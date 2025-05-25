import pytest
from faker import Faker

from conftest import grades_data
from services.university.models.grade_statistic_request import GradesStatsRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestGetGradeStats:

    @pytest.fixture(scope="class", autouse=True)
    def _setup(self, university_api_utils_admin, grades_data, request):
        university_service = UniversityService(api_utils=university_api_utils_admin)
        stats_request = GradesStatsRequest(student_id=grades_data.student_id)

        cls = request.cls
        cls.stats_response = university_service.receive_grades_stats(stats_request)
        cls.expected_count = grades_data.expected_count
        cls.expected_min = grades_data.expected_min
        cls.expected_max = grades_data.expected_max
        cls.expected_avg = grades_data.expected_avg

    def test_grades_count(self):
        assert self.stats_response.count == self.expected_count, \
            (f"Фактическое количество оценок: {self.stats_response.count}, "
             f"Ожидаемое количество оценок: {self.expected_count}")

    def test_grades_min(self):
        assert self.stats_response.min == self.expected_min, \
            (f"Фактическое количество оценок: {self.stats_response.min}, "
             f"Ожидаемое количество оценок: {self.expected_min}")

    def test_grades_max(self):
        assert self.stats_response.max == self.expected_max, \
            (f"Фактическое количество оценок: {self.stats_response.max}, "
             f"Ожидаемое количество оценок: {self.expected_max}")

    def test_grades_avg(self):
        assert self.stats_response.avg == self.expected_avg, \
            (f"Фактическое количество оценок: {self.stats_response.avg}, "
             f"Ожидаемое количество оценок: {self.expected_avg}")
