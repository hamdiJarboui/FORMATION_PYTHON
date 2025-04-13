import pytest


@pytest.mark.sanity
def test_addition():
    assert 1 + 1 == 2


@pytest.mark.sanity
def test_subtraction():
    assert 2 - 1 == 1


@pytest.mark.smoke
def test_multiplication():
    assert 2 * 3 == 6


@pytest.mark.regression
def test_division():
    assert 6 / 2 == 3
