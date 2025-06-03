import transaction
from typing import List, Dict, Any

def search_transactions_by_description(
    transactions: List[Dict[str, Any]], search_string: str
) -> List[Dict[str, Any]]:
    """
    Ищет банковские операции по заданной строке в описании с использованием
    регулярных выражений.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка для поиска в описании операций.
    :return: Список словарей с операциями, у которых в описании есть заданная строка.
    """
    global transaction
    found_transactions: List[Dict[str, Any]] = []
    # Компилируем регулярное выражение для более эффективного поиска
    # re.IGNORECASE позволяет игнорировать регистр
    pattern = transaction.compile(search_string, transaction.IGNORECASE)
    for transaction in transactions:
        if "description" in transaction and pattern.search(transaction["description"]):
            found_transactions.append(transaction)
    return found_transactions
