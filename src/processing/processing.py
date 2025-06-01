from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    transactions: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """Фильтрует список транзакций по заданному состоянию."""
    return [
        transaction for transaction in transactions if transaction.get("state") == state
    ]


def sort_by_date(
    transactions: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """Сортирует список транзакций по дате."""
    return sorted(
        transactions,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"),
        reverse=descending,
    )

    def filter_by_state(data, state):
        return [item for item in data if item["state"] == state]

    def sort_by_date(data, reverse=False):
        return sorted(data, key=lambda x: x["date"], reverse=reverse)
