import pytest
import logging
from decorators import log


import pytest
import logging
from src import log  # Замените your_module на имя вашего модуля

@log()
def add(a: int, b: int) -> int:
    return a + b

@log()
def divide(a: int, b: int) -> float:
    return a / b

def test_add(caplog):
    with caplog.at_level(logging.INFO):
        result = add(2, 3)

    assert "Calling function: add with args: (2, 3) and kwargs: {}" in caplog.text
    assert "Function: add returned: 5" in caplog.text

def test_divide(caplog):
    with caplog.at_level(logging.INFO):
        result = divide(10, 2)

    assert "Calling function: divide with args: (10, 2) and kwargs: {}" in caplog.text
    assert "Function: divide returned: 5.0" in caplog.text

def test_divide_by_zero(caplog):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)



# Определяем функцию add с декоратором log
@log()
def add(a: int, b: int) -> int:
    return a + b


# Определяем функцию divide с декоратором log
@log()
def divide(a: int, b: int) -> float:
    return a / b


# Тест для успешного вызова функции
def test_log_success(capsys):
    result = add(1, 2)
    captured = capsys.readouterr()
    assert "Calling function: add with args: (1, 2) and kwargs: {}" in captured.out
    assert "Function: add returned: 3" in captured.out


# Тест для обработки ошибок
def test_log_error(capsys):
    @log()
    def error_function(x):
        return 1 / x

    with pytest.raises(ZeroDivisionError):
        error_function(0)

    captured = capsys.readouterr()
    assert "Function: error_function raised an error: ZeroDivisionError with args: (0,)" in captured.err


# Тест для функции add
def test_add(caplog):  # подключаем caplog
    with caplog.at_level(logging.INFO):  # Устанавливаем уровень логирования
        result = add(2, 3)

    # Проверяем логи
    assert "Вызов функции add с аргументами (2, 3) и {}" in caplog.text
    assert "Функция add вернула результат: 5" in caplog.text


# Тест для функции divide
def test_divide(capsys):
    result = divide(10, 2)

    captured = capsys.readouterr()

    assert "Вызов функции divide с аргументами (10, 2) и {}" in captured.out
    assert "Функция divide вернула результат: 5.0" in captured.out


# Тест для деления на ноль
def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()

    assert "Ошибка в функции divide: ZeroDivisionError - division by zero." in captured.err

