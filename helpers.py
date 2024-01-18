from typing import Any

import requests



def expect_equal(check_name: str, actual_value: Any, expected_value: Any):
    """Сравнение фактического значения с ожидаемым, проверяем что равны.

    :param check_name: название проверки
    :param actual_value: фактическое значение
    :param expected_value: ожидаемое значение
    """
    error_text = f"{check_name}. Ожидание: '{expected_value}'. Факт: '{actual_value}"
    assert actual_value == expected_value, error_text


# def find_user_q(username, auth_key):
#     request_body = {"UserInfoSearch": {"queryString": username}, "searchOnlyActive": 0, "excludeRoles": []}
#     headers = {"Authorization": "Bearer V28fWJhsiVZgDOcbQtRB8j1u1HQiz2E5"}
#     # V28fWJhsiVZgDOcbQtRB8j1u1HQiz2E5
#     response = requests.post(url='https://tc-qmt3-dev.telecontact.ru/web/' + 'user/user-info/find-user-info',
#                              json=request_body,
#                              headers=headers)
#     u = response.json()
#     dict_1 = {i: u['data'][i] for i in range(len(u['data']))}
#     delete_user(dict_1[0]['user_id'], auth_key)
#


