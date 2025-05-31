from typing import List, Dict
import pandas as pd
from pathlib import Path # Добавляем для лучшей работы с путями

def read_csv_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из CSV-файла.

    Args:
        path (str): Путь к CSV-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(Path(path)) # Используем Path
        # Убедимся, что ключи словарей являются строками,
        # но сохраняем исходные типы значений.
        records = df.to_dict(orient='records')
        return [
            {str(k): v for k, v in row.items()}
            for row in records
        ]
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл CSV пуст: {path}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении CSV-файла {path}: {e}")
        return []

def read_excel_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из Excel-файла (.xlsx).

    Args:
        path (str): Путь к Excel-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(Path(path), engine="openpyxl") # Используем Path
        # Убедимся, что ключи словарей являются строками,
        # но сохраняем исходные типы значений.
        records = df.to_dict(orient='records')
        return [
            {str(k): v for k, v in row.items()}
            for row in records
        ]
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {path}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтеии Excel-файла {path}: {e}")
        return []

