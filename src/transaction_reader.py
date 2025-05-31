import pandas as pd
from typing import Dict, List


def read_csv_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из CSV-файла.

    Args:
        path (str): Путь к CSV-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    df = pd.read_csv(path)
    # Возвращаем список словарей, сохраняя исходные типы данных, определенные Pandas.
    # Больше нет преобразования всех значений в строки.
    return df.to_dict(orient="records")


def read_excel_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из Excel-файла (.xlsx).

    Args:
        path (str): Путь к Excel-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    df = pd.read_excel(path, engine="openpyxl")
    # Здесь тоже сохраняются исходные типы данных, определенные Pandas.
    return df.to_dict(orient="records")