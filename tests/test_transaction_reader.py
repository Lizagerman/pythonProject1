from typing import Dict, List
from unittest.mock import patch

import pandas as pd

from src.transaction_reader import read_csv_transactions, read_excel_transactions


def test_read_csv_transactions() -> None:
    fake_data: List[Dict[str, object]] = [
        {"date": "2024-01-01", "amount": 1000.0, "category": "Salary"},
        {"date": "2024-01-02", "amount": -200.0, "category": "Groceries"},
    ]
    with patch("pandas.read_csv", return_value=pd.DataFrame(fake_data)):
        result = read_csv_transactions("fake.csv")
        assert result == fake_data


def test_read_excel_transactions() -> None:
    fake_data: List[Dict[str, object]] = [
        {"date": "2024-01-03", "amount": -50.0, "category": "Transport"},
        {"date": "2024-01-04", "amount": -100.0, "category": "Utilities"},
    ]
    with patch("pandas.read_excel", return_value=pd.DataFrame(fake_data)):
        result = read_excel_transactions("fake.xlsx")
        assert result == fake_data
