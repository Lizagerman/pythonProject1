import pytest
from unittest.mock import patch
from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_log_success(caplog):
    result = my_function(1, 2)
    assert "Вызов функции my_function с аргументами (1, 2) и {}" in caplog.text
    assert "Функция my_function вернула результат: 3" in caplog.text
    assert result == 3


def test_log_error(caplog):
    @log()
    def error_function(x):
        return 1 / x

    with pytest.raises(ZeroDivisionError):
        error_function(0)

    assert "Ошибка в функции error_function: ZeroDivisionError - division by zero. Аргументы: (0,), {}" in caplog.text


@log()
def divide(a: int, b: int) -> float:
    return a / b


def test_divide(caplog):
    result = divide(10, 2)
    assert "Вызов функции divide с аргументами (10, 2) и {}" in caplog.text
    assert "Функция divide вернула результат: 5.0" in caplog.text
    assert result == 5.0


def test_divide_by_zero(caplog):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    assert "Ошибка в функции divide: ZeroDivisionError - division by zero. Аргументы: (10, 0), {}" in caplog.text
