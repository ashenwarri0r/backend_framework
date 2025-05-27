import pytest


@pytest.mark.usefixtures("university_api_utils_admin", "teacher", "teacher_get_response")
class TestTeacherFields:
    def test_teacher_first_name(self, university_api_utils_admin, teacher, teacher_get_response):
        expected_first_name = teacher.first_name

        assert teacher_get_response.first_name == expected_first_name, \
            (f"Ожидаемое имя: {expected_first_name}"
             f"Фактическое имя: {teacher_get_response.first_name}")

    def test_teacher_last_name(self, university_api_utils_admin, teacher, teacher_get_response):
        expected_last_name = teacher.last_name

        assert teacher_get_response.last_name == expected_last_name, \
            (f"Ожидаемая фамилия: {expected_last_name}"
             f"Фактическая фамилия: {teacher_get_response.last_name}")

    def test_teacher_subject(self, university_api_utils_admin, teacher, teacher_get_response):
        expected_subject = teacher.subject

        assert teacher_get_response.subject == expected_subject, \
            (f"Ожидаемый предмет: {expected_subject}"
             f"Фактический предмет: {teacher_get_response.subject}")
