import pytest


@pytest.fixture
def sample_data():
    print("\nSetup: Creating sample data")
    data = {"name": "John", "age": 30}
    yield data
    print("\nTeardown: Sample data cleanup")


def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30


@pytest.fixture
def init_list():
    print('fixture started')
    initial_list = [1, 2, 3, 4, 5, 6]
    print(initial_list)
    return initial_list


def test_print_list_items(init_list):
    print(init_list[1:])


@pytest.fixture(scope="function")
def function_scope_fixture():
    print("\nSetup: Function scope fixture")
    yield "function scope"
    print("\nTeardown: Function scope fixture")


def test_function_scope(function_scope_fixture):
    assert function_scope_fixture == "function scope"


@pytest.fixture(scope="module")
def module_scope_fixture():
    print("\nSetup: Module scope fixture")
    yield "module scope"
    print("\nTeardown: Module scope fixture")


def test_module_scope_1(module_scope_fixture):
    assert module_scope_fixture == "module scope"


def test_module_scope_2(module_scope_fixture):
    assert module_scope_fixture == "module scope"
