def filter_by_state(transactions, state='EXECUTED'):
    """Фильтрует список транзакций по заданному состоянию."""
    return [transaction for transaction in transactions if transaction.get('state') == state]

from datetime import datetime

   def sort_by_date(transactions, descending=True):
       """Сортирует список транзакций по дате."""
       return sorted(transactions, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=descending)

