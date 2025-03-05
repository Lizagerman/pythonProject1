from masks import get_mask_card_number, get_mask_account
from widget import mask_account_card, get_date
from processing import filter_by_state, sort_by_date


# Модуль masks
def test_get_mask_card_number(card_number_data):
    for card_number, expected in card_number_data:
        assert get_mask_card_number(card_number) == expected


def test_get_mask_account(account_data):
    for account_number, expected in account_data:
        assert get_mask_account(account_number) == expected


# Модуль widget
def test_mask_account_card():
    # Пример параметризованные данные
    data = [
        ("card", "1234-5678-9123-4567", "---4567"),
        ("account", "12345678", ""),
    ]
    for acc_type, acc_number, expected in data:
        assert mask_account_card(acc_type, acc_number) == expected


# Модуль processing
def test_filter_by_state():
    data = [{'name': 'item1', 'state': 'active'},
            {'name': 'item2', 'state': 'inactive'}]
    assert filter_by_state(data, 'active') == [{'name': 'item1', 'state': 'active'}]


def test_sort_by_date():
    data = [{'date': '2023-01-01'}, {'date': '2022-01-01'}]
    assert sort_by_date(data) == [{'date': '2023-01-01'}, {'date': '2022-01-01'}]

