from typing import Any


def expect_equal(check_name: str, actual_value: Any, expected_value: Any):
    """Сравнение фактического значения с ожидаемым, проверяем что равны.

    :param check_name: название проверки
    :param actual_value: фактическое значение
    :param expected_value: ожидаемое значение
    """
    error_text = f"{check_name}. Ожидание: '{expected_value}'. Факт: '{actual_value}"
    print(error_text)
    assert actual_value == expected_value, error_text


def expected_response(check_name: str, actual_value: Any, expected_value: Any):
    """Сравнение фактического значения с ожидаемым, проверяем что равны.

    :param check_name: название проверки
    :param actual_value: фактическое значение
    :param expected_value: ожидаемое значение
    """
    error_text = f"{check_name}. Ожидание: '{expected_value}'. Факт: '{actual_value}"
    print(error_text)
    assert actual_value == expected_value, error_text
