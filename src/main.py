# Модуль masks
from typing import Dict, List, Tuple

from masks import get_mask_account, get_mask_card_number
from processing import filter_by_state, sort_by_date
from widget import get_date, mask_account_card


def test_get_mask_card_number(card_number_data: List[Tuple[str, str]]) -> None:
    """Тестирует функцию get_mask_card_number на различных номерах карт."""
    for card_number, expected in card_number_data:
        assert (
            get_mask_card_number(card_number) == expected
        ), f"Expected {expected} but got {get_mask_card_number(card_number)} for card number {card_number}"


def test_get_mask_account(account_data: List[Tuple[str, str]]) -> None:
    """Тестирует функцию get_mask_account на различных номерах счетов."""
    for account_number, expected in account_data:
        assert (
            get_mask_account(account_number) == expected
        ), f"Expected {expected} but got {get_mask_account(account_number)} for account number {account_number}"


# Модуль widget
from typing import List, Tuple


def test_mask_account_card() -> None:
    """Тестирует функцию mask_account_card на различных типах счетов и карт."""
    # Пример параметризованные данные
    data: List[Tuple[str, str, str]] = [
        ("card", "1234-5678-9123-4567", "---4567"),
        ("account", "12345678", ""),
    ]

    for acc_type, acc_number, expected in data:
        result = mask_account_card(acc_number)
        assert (
            result == expected
        ), f"Expected '{expected}' but got '{result}' for type '{acc_type}' and number '{acc_number}'"


# Модуль processing


def test_filter_by_state() -> None:
    """Тестирует функцию filter_by_state на фильтрации элементов по состоянию."""
    data: List[Dict[str, str]] = [
        {"name": "item1", "state": "active"},
        {"name": "item2", "state": "inactive"},
        {"name": "item3", "state": "active"},
        {"name": "item4", "state": "inactive"},
    ]

    # Тест на фильтрацию активных элементов
    result = filter_by_state(data, "active")
    expected = [
        {"name": "item1", "state": "active"},
        {"name": "item3", "state": "active"},
    ]
    assert (
        result == expected
    ), f"Expected {expected} but got {result} for state 'active'"

    # Тест на фильтрацию неактивных элементов
    result = filter_by_state(data, "inactive")
    expected = [
        {"name": "item2", "state": "inactive"},
        {"name": "item4", "state": "inactive"},
    ]
    assert (
        result == expected
    ), f"Expected {expected} but got {result} for state 'inactive'"

    # Тест на фильтрацию с состоянием, которого нет
    result = filter_by_state(data, "unknown")
    expected = []
    assert (
        result == expected
    ), f"Expected {expected} but got {result} for state 'unknown'"


# Вызов теста
test_filter_by_state()


def test_sort_by_date() -> None:
    """Тестирует функцию sort_by_date на сортировке элементов по дате."""
    data: List[Dict[str, str]] = [
        {"date": "2023-01-01"},
        {"date": "2022-01-01"},
        {"date": "2021-01-01"},
    ]

    # Ожидаемый результат после сортировки по дате
    expected = [
        {"date": "2021-01-01"},
        {"date": "2022-01-01"},
        {"date": "2023-01-01"},
    ]

    # Выполнение сортировки
    result = sort_by_date(data)

    # Проверка результата
    assert result == expected, f"Expected {expected} but got {result}"


# Вызов теста
test_sort_by_date()
