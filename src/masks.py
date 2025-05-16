# masks.py

import logging
import os

# === Настройка логгера для модуля masks ===

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)

# === Типизированные функции ===

def get_mask_card_number(card_number: str) -> str:
    """Замаскировать номер банковской карты,
    оставляя последние 4 цифры видимыми."""
    try:
        masked = "*" * (len(card_number) - 4) + card_number[-4:]
        logger.debug(f"Маскирование карты выполнено: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера карты: {e}")
        return ""

def get_mask_account(account_number: str) -> str:
    """Замаскировать номер банковского счета,
    оставляя последние 4 цифры видимыми."""
    try:
        masked = "*" * (len(account_number) - 4) + account_number[-4:]
        logger.debug(f"Маскирование счета выполнено: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера счета: {e}")
        return ""
