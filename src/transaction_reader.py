from typing import List, Dict
import pandas as pd


def read_csv_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из CSV-файла.

    Args:
        path (str): Путь к CSV-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    df = pd.read_csv(path)
    records = df.to_dict(orient='records')
    return [dict(map(str, row.items())) for row in records]


def read_excel_transactions(path: str) -> list[dict[str, object]]:
    """
    Считывает транзакции из Excel-файла (.xlsx).

    Args:
        path (str): Путь к Excel-файлу.

    Returns:
        list[dict[str, object]]: Список словарей с транзакциями.
    """
    df = pd.read_excel(path, engine="openpyxl")
    return df.to_dict(orient='records')
