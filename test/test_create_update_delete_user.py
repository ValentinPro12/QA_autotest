from http_metod import Http_methods
from constants import CREATE_URL, ASSIGN_ROLE_URL, DELETE_URL, REMOVE_SCALE_URL, ASSIGN_SCALE_URL, REMOVE_ROLE_URL
from helpers import expected_response
from request_body import BodyBuild


def test_create_user(create_user: int):
    ''' тут надо что то сделать что бы получить ответ что все норм '''
    print(create_user)


def test_assign_role_by_user(create_user):
    user_id = create_user
    request_body = BodyBuild.user_body('director', user_id)
    response = Http_methods.post(ASSIGN_ROLE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


## тут вопросы, если создаю нового пользователя,
# у него нет роли, кроме guest, либо тестить на ней или надо что то сделать но я пока не понимаю
def test_failed_assign_role_by_user(create_user):
    user_id = create_user['user_id']
    request_body = BodyBuild.user_body('director', user_id)
    response = Http_methods.post(ASSIGN_ROLE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 400
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_remove_role_by_user(create_user):
    user_id = create_user['user_id']
    request_body = BodyBuild.user_body('guest', user_id)
    response = Http_methods.post(REMOVE_ROLE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_assign_scale_to_user(create_user):
    user_id = create_user['user_id']
    request_body = BodyBuild.scale(102, user_id)
    response = Http_methods.post(ASSIGN_SCALE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_remove_scale_to_user(create_user):
    user_id = create_user['user_id']
    request_body = BodyBuild.scale(102, user_id)
    response = Http_methods.post(REMOVE_SCALE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_delete_user(create_user):
    user_id = create_user['user_id']
    request_body = {"id": user_id}
    response = Http_methods.post(DELETE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)
