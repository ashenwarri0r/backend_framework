from services.university.university_service import UniversityService


class TestGetTeacher:
    def test_get_teacher(self, university_api_utils_admin, teacher):
        university_service = UniversityService(api_utils=university_api_utils_admin)

        expected_first_name = teacher.first_name
        expected_last_name = teacher.last_name
        expected_subject = teacher.subject
        response = university_service.receive_teacher(str(teacher.id))

        assert response.first_name == expected_first_name, \
            (f"Ожидаемое имя: {expected_first_name}"
             f"Фактическое имя: {response.first_name}")

        assert response.last_name == expected_last_name, \
            (f"Ожидаемая фамилия: {expected_last_name}"
             f"Фактическая фамилия: {response.last_name}")

        assert response.subject == expected_subject, \
            (f"Ожидаемый предмет: {expected_subject}"
             f"Фактический предмет: {response.subject}")