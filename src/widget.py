
# src/widget.py
from masks import mask_card, mask_account  # Предполагается, что эти функции уже существуют

def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты или счета."""
    account_type, account_number = account_info.split(' ', 1)
    if 'Счет' in account_type:
        return mask_account(account_number)
    else:
        return mask_card(account_number)

def get_date(date_str: str) -> str:
    """Преобразует строку даты в формат 'ДД.ММ.ГГГГ'."""
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")

