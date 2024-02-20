import pytest
import requests

from random import randrange
from constants import USERNAME_AAA, PASSWORD_AAA, QMT_URL, CREATE_URL
from http_metod import Http_methods
from request_body import BodyBuild

from faker import Faker


@pytest.fixture(scope='module')
def login_token():
    request_body = {"username": USERNAME_AAA, "password": PASSWORD_AAA, "rememberMe": 1, "type": 'AAA'}
    response = requests.post(url=QMT_URL + "authorization/login", json=request_body)
    auth_key = response.json()
    return auth_key['auth_key']


@pytest.fixture()
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
