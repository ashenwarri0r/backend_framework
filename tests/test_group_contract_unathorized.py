from faker import Faker
import requests.status_codes

from services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContractUnauthorized:
    def test_create_group_unauthorized(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            (f"Wrong status code. Actual: {response.status_code}, "
             f"expected: {requests.status_codes.codes.unauthorized}")
