import pytest
import requests

from random import randrange
from constants import USERNAME_AAA, PASSWORD_AAA, QMT_URL, CREATE_URL
from http_metod import Http_methods


@pytest.fixture(scope='module')
def login_token():
    request_body = {"username": USERNAME_AAA, "password": PASSWORD_AAA, "rememberMe": 1, "type": 'AAA'}
    response = requests.post(url=QMT_URL + "authorization/login", json=request_body)
    auth_key = response.json()
    return auth_key['auth_key']


@pytest.fixture(scope='module')
# pip install Faker надо поставить
def create_user():
    username = 'Test_user' + str(randrange(0, 101, 2))
    request_body = {"Signup": {"username": username, "password": username,
                               "email": username + '@mail.ru',
                               "user_info_loader_type_id": 1}}
    response = Http_methods.post(CREATE_URL, request_body)
    user_id = response.json().get('data')
    data_user = {'user_id': user_id['id'], 'user_info': user_id}
    yield data_user
    delete_user(data_user)
