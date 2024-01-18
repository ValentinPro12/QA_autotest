import os

import requests


def find_user():
    request_body = {"UserInfoSearch": {"queryString": "test_test"}, "searchOnlyActive": 0, "excludeRoles": []}
    headers = {"Authorization": "Bearer V28fWJhsiVZgDOcbQtRB8j1u1HQiz2E5"}
    # V28fWJhsiVZgDOcbQtRB8j1u1HQiz2E5
    response = requests.post(url='https://tc-qmt3-dev.telecontact.ru/web/' + 'user/user-info/find-user-info',
                             json=request_body,
                             headers=headers)
    u = response.json()
    print(u)

    dict_1 = {i: u['data'][i] for i in range(len(u['data']))}
    print(dict_1)
    print(dict_1[0]['user_id'])



find_user()
