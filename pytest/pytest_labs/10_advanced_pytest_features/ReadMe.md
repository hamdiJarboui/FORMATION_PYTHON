# Course Plan for Pytest Using Python

## 10. Advanced Pytest Features

### Test Configuration
**Description**: Pytest allows you to configure various settings and behaviors using configuration files such as `pytest.ini`, `conftest.py`, `setup.cfg`, and `pyproject.toml`. These files help you manage test settings, plugins, and other configurations in a centralized manner.

**Lab Activity**:
1. **Using `pytest.ini`**:
   - Create a `pytest.ini` file in your project directory.
   - Add the following content to configure test settings:
     ```ini
     [pytest]
     addopts = -v --maxfail=3
     markers =
         sanity: marks tests as sanity tests
         smoke: marks tests as smoke tests
         regression: marks tests as regression tests
     ```
   - This configuration sets verbose output, limits the number of test failures to three, and registers custom markers.

2. **Using `conftest.py`**:
   - Create a `conftest.py` file in your test directory.
   - Add the following code to define fixtures and hooks:
     ```python
     import pytest

     @pytest.fixture
     def sample_fixture():
         return {"key": "value"}

     def pytest_runtest_setup(item):
         print(f"Setting up {item.name}")
     ```
   - This configuration defines a fixture and a hook function that runs before each test.

3. **Using `setup.cfg`**:
   - Create a `setup.cfg` file in your project directory.
   - Add the following content to configure test settings:
     ```ini
     [tool:pytest]
     addopts = -v --maxfail=3
     ```
   - This configuration sets verbose output and limits the number of test failures to three.

### Mocking
**Description**: Mocking is a technique used to replace real objects with mock objects during testing. This allows you to isolate the code being tested and control its behavior. The `pytest-mock` plugin provides a simple interface for mocking objects in your tests.

**Lab Activity**:
1. **Install `pytest-mock`**:
   - Install the plugin using pip:
     ```sh
     pip install pytest-mock
     ```

2. **Basic Mocking Example**:
   - Create a new file named `test_mocking.py`.
   - Add the following code to demonstrate basic mocking:
     ```python
     def test_mocking_example(mocker):
         mock = mocker.Mock()
         mock.return_value = 42
         assert mock() == 42
     ```

3. **Mocking a Function**:
   - Add the following code to mock a function:
     ```python
     import mymodule

     def test_mock_function(mocker):
         mocker.patch('mymodule.myfunction', return_value=42)
         assert mymodule.myfunction() == 42
     ```

4. **Mocking an Object Method**:
   - Add the following code to mock an object method:
     ```python
     class MyClass:
         def mymethod(self):
             return 42

     def test_mock_method(mocker):
         instance = MyClass()
         mocker.patch.object(instance, 'mymethod', return_value=24)
         assert instance.mymethod() == 24
     ```

### Debugging Tests
**Description**: Debugging tests is crucial for identifying and fixing issues in your code. Pytest provides several techniques and tools to help you debug failing tests, including built-in debugging support, integration with debuggers, and detailed error messages.

**Lab Activity**:
1. **Using Built-in Debugging**:
   - Add the following code to a test file to demonstrate built-in debugging:
     ```python
     def test_debugging():
         x = 1
         y = 2
         assert x + y == 4
     ```
   - Run the test with the `--pdb` option to start the debugger on failure:
     ```sh
     pytest --pdb
     ```

2. **Using `pdb` for Debugging**:
   - Add the following code to a test file to demonstrate using `pdb`:
     ```python
     import pdb

     def test_pdb():
         x = 1
         y = 2
         pdb.set_trace()
         assert x + y == 4
     ```
   - Run the test and use the `pdb` commands to inspect variables and step through the code.

3. **Using `pytest` with IDE Debuggers**:
   - Most modern IDEs (e.g., PyCharm, VSCode) support debugging Pytest tests directly within the IDE. Set breakpoints in your test code and run the tests in debug mode from the IDE.

4. **Analyzing Detailed Error Messages**:
   - Pytest provides detailed error messages that help you understand why a test failed. Run the following test to see an example:
     ```python
     def test_error_message():
         x = 1
         y = 2
         assert x + y == 4
     ```
   - Observe the detailed error message provided by Pytest.

These activities will help you understand advanced Pytest features, including test configuration, mocking, and debugging techniques. If you need further assistance or additional sections, feel free to ask!
