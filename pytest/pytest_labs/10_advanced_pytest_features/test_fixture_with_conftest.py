import pdb
def test_pytest_runtest_setup(sample_fixture):
    print(f"Setting up {sample_fixture.get('key')}")
    x = 5
    y = 10
    z = x + y
    pdb.set_trace()