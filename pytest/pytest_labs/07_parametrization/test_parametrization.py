import pytest


@pytest.mark.parametrize("input,expected", [
    (1 + 1, 2),
    (2 + 2, 4),
    (3 + 3, 6),
])
def test_addition(input, expected):
    assert input == expected


@pytest.fixture
def sample_data():
    return [1, 2, 3]


@pytest.mark.parametrize("item", [1, 2, 3])
def test_sample_data(sample_data, item):
    assert item in sample_data


@pytest.mark.parametrize("a,b,expected", [
    pytest.param(1, 2, 3, id="one_plus_two"),
    pytest.param(4, 5, 9, id="four_plus_five"),
    pytest.param(10, 20, 30, id="ten_plus_twenty"),
])
def test_addition_with_ids(a, b, expected):
    assert a + b == expected
