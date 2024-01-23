import requests

from constants import QMT_URL, HEADER_TOKEN, CREATE_URL
from helpers import expect_equal
from http_metod import Http_methods


def create_user():
    request_body = {"Signup": {"username": 'Test_user02', "password": 'test_test_3443test_test_13',
                               "email": 'Test_user02@mail.ru',
                               "user_info_loader_type_id": 1}}
    response = Http_methods.post(CREATE_URL, request_body)
    user_i = response.json()

    failed_create_user(user_id)
    # assign_role_by_user(var['data']['id'])
    # assign_scale_to_user(var['data']['id'])
    # remove_role_by_user(var['data']['id'])
    # remove_scale_to_user(var['data']['id'])


def failed_create_user(user_data: dict):
    """Провторное создание пользователя
    :param user_data: объект созданного пользователя

    """
    request_body = {"Signup": {"username": user_data['username'], "password": 'passwordTest',
                               "email": user_data['username'] + '@mail.ru',
                               "user_info_loader_type_id": 1}}

    response = Http_methods.post(CREATE_URL, request_body)
    check_post = response.json()
    place_id = check_post.get('id')
    print(place_id)
    print(user_data.get('id'))
    print(check_post)
    response_body = response.json()
    expected_value = 400
    response_server = f'Ожидание: {expected_value} Факт: {response.status_code}, Сообщение о ошибке {response_body["message"]}\n'

    assert response_body["statusCode"] == expected_value, response_server


def assign_role_by_user():
    request_body = {"roleName": "director", "userId": 68261}
    response = Http_methods.post(CREATE_URL, request_body)

    pass


def remove_role_by_user():
    request_body = {"roleName": "guest", "userId": 6944}
    response = Http_methods.post(CREATE_URL, request_body)

    pass


def assign_scale_to_user():
    request_body = {"userId": 68261, "scalesId": [102]}
    response = Http_methods.post(CREATE_URL, request_body)

    pass


def remove_scale_to_user():
    request_body = {"userId": 68261, "scalesId": [102]}
    response = Http_methods.post(CREATE_URL, request_body)

    pass


def delete_user():
    request_body = {"id": 68261}
    response = Http_methods.post(CREATE_URL, request_body)

    pass


create_user()
