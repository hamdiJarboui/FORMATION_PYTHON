# Course Plan for Pytest Using Python

## 8. Markers and Customization

### Using Markers
**Description**: Markers in Pytest allow you to add metadata to your test functions. This metadata can be used to selectively run tests, skip tests, or apply custom behaviors. Markers are a powerful way to organize and manage your test suite, especially when dealing with large numbers of tests.

**Lab Activity**:
1. **Basic Usage of Markers**:
   - Create a new file named `test_markers.py`.
   - Add the following code to define tests with markers:
     ```python
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
     ```
   - This code marks tests with different types such as `sanity`, `smoke`, and `regression`.

2. **Running Tests with Markers**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing your test file.
   - Run the command `pytest -m sanity` to run only the tests marked with `sanity`.
   - Run the command `pytest -m smoke` to run only the tests marked with `smoke`.
   - Run the command `pytest -m regression` to run only the tests marked with `regression`.

### Custom Markers
**Description**: Custom markers allow you to define your own markers to categorize and manage your tests. You can register custom markers in the `pytest.ini` file to avoid warnings and to provide descriptions for the markers.

**Lab Activity**:
1. **Define Custom Markers**:
   - Create a `pytest.ini` file in your project directory.
   - Add the following content to register custom markers:
     ```ini
     [pytest]
     markers =
         sanity: marks tests as sanity tests
         smoke: marks tests as smoke tests
         regression: marks tests as regression tests
         performance: marks tests as performance tests
         slow: marks tests as slow tests
     ```

2. **Apply Custom Markers**:
   - Modify `test_markers.py` to use the registered custom markers:
     ```python
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

     @pytest.mark.performance
     def test_performance():
         assert perform_heavy_computation() < 1

     @pytest.mark.slow
     def test_slow():
         import time
         time.sleep(5)
         assert True
     ```

3. **Run Tests with Custom Markers**:
   - Run the command `pytest -m sanity` to run only the tests marked with `sanity`.
   - Run the command `pytest -m smoke` to run only the tests marked with `smoke`.
   - Run the command `pytest -m regression` to run only the tests marked with `regression`.
   - Run the command `pytest -m performance` to run only the tests marked with `performance`.
   - Run the command `pytest -m slow` to run only the tests marked with `slow`.

### Advanced Marker Usage
**Description**: Pytest markers can be used for more advanced scenarios, such as skipping tests, expecting failures, and applying markers to entire classes or modules.

**Lab Activity**:
1. **Skipping Tests**:
   - Add the following code to `test_markers.py` to demonstrate skipping tests:
     ```python
     @pytest.mark.skip(reason="Skipping this test for demonstration purposes")
     def test_skip():
         assert 1 == 1
     ```

2. **Expected Failures**:
   - Add the following code to demonstrate expected failures:
     ```python
     @pytest.mark.xfail(reason="This test is expected to fail")
     def test_expected_failure():
         assert 1 == 2
     ```

3. **Applying Markers to Classes**:
   - Add the following code to demonstrate applying markers to classes:
     ```python
     @pytest.mark.regression
     class TestMathOperations:
         def test_addition(self):
             assert 1 + 1 == 2

         def test_subtraction(self):
             assert 2 - 1 == 1
     ```

4. **Combining Markers**:
   - Add the following code to demonstrate combining markers:
     ```python
     @pytest.mark.sanity
     @pytest.mark.smoke
     def test_combined_markers():
         assert 1 + 1 == 2
     ```

### Using Built-in Markers
**Description**: Pytest comes with several built-in markers that provide additional functionality, such as skipping tests under certain conditions, marking tests as expected to fail, and using fixtures.

**Lab Activity**:
1. **Using skipif**:
   - Add the following code to demonstrate using `skipif`:
     ```python
     import sys

     @pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
     def test_not_on_windows():
         assert True
     ```

2. **Using xfail**:
   - Add the following code to demonstrate using `xfail`:
     ```python
     @pytest.mark.xfail(reason="This test is expected to fail")
     def test_expected_failure():
         assert 1 == 2
     ```

3. **Using usefixtures**:
   - Add the following code to demonstrate using `usefixtures`:
     ```python
     @pytest.fixture
     def setup():
         print("\nSetup fixture")

     @pytest.mark.usefixtures("setup")
     def test_with_fixture():
         assert True
     ```

### Best Practices for Using Markers
**Description**: When using markers, it's important to follow best practices to ensure your tests are maintainable and readable. Use descriptive marker names, register custom markers to avoid warnings, and apply markers consistently across your test suite.

**Lab Activity**:
1. **Descriptive Marker Names**:
   - Ensure your marker names are descriptive and meaningful.
   - Example:
     ```python
     @pytest.mark.performance
     def test_performance():
         assert perform_heavy_computation() < 1
     ```

2. **Register Custom Markers**:
   - Always register custom markers in the `pytest.ini` file to avoid warnings.
   - Example:
     ```ini
     [pytest]
     markers =
         performance: marks tests as performance tests
     ```

3. **Consistent Marker Application**:
   - Apply markers consistently across your test suite to maintain organization and readability.
   - Example:
     ```python
     @pytest.mark.performance
     def test_performance_1():
         assert perform_heavy_computation() < 1

     @pytest.mark.performance
     def test_performance_2():
         assert perform_heavy_computation() < 2
     ```

These activities will help you understand how to use markers in Pytest, including marking tests for selective runs, creating and using custom markers, and applying advanced marker usage techniques. If you need further assistance or additional sections, feel free to ask!
