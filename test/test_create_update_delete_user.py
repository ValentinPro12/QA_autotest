from http_metod import Http_methods
from constants import CREATE_URL, ASSIGN_ROLE_URL, DELETE_URL, REMOVE_SCALE_URL, ASSIGN_SCALE_URL, REMOVE_ROLE_URL
from helpers import expected_response

def test_create_user():
    create_user(CREATE_URL)
    pass
def test_failed_create_user(create_user):
    user =  create_user(CREATE_URL)
    """Провторное создание пользователя"""
    user = create_user['user_info']
    """TODO  надо json body вывести в класс для удобстава"""
    request_body = {"Signup": {"username": user['username'], "password": user['username'],
                               "email": user['username'] + '@mail.ru',
                               "user_info_loader_type_id": 1}}

    response = Http_methods.post(CREATE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 400
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_assign_role_by_user(create_user):
    user_id = create_user['user_id']
    request_body = {"roleName": "director", "userId": user_id}
    response = Http_methods.post(ASSIGN_ROLE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_failed_assign_role_by_user(create_user):
    user_id = create_user['user_id']
    request_body = {"roleName": "director", "userId": user_id}
    response = Http_methods.post(ASSIGN_ROLE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 400
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_remove_role_by_user(create_user):
    user_id = create_user['user_id']
    request_body = {"roleName": "director", "userId": user_id}
    response = Http_methods.post(REMOVE_ROLE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_assign_scale_to_user(create_user):
    user_id = create_user['user_id']
    request_body = {"userId": user_id, "scalesId": [102]}
    response = Http_methods.post(ASSIGN_SCALE_URL, request_body)
    PDO_body = response.json()
    expected_status_code = 200
    expected_response(check_name="Код ответа сервера", actual_value=PDO_body["statusCode"],
                      expected_value=expected_status_code)


def test_remove_scale_to_user(create_user):
    user_id = create_user['user_id']
    request_body = {"userId": user_id, "scalesId": [102]}
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
