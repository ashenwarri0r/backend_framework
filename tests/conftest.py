import random
import time

import pytest
import requests

from logger.logger import Logger
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import SubjectEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.grade_test_data import GradeTestData
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.constants_for_models import Constants
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from faker import Faker

faker = Faker()


@pytest.fixture(scope='session', autouse=True)
def auth_service_readiness():
    timeout = 180
    start = time.time()
    while time.time() - start < timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wan't started during {timeout} seconds")


@pytest.fixture(scope='session', autouse=True)
def university_service_readiness():
    timeout = 180
    start = time.time()
    while time.time() - start < timeout:
        try:
            response = requests.get(UniversityService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except ConnectionError:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wan't started during {timeout} seconds")


@pytest.fixture(scope='class', autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope='class', autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope='class', autouse=False)
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_service.register_user(
        register_request=RegisterRequest(
            username=username, password=password,
            password_repeat=password, email=faker.email()))

    login_response = auth_service.login_user(login_request=LoginRequest(
        username=username, password=password))
    return login_response.access_token


@pytest.fixture(scope='function', autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL, headers={'Authorization': f'Bearer {access_token}'})
    return api_utils


@pytest.fixture(scope='class', autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, headers={'Authorization': f'Bearer {access_token}'})
    return api_utils


@pytest.fixture(scope='class', autouse=False)
def student(university_api_utils_admin):
    Logger.info("Setup step 1. Create group")
    university_service = UniversityService(api_utils=university_api_utils_admin)
    group = GroupRequest(name=faker.name())
    group_response = university_service.create_group(group_request=group)

    Logger.info("Setup step 2. Create student")
    student_request = StudentRequest(first_name=faker.first_name(),
                                     last_name=faker.last_name(),
                                     email=faker.email(),
                                     degree=random.choice([option for option in DegreeEnum]),
                                     phone=faker.numerify("+7##########"),
                                     group_id=group_response.id)
    student = university_service.create_student(student_request=student_request)
    return student


@pytest.fixture(scope='class', autouse=False)
def teacher(university_api_utils_admin):
    Logger.info("Setup - Create teacher")
    university_service = UniversityService(api_utils=university_api_utils_admin)

    teacher_request = TeacherRequest(first_name=faker.first_name(), last_name=faker.last_name(),
                                     subject=random.choice([option for option in SubjectEnum]))
    teacher = university_service.create_teacher(teacher_request=teacher_request)
    return teacher


@pytest.fixture(scope='class', autouse=False)
def teacher_get_response(university_api_utils_admin, teacher):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher_response = university_service.receive_teacher(teacher.id)
    return teacher_response


@pytest.fixture(scope='class', autouse=False)
def grades_data(university_api_utils_admin, student, teacher):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    number_of_grades = random.randint(2, 20)
    grades = []
    for _ in range(number_of_grades):
        random_grade = random.randint(Constants.MIN_GRADE, Constants.MAX_GRADE)
        Logger.info(f"Add grade {random_grade} to student {student.id}")
        grade = GradeRequest(student_id=student.id, teacher_id=teacher.id, grade=random_grade)
        university_service.add_grade(grade_request=grade)
        grades.append(random_grade)
    grades_data = GradeTestData(student.id, grades)
    return grades_data
