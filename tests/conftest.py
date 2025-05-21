import pytest

from src.widget import get_date


@pytest.fixture
def card_number_data():
    return [
        ("1234-5678-9123-4567", "---4567"),
        ("", None),  # случай, где отсутствует номер карты
        ("1234-5678", "-5678"),
    ]


@pytest.fixture
def account_data():
    return [
        ("12345678", ""),
        ("12", None),  # номер счета меньше ожидаемой длины
        ("1234567890123456", "3456"),
    ]


@pytest.mark.parametrize(
    "input,expected",
    [
        ("2023-01-01", "2023-01-01"),
        ("not_a_date", None),  # некорректный формат
    ],
)
def test_get_date(input, expected):
    """

    :type expected: object
    """
    assert get_date(input) == expected
