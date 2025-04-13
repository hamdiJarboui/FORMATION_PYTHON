
## 3. Basic Pytest Usage

### Writing Your First Test
**Description**: Creating a simple test function is the first step in using Pytest. A test function is a regular Python function that uses assertions to check if the code behaves as expected. Pytest automatically identifies test functions by looking for functions whose names start with `test_`.

**Lab Activity**:
1. **Create a Test File**:
   - Create a new file named `test_example.py`.
2. **Write a Simple Test Function**:
   - Add the following code to `test_example.py`:
     ```python
     def test_addition():
         assert 1 + 1 == 2
     ```
   - This function tests if the addition of 1 and 1 equals 2.
3. **Write Another Test Function**:
   - Add another test function to the same file:
     ```python
     def test_subtraction():
         assert 2 - 1 == 1
     ```

### Running Tests
**Description**: Pytest provides a simple command-line interface to run tests. You can run all tests in a directory or specify a particular test file. Pytest will automatically discover all test files and functions based on naming conventions.

**Lab Activity**:
1. **Run All Tests in a Directory**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing your test files.
   - Run the command `pytest` to execute all tests in the directory.
   - Example output:
     ```
     ============================= test session starts ==============================
     platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
     collected 2 items

     test_example.py ..                                                   [100%]

     ============================== 2 passed in 0.01s ===============================
     ```
2. **Run a Specific Test File**:
   - To run tests in a specific file, use the command `pytest test_example.py`.
   - Example output:
     ```
     ============================= test session starts ==============================
     platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
     collected 2 items

     test_example.py ..                                                   [100%]

     ============================== 2 passed in 0.01s ===============================
     ```

### Understanding Test Results
**Description**: Pytest provides detailed output for test results, including which tests passed or failed and any error messages. Understanding this output is crucial for debugging and improving your tests.

**Lab Activity**:
1. **Run the Test and Observe the Output**:
   - Run the command `pytest test_example.py`.
   - Observe the output in the terminal. You should see a summary indicating that the tests passed.
2. **Introduce a Failure**:
   - Modify the test function in `test_example.py` to:
     ```python
     def test_addition():
         assert 1 + 1 == 3
     ```
   - Run the test again using `pytest test_example.py`.
   - Observe the output. Pytest will indicate that the test failed and provide details about the failure.
   - Example output:
     ```
     ============================= test session starts ==============================
     platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
     collected 2 items

     test_example.py F.                                                   [100%]

     =================================== FAILURES ===================================
     _______________________________ test_addition _________________________________
     test_example.py:2: in test_addition
         assert 1 + 1 == 3
     E       assert (1 + 1) == 3
     E        +  where 2 = (1 + 1)

     ========================== short test summary info ============================
     FAILED test_example.py::test_addition - assert (1 + 1) == 3
     ============================== 1 failed, 1 passed in 0.01s =====================
     ```

These activities will help you get started with writing and running tests using Pytest, as well as understanding the test results. If you need further assistance or additional sections, feel free to ask!
