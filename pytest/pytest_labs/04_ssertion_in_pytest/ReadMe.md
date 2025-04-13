
## 4. Assertions in Pytest

### Basic Assertions
**Description**: Assertions are used to verify that a certain condition holds true. In Pytest, you can use the standard Python `assert` statement to write assertions. If the condition is true, the test passes; if it is false, the test fails, and Pytest provides detailed information about the failure.

**Lab Activity**:
1. **Create a Test File**:
   - Create a new file named `test_assertions.py`.
2. **Write Basic Assertions**:
   - Add the following code to `test_assertions.py`:
     ```python
     def test_basic_assertions():
         assert 1 + 1 == 2
         assert "hello".upper() == "HELLO"
         assert len([1, 2, 3]) == 3
     ```
   - This function tests basic assertions for arithmetic, string methods, and list length.

### Advanced Assertions
**Description**: Pytest supports advanced assertions, including checking for exceptions and approximate values. These features help in writing more comprehensive tests.

**Lab Activity**:
1. **Assertions with Messages**:
   - Modify `test_assertions.py` to include custom messages:
     ```python
     def test_assertions_with_messages():
         assert 1 + 1 == 2, "Addition failed"
         assert "hello".upper() == "HELLO", "String conversion failed"
         assert len([1, 2, 3]) == 3, "List length check failed"
     ```

2. **Assertions for Exceptions**:
   - Add tests to check for exceptions:
     ```python
     import pytest

     def test_zero_division():
         with pytest.raises(ZeroDivisionError):
             1 / 0

     def test_value_error():
         with pytest.raises(ValueError, match="invalid literal for int()"):
             int("hello")
     ```
   - These tests check if the correct exceptions are raised and if the exception messages match the expected patterns.

3. **Approximate Assertions**:
   - Add tests for approximate values:
     ```python
     def test_approximate():
         assert 0.1 + 0.2 == pytest.approx(0.3)
     ```

### Assertions for Exceptions
**Description**: Pytest provides a way to assert that exceptions are raised using the `pytest.raises` context manager. This is useful for testing error conditions and ensuring that your code handles exceptions correctly.

**Lab Activity**:
1. **Basic Exception Assertion**:
   - Add the following code to `test_assertions.py`:
     ```python
     import pytest

     def test_zero_division():
         with pytest.raises(ZeroDivisionError):
             1 / 0
     ```
   - This test checks if a `ZeroDivisionError` is raised when dividing by zero.

2. **Accessing Exception Information**:
   - Modify the test to access the exception information:
     ```python
     def test_recursion_depth():
         with pytest.raises(RuntimeError) as excinfo:
             def f():
                 f()
             f()
         assert "maximum recursion" in str(excinfo.value)
     ```
   - This test checks if a `RuntimeError` with a specific message is raised due to maximum recursion depth.

3. **Matching Exception Messages**:
   - Add a test to match exception messages using regular expressions:
     ```python
     def myfunc():
         raise ValueError("Exception 123 raised")

     def test_match():
         with pytest.raises(ValueError, match=r".* 123 .*"):
             myfunc()
     ```

### Understanding Assertion Failures
**Description**: When an assertion fails, Pytest provides detailed information about the failure, including the values involved in the assertion. This helps in debugging and understanding why the test failed.

**Lab Activity**:
1. **Introduce Failures**:
   - Modify `test_assertions.py` to introduce failures:
     ```python
     def test_failures():
         assert 1 + 1 == 3
         assert "hello".upper() == "HELLO!"
         assert len([1, 2, 3]) == 4
     ```
   - Run the tests using `pytest test_assertions.py` and observe the detailed failure messages provided by Pytest.
   - Example output:
     ```
     ============================= test session starts ==============================
     platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
     collected 3 items

     test_assertions.py FFF                                                 [100%]

     =================================== FAILURES ===================================
     ______________________________ test_failures _________________________________
     test_assertions.py:2: in test_failures
         assert 1 + 1 == 3
     E       assert 2 == 3
     E        +  where 2 = (1 + 1)

     test_assertions.py:3: in test_failures
         assert "hello".upper() == "HELLO!"
     E       AssertionError: assert 'HELLO' == 'HELLO!'
     E         - HELLO
     E         + HELLO!

     test_assertions.py:4: in test_failures
         assert len([1, 2, 3]) == 4
     E       assert 3 == 4
     E        +  where 3 = len([1, 2, 3])

     ========================== short test summary info ============================
     FAILED test_assertions.py::test_failures - assert 2 == 3
     FAILED test_assertions.py::test_failures - AssertionError: assert 'HELLO' == 'HELLO!'
     FAILED test_assertions.py::test_failures - assert 3 == 4
     ============================== 3 failed in 0.01s ===============================
     ```

These activities will help you understand and use assertions in Pytest effectively, including handling exceptions and using advanced assertion features like `pytest.raises` and `pytest.approx`. If you need further assistance or additional sections, feel free to ask!
