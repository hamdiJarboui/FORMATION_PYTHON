import pytest


@pytest.mark.sanity
def test_addition():
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_subtraction():
    assert 2 - 1 == 1


@pytest.mark.regression
def test_multiplication():
    assert 2 * 3 == 6


@pytest.mark.regression
def test_division():
    assert 6 / 2 == 3


@pytest.mark.slow
def test_slow():
    import time
    time.sleep(5)
    assert True


@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_skip():
    assert 1 == 1


@pytest.mark.xfail(reason="This test is expected to fail")
def test_expected_failure():
    assert 1 == 2


@pytest.mark.sanity
@pytest.mark.smoke
def test_combined_markers():
    assert 1 + 1 == 2


import sys


@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_not_on_windows():
    assert True


@pytest.fixture
def setup():
    print("\nSetup fixture")
    return [1,2,3,4,5]

@pytest.mark.usefixtures("setup")
def test_with_fixture():
    setup.append(8)
    assert True

def test_with_fixture2(setup):
    setup.append(8)
    assert True