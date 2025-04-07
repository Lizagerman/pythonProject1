import pytest
from unittest.mock import patch
from decorators import log


@log()
def my_function(x, y):
    return x + y


def test_log_success():
    with patch('builtins.print') as mock_print:
        result = my_function(1, 2)
        mock_print.assert_any_call("Вызов функции my_function с аргументами (1, 2) и {}")
        mock_print.assert_any_call("Функция my_function вернула результат: 3")
        assert result == 3


def test_log_error():
    @log()
    def error_function(x):
        return 1 / x

    with patch('builtins.print') as mock_print:
        with pytest.raises(ZeroDivisionError):
            error_function(0)

        mock_print.assert_any_call("Ошибка в функции error_function: ZeroDivisionError - division by zero. Аргументы: (0,), {}")


# Пример функции для тестирования декоратора
@log()
def add(a: int, b: int) -> int:
    return a + b


@log()
def divide(a: int, b: int) -> float:
    return a / b


# Тесты для декоратора log
def test_add():
    with patch('builtins.print') as mock_print:
        result = add(2, 3)
        mock_print.assert_any_call("Вызов функции add с аргументами (2, 3) и {}")
        mock_print.assert_any_call("Функция add вернула результат: 5")
        assert result == 5


def test_divide():
    with patch('builtins.print') as mock_print:
        result = divide(10, 2)
        mock_print.assert_any_call("Вызов функции divide с аргументами (10, 2) и {}")
        mock_print.assert_any_call("Функция divide вернула результат: 5.0")
        assert result == 5.0


def test_divide_by_zero():
    with patch('builtins.print') as mock_print:
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        mock_print.assert_any_call("Ошибка в функции divide: ZeroDivisionError - division by zero. Аргументы: (10, 0), {}")
