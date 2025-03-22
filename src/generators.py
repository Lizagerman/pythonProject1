# generators.py

def filter_by_currency(transactions, currency):
    """Генератор, который фильтрует транзакции по валюте."""
    for transaction in transactions:
        if transaction.get('currency') == currency:
            yield transaction

def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой транзакции."""
    for transaction in transactions:
        yield f"{transaction.get('date')}: {transaction.get('amount')} {transaction.get('currency')}"

def card_number_generator(start=1, end=9999999999999999):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        yield f"{number:016d}"  # Форматируем номер карты с ведущими нулями
        