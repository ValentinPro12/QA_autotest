import pytest
import requests

from constants import QMT_URL, PASSWORD, USERNAME


@pytest.fixture(scope='module')
def login_token():
    request_body = {"username": USERNAME, "password": PASSWORD, "rememberMe": 1, "type": 'AAA'}
    response = requests.post(url=QMT_URL + "authorization/login", json=request_body)
    auth_key = response.json()
    return auth_key['auth_key']
