import pytest


def test_basic_assertions():
    assert 1 + 1 == 2
    assert "hello".upper() == "HELLO"
    assert len([1, 2, 3]) == 3


def test_assertions_with_messages():
    assert 1 + 1 == 2, "Addition failed"
    assert "hello".upper() == "HELLO", "String conversion failed"
    assert len([1, 2, 3]) == 3, "List length check failed"


def test_approximate():
    assert 0.1 + 0.2 == pytest.approx(0.3)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        print(1 / 0)


def test_value_error():
    with pytest.raises(ValueError, match="invalid literal for int()"):
        int("hello")


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    print(str(excinfo.value))
    assert "maximum recursion" in str(excinfo.value)
