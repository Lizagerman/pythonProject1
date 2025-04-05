import pytest
from decorators import log
import decorators


@log()
def test_function(x, y):
    return x + y


def test_log_success(capsys):
    test_function(1, 2)
    captured = capsys.readouterr()
    assert "Calling function: test_function with args: (1, 2) and kwargs: {}" in captured.out
    assert "Function: test_function returned: 3" in captured.out


def test_log_error(capsys):
    @log()
    def error_function(x):
        return 1 / x

    with pytest.raises(ZeroDivisionError):
        error_function(0)

    captured = capsys.readouterr()
    assert "Function: error_function raised an error: ZeroDivisionError with args: (0,)" in captured.err


import pytest
import io
import sys
from decorators import log


# Пример функции для тестирования декоратора
@log()
def add(a: int, b: int) -> int:
    return a + b


@log()
def divide(a: int, b: int) -> float:
    return a / b


# Тесты для декоратора log
def test_add(capsys):
    add(2, 3)

    captured = capsys.readouterr()

    assert "Вызов функции add с аргументами (2, 3) и {}" in captured.out
    assert "Функция add вернула результат: 5" in captured.out


def test_divide(capsys):
    divide(10, 2)

    captured = capsys.readouterr()

    assert "Вызов функции divide с аргументами (10, 2) и {}" in captured.out
    assert "Функция divide вернула результат: 5.0" in captured.out


def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()

    assert "Ошибка в функции divide: ZeroDivisionError - division by zero. Аргументы: (10,), {0}" in captured.err

