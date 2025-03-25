import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

@pytest.mark.parametrize("n, expected", [
    (1, 3),  # Изменено с 2 на 3
    (2, 4),
    (3, 5),
])
def test_increment(sample_list, n, expected):
    assert sample_list[n] + 1 == expected
