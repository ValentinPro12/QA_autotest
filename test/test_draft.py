from http_metod import Http_methods
from constants import CREATE_URL, ASSIGN_ROLE_URL, DELETE_URL, REMOVE_SCALE_URL, ASSIGN_SCALE_URL, REMOVE_ROLE_URL
from helpers import expected_response
from request_body import BodyBuild


class TestUser:
    @staticmethod
    def create_user():
        fake = Faker()

        username = fake.first_name() + '_Test'
        password = '1234567890'
        request_body = BodyBuild.user_body_create(username, password, fake.ascii_free_email(), 1)
        response = Http_methods.post(CREATE_URL, request_body)
        user_id = response.json().get('data')
        expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                          expected_value=expected_status_code)
        yield user_id['id']
        # return PDO_body["user_id"]

    @staticmethod
    def assign_role_by_user(user_id, role):
        request_body = BodyBuild.user_body(role, user_id)
        response = Http_methods.post(ASSIGN_ROLE_URL, request_body)
        PDO_body = response.json()
        return PDO_body["statusCode"]

    @staticmethod
    def remove_role_by_user(user_id, role):
        request_body = BodyBuild.user_body(role, user_id)
        response = Http_methods.post(REMOVE_ROLE_URL, request_body)
        PDO_body = response.json()
        return PDO_body["statusCode"]

    @staticmethod
    def assign_scale_to_user(user_id, scale):
        request_body = BodyBuild.scale(scale, user_id)
        response = Http_methods.post(ASSIGN_SCALE_URL, request_body)
        PDO_body = response.json()
        return PDO_body["statusCode"]

    @staticmethod
    def remove_scale_to_user(user_id, scale):
        request_body = BodyBuild.scale(scale, user_id)
        response = Http_methods.post(REMOVE_SCALE_URL, request_body)
        PDO_body = response.json()
        return PDO_body["statusCode"]

    @staticmethod
    def delete_user(user_id):
        request_body = BodyBuild.user_body('director', user_id=user_id)
        response = Http_methods.post(DELETE_USER_URL, request_body)
        PDO_body = response.json()
        return PDO_body["statusCode"]


class TestUserAssignRole:
    def test_assign_role_by_user(self):
        user_id = TestUser().create_user()
        status_code = TestUser().assign_role_by_user(user_id, 'director')
        expected_status_code = 200
        assert status_code == expected_status_code

    def test_failed_assign_role_by_user(self):
        user_id = TestUser().create_user()
        TestUser().assign_role_by_user(user_id, 'director')
        status_code = TestUser().assign_role_by_user(user_id, 'director')
        expected_status_code = 400
        assert status_code == expected_status_code


class TestUserRemoveRole:
    def test_remove_role_by_user(self):
        user_id = TestUser().create_user()
        TestUser().assign_role_by_user(user_id, 'director')
        status_code = TestUser().remove_role_by_user(user_id, 'director')
        expected_status_code = 200
        assert status_code == expected_status_code


class TestUserAssignScale:
    def test_assign_scale_to_user(self):
        user_id = TestUser().create_user()
        status_code = TestUser().assign_scale_to_user(user_id, 102)
        expected_status_code = 200
        assert status_code == expected_status_code


class TestUserRemoveScale:
    def test_remove_scale_to_user(self):
        user_id = TestUser().create_user()
        TestUser().assign_scale_to_user(user_id, 102)
        status_code = TestUser().remove_scale_to_user(user_id, 102)
        expected_status_code = 200
        assert status_code == expected_status_code
