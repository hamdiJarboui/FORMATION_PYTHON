import pytest


@pytest.fixture
def first_entry():
    print("\nSetup: First entry fixture")
    yield "a"
    print("\nTeardown: First entry fixture")


@pytest.fixture
def order(first_entry):
    print("\nSetup: Order fixture")
    order_list = [first_entry]
    yield order_list
    print("\nTeardown: Order fixture")


def test_order(order):
    order.append("b")
    assert order == ["a", "b"]

