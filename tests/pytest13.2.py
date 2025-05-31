# test_transactions.py
import pytest
from your_module import search_transactions_by_description, count_transactions_by_category
# Предполагается, что твои функции находятся в файле your_module.py

@pytest.fixture
def sample_transactions():
    """Фикстура для тестовых данных транзакций."""
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "40542.00", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "from": "Счет 4321",
            "to": "Счет 4321"
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2019-11-12T17:15:36.438502",
            "operationAmount": {"amount": "130.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "MasterCard 7771 27** **** 3727",
            "to": "Visa Platinum 1293 38** **** 9203"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2018-07-18T10:04:14.538189",
            "operationAmount": {"amount": "8390.00", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 7492 65** **** 7202",
            "to": "Счет 0034"
        },
        {
            "id": 4,
            "state": "PENDING",
            "date": "2018-06-03T18:34:03.438502",
            "operationAmount": {"amount": "8200.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 2935",
            "to": "Счет 4321"
        },
        {
            "id": 5,
            "state": "EXECUTED",
            "date": "2020-01-01T12:00:00.000000",
            "operationAmount": {"amount": "500.00", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Покупка продуктов",
            "from": "Счет 1234",
            "to": "Магазин 5678"
        }
    ]

def test_search_transactions_by_description(sample_transactions):
    # Тест на поиск "Перевод"
    results = search_transactions_by_description(sample_transactions, "Перевод")
    assert len(results) == 3
    assert results[0]["id"] == 2
    assert results[1]["id"] == 3
    assert results[2]["id"] == 4

    # Тест на регистронезависимый поиск "вклад"
    results = search_transactions_by_description(sample_transactions, "ВКЛАД")
    assert len(results) == 1
    assert results[0]["id"] == 1

    # Тест на отсутствие совпадений
    results = search_transactions_by_description(sample_transactions, "Аренда")
    assert len(results) == 0

    # Тест на частичное совпадение
    results = search_transactions_by_description(sample_transactions, "карта")
    assert len(results) == 1
    assert results[0]["id"] == 2

def test_count_transactions_by_category(sample_transactions):
    category_keywords = {
        "Переводы": ["перевод", "счет", "карта"],
        "Вклады": ["вклад"],
        "Покупки": ["покупка", "магазин"]
    }

    counts = count_transactions_by_category(sample_transactions, category_keywords)
    assert counts.get("Переводы") == 4 # Перевод с карты, Перевод организации, Перевод со счета, Открытие вклада (вклад может быть на счет)
    assert counts.get("Вклады") == 1
    assert counts.get("Покупки") == 1
    assert "Неизвестная" not in counts # Проверяем, что нет лишних категорий

    # Тест с пустым списком транзакций
    counts = count_transactions_by_category([], category_keywords)
    assert counts == {}

    # Тест с пустым словарем категорий
    counts = count_transactions_by_category(sample_transactions, {})
    assert counts == {}

