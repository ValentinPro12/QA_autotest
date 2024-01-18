import os

import requests

from constants import QMT_URL
from helpers import expect_equal


def create_user(username: str, email: str, password: str, user_info_loader_type_id: int, expected_status_code: int,
                auth_key: str):
    """Создание пользователя .

      :param auth_key: токен авторизации
      :param user_info_loader_type_id: тип авторизации в сисиетме
      :param email: почта
      :param username: имя пользователя
      :param password: пароль
      :param expected_status_code: ожидаемый http код ответа
      """
    request_body = {"Signup": {"username": username, "password": password, "email": email,
                               "user_info_loader_type_id": user_info_loader_type_id}}
    headers = {"Authorization": "Bearer " + auth_key}
    response = requests.post(url=os.getenv('QMT_URL') + 'user/user/create', json=request_body,
                             headers=headers)

    expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                 expected_value=expected_status_code)


#
# def delete_user(user_id: int, expected_status_code: int, auth_key: str):
#     """Удаление пользователя .
#
#        :param user_id: id пользователя
#        :param auth_key:
#        :param expected_status_code: ожидаемый http код ответа
#       """
#     request_body = {"id": user_id}
#     headers = {"Authorization": "Bearer " + auth_key}
#     response = requests.post(url=os.getenv('QMT_URL') + 'user/user/delete', json=request_body,
#                              headers=headers)
#     print(response.text)
#     expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
#                  expected_value=expected_status_code)
