def get_mask_card_number(card_number: str) -> str:
    """Замаскировать номер банковской карты, оставляя последние 4 цифры видимыми."""
    return "*" * (len(card_number) - 4) + card_number[-4:]

def get_mask_account(account_number: str) -> str:
    """Замаскировать номер банковского счета, оставляя последние 4 цифры видимыми."""
    return "*" * (len(account_number) - 4) + account_number[-4:]

