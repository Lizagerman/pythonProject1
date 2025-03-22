# test_generators.py

import unittest
from generators import filter_by_currency, transaction_descriptions, card_number_generator

class TestGenerators(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {'date': '2023-01-01', 'amount': 100, 'currency': 'USD'},
            {'date': '2023-01-02', 'amount': 200, 'currency': 'EUR'},
            {'date': '2023-01-03', 'amount': 150, 'currency': 'USD'},
        ]

    def test_filter_by_currency(self):
        filtered = list(filter_by_currency(self.transactions, 'USD'))
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0]['amount'], 100)
        self.assertEqual(filtered[1]['amount'], 150)

    def test_transaction_descriptions(self):
        descriptions = list(transaction_descriptions(self.transactions))
        self.assertEqual(len(descriptions), 3)
        self.assertEqual(descriptions[0], '2023-01-01: 100 USD')

    def test_card_number_generator(self):
        generator = card_number_generator(1, 5)
        generated_numbers = list(generator)
        self.assertEqual(len(generated_numbers), 5)
        self.assertEqual(generated_numbers[0], '0000000000000001')
        self.assertEqual(generated_numbers[-1], '0000000000000005')

if __name__ == '__main__':
    unittest.main()

