## 5. Organizing Tests

### Test Discovery
**Description**: Pytest automatically discovers tests based on naming conventions and file locations. By default, it looks for files matching the pattern `test_*.py` or `*_test.py` and collects test functions and methods within those files.

**Lab Activity**:
1. **Create Test Files**:
   - Create two test files named `test_math.py` and `math_test.py`.
2. **Write Test Functions**:
   - Add the following code to `test_math.py`:
     ```python
     def test_addition():
         assert 1 + 1 == 2

     def test_subtraction():
         assert 2 - 1 == 1
     ```
   - Add the following code to `math_test.py`:
     ```python
     def test_multiplication():
         assert 2 * 3 == 6

     def test_division():
         assert 6 / 2 == 3
     ```
3. **Run Pytest**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing your test files.
   - Run the command `pytest` to see how Pytest discovers and runs the tests in both files.

### Test Naming Conventions
**Description**: Following consistent naming conventions for test files and functions helps Pytest discover tests easily and makes your test suite more readable. Test files should be named `test_*.py` or `*_test.py`, and test functions should start with `test_`.

**Lab Activity**:
1. **Rename Test Files**:
   - Ensure your test files follow the naming conventions: `test_math.py` and `math_test.py`.
2. **Rename Test Functions**:
   - Ensure all test functions in your files start with `test_`.
3. **Run Pytest**:
   - Run the command `pytest` to verify that all tests are discovered and executed correctly.

### Grouping Tests
**Description**: Grouping tests can be done using classes and modules. This helps organize related tests together and can share setup and teardown logic using fixtures.

**Lab Activity**:
1. **Group Tests Using Classes**:
   - Modify `test_math.py` to group tests into classes:
     ```python
     class TestArithmetic:
         def test_addition(self):
             assert 1 + 1 == 2

         def test_subtraction(self):
             assert 2 - 1 == 1

     class TestMultiplication:
         def test_multiplication(self):
             assert 2 * 3 == 6

         def test_division(self):
             assert 6 / 2 == 3
     ```
2. **Run Pytest**:
   - Run the command `pytest` to see how Pytest discovers and runs the grouped tests.
3. **Group Tests Using Modules**:
   - Create a new directory named `tests`.
   - Move `test_math.py` and `math_test.py` into the `tests` directory.
   - Run the command `pytest tests/` to verify that Pytest discovers and runs the tests in the new structure.

### Using Markers for Grouping
**Description**: Pytest allows you to use markers to group tests. Markers can be used to selectively run tests based on certain criteria, such as test types (sanity, smoke, regression).

**Lab Activity**:
1. **Apply Markers to Tests**:
   - Modify `test_math.py` to include markers for different test types:
     ```python
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
     ```
2. **Run Marked Tests**:
   - Run the command `pytest -m sanity` to run only the tests marked with `sanity`.
   - Run the command `pytest -m smoke` to run only the tests marked with `smoke`.
   - Run the command `pytest -m regression` to run only the tests marked with `regression`.

### Running Tests with Keyword Expressions
**Description**: Pytest allows you to run tests based on keyword expressions using the `-k` option. This is useful for running a subset of tests that match certain conditions.

**Lab Activity**:
1. **Run Tests by Keyword**:
   - Run the command `pytest -k "addition"` to run only the tests whose names contain the keyword `addition`.
   - Run the command `pytest -k "not division"` to run all tests except those whose names contain the keyword `division`.
2. **Combine Keywords**:
   - Run the command `pytest -k "addition or multiplication"` to run tests whose names contain either `addition` or `multiplication`.
   - Run the command `pytest -k "sanity and not subtraction"` to run tests marked with `sanity` but not containing `subtraction`.

These activities will help you understand how Pytest discovers tests, the importance of naming conventions, how to group tests effectively, and how to run tests using different options like `-m` and `-k`. If you need further assistance or additional sections, feel free to ask!
