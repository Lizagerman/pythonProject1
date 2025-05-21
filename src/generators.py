# generators.py
from typing import Any, Dict, Generator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency: str
) -> Generator[Dict[str, Any], None, None]:
    """Генератор, который фильтрует транзакции по валюте."""
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]],
) -> Generator[str, None, None]:
    """Генератор, который возвращает описание каждой транзакции."""
    for transaction in transactions:
        yield f"{transaction.get('date')}: {transaction.get('amount')} {transaction.get('currency')}"


def card_number_generator(
    start: int = 1, stop: int = 9999999999999999
) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        yield f"{number:016d}"  # Форматируем номер карты с ведущими нулями
