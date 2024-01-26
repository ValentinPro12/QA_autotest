import os

import requests

from constants import QMT_URL
from helpers import expect_equal


def login(username: str, password: str, remember_me: int, auth_type: str, expected_status_code: int):
    """Авторизация пользователя.

    :param username: имя пользователя
    :param password: пароль
    :param remember_me: параметор запоминания пароля
    :param auth_type: тип авторизации QMT/AAA
    :param expected_status_code: ожидаемый http код ответа
    """
    request_body = {"username": username, "password": password, "rememberMe": remember_me, "type": auth_type}
    response = requests.post(url=QMT_URL + "authorization/login", json=request_body)
    expect_equal(check_name="Код ответа сервера", actual_value=response.status_code,
                 expected_value=expected_status_code)
