from faker import Faker
import requests.status_codes

from services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:
    def test_create_group(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)

        group_name = faker.name()
        response = group_helper.post_group({"name": group_name})
        response_2 = group_helper.post_group({"name": group_name})

        assert response_2.status_code == requests.status_codes.codes.conflict, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"expected: {requests.status_codes.codes.conflict}")