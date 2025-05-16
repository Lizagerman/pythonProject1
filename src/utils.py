# utils.py

import json
import logging
import os
from typing import List, Dict, Any

# === Настройка логгера для модуля utils ===

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)

# === Функция с типами ===

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    logger.debug(f"Попытка загрузки файла: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
             data: Any = json.load(file)
             if isinstance(data, list):
                 logger.debug(f"Успешно загружено {len(data)} транзакций из {file_path}")
                 return data
             else:
                 logger.error(f"Некорректный формат данных в файле: {file_path}")
                 return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []

"""
Модуль для загрузки списка транзакций из JSON-файла.

Содержит функцию load_transactions, которая безопасно читает данные и возвращает список транзакций.
"""
