
# src/widget.py


def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты или счета."""
    account_type, account_number = account_info.split(' ', 1)
    if 'Счет' not in account_type:
        return mask_account_card(account_number)
    else:
        return mask_account_card(account_number)


def get_date(date_str: str) -> str:
    """Преобразует строку даты в формат 'ДД.ММ.ГГГГ'."""
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")

