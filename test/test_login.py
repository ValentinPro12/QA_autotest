import os

from steps.authorize_steps import login


def test_success_login_with_qmt_type():
    """Успешная авторизация пользователя с типом входа QMT."""
    login(
        username=os.getenv('USER_QMT'),
        password=os.getenv('PASSWORD_QMT'),
        remember_me=1,
        auth_type="QMT",
        expected_status_code=200
    )


def test_success_login_with_aaa_type():
    """Успешная авторизация пользователя с типом входа AAA."""
    login(
        username=os.getenv('USER_AAA'),
        password=os.getenv('PASSWORD_AAA'),
        remember_me=1,
        auth_type="AAA",
        expected_status_code=200
    )


def test_failed_login_with_not_valid_type():
    """Неуспешная авторизация пользователя с невалидным типом входа."""
    login(
        username="6759",
        password="jH6kd*(",
        remember_me=1,
        auth_type="FFF",
        expected_status_code=404  # подставить ожидаемый код ответа
    )
