from collections import Counter
from typing import List, Dict, Any, Counter as TypeCounter


def count_transactions_by_category(
    transactions: List[Dict[str, Any]], category_keywords: Dict[str, List[str]]
) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по заданным категориям.

    :param transactions: Список словарей с данными о банковских операциях.
    :param category_keywords: Словарь, где ключи - названия категорий,
    а значения - список ключевых слов,
     по которым определять категорию в описании транзакции.
    :return: Словарь, в котором ключи - названия категорий,
    а значения - количество операций в каждой категории.
    """
    category_counts: TypeCounter[str] = Counter()
    for transaction in transactions:
        if "description" in transaction:
            description = transaction[
                "description"
            ].lower()  # Приводим к нижнему регистру для сравнения
            found_category = False
            for category_name, keywords in category_keywords.items():
                for keyword in keywords:
                    if keyword.lower() in description:
                        category_counts[category_name] += 1
                        found_category = True
                        break  # Прерываем внутренний цикл,
                        # если нашли ключевое слово для этой категории
                if found_category:
                    break  # Прерываем внешний цикл, если нашли категорию для транзакции
    return dict(category_counts)
