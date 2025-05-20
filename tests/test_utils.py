# test_utils.py

import unittest
from unittest.mock import mock_open, patch

from utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"amount": 100, "currency": "RUB"}]',
    )
    def test_load_transactions_valid(self, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 100)

    @patch("os.path.exists", return_value=False)
    def test_load_transactions_file_not_found(self, mock_exists):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_load_transactions_invalid_json(self, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])
