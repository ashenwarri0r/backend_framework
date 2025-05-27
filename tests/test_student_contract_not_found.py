from random import randint

from services.university.helpers.student_helper import StudentHelper

STUDENT_ID = str(randint(10, 99))
EXPECTED_ERROR_TEXT = "not found"

class TestStudentContractNotFound:
    def test_student_contract_not_found(self, university_api_utils_admin):
        student_helper = StudentHelper(university_api_utils_admin)

        response = student_helper.delete_student(STUDENT_ID)

        assert response.status_code == 404, \
            (f"Ожидался статус код 404"
             f"Фактический статус код: {response.status_code}")

        assert EXPECTED_ERROR_TEXT in response.json().get("detail", "").lower(), \
            (f"Ожидалось, что в тексте ошибки будет: {EXPECTED_ERROR_TEXT}"
             f"Фактический текст ошибки: {response.json().get('detail')}")
