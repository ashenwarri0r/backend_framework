import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    STATS_ENDPOINT = f"{ENDPOINT_PREFIX}/stats/"

    def post_grade(self, json: dict) -> requests.Response:
        response = self.api_utils.post(
            self.ROOT_ENDPOINT,
            data=json)
        return response

    def get_grades_statistics(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
            group_id: int | None = None,
    ) -> requests.Response:
        params = {
            "student_id": student_id,
            "teacher_id": teacher_id,
            "group_id": group_id,
        }
        params = {k: v for k, v in params.items() if v is not None}

        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response
