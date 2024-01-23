import requests
from requests import Response

from constants import HEADER_TOKEN


class Http_methods:
    cookie = ''

    @staticmethod
    def get(url) -> Response:
        result = requests.get(url, headers=HEADER_TOKEN, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def post(url, body) -> Response:
        result = requests.post(url, json=body, headers=HEADER_TOKEN, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def put(url, body) -> Response:
        result = requests.put(url, json=body, headers=HEADER_TOKEN, cookies=Http_methods.cookie)
        return result

    @staticmethod
    def delete(url, body) -> Response:
        result = requests.delete(url, json=body, headers=HEADER_TOKEN, cookies=Http_methods.cookie)
        return result
