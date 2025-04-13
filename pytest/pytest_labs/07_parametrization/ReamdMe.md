## 7. Parametrization

### Parametrizing Tests
**Description**: Parametrizing tests allows you to run the same test function with multiple sets of data. This is useful for testing different inputs and outputs without writing separate test functions for each case. Pytest provides the `@pytest.mark.parametrize` decorator to easily define multiple sets of arguments for a test function.

**Lab Activity**:
1. **Basic Parametrization**:
   - Create a new file named `test_parametrization.py`.
   - Add the following code to define a parametrized test:
     ```python
     import pytest

     @pytest.mark.parametrize("input,expected", [
         (1 + 1, 2),
         (2 + 2, 4),
         (3 + 3, 6),
     ])
     def test_addition(input, expected):
         assert input == expected
     ```
   - This test will run three times with different sets of input and expected values.

2. **Run the Parametrized Test**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing your test file.
   - Run the command `pytest` to execute the parametrized test.
   - Example output:
     ```
     ============================= test session starts ==============================
     platform linux -- Python 3.8.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
     collected 3 items

     test_parametrization.py ...                                             [100%]

     ============================== 3 passed in 0.01s ===============================
     ```

### Using pytest.mark.parametrize
**Description**: The `@pytest.mark.parametrize` decorator allows you to define multiple sets of arguments for a test function. You can specify the parameter names and the corresponding values as a list of tuples. This decorator can also be used to parametrize multiple arguments and even fixtures.

**Lab Activity**:
1. **Parametrize Multiple Arguments**:
   - Add the following code to `test_parametrization.py` to parametrize multiple arguments:
     ```python
     @pytest.mark.parametrize("a,b,expected", [
         (1, 2, 3),
         (4, 5, 9),
         (10, 20, 30),
     ])
     def test_addition_multiple_args(a, b, expected):
         assert a + b == expected
     ```
   - This test will run three times with different sets of arguments.

2. **Parametrize with Fixtures**:
   - Add the following code to demonstrate parametrizing with fixtures:
     ```python
     @pytest.fixture
     def sample_data():
         return [1, 2, 3]

     @pytest.mark.parametrize("item", [1, 2, 3])
     def test_sample_data(sample_data, item):
         assert item in sample_data
     ```
   - This test will run three times, each time checking if the item is in the sample data fixture.

3. **Using IDs for Parametrized Tests**:
   - Add the following code to provide custom IDs for parametrized tests:
     ```python
     @pytest.mark.parametrize("a,b,expected", [
         pytest.param(1, 2, 3, id="one_plus_two"),
         pytest.param(4, 5, 9, id="four_plus_five"),
         pytest.param(10, 20, 30, id="ten_plus_twenty"),
     ])
     def test_addition_with_ids(a, b, expected):
         assert a + b == expected
     ```
   - Custom IDs make it easier to identify which test case is running or failing.

### Advanced Parametrization Techniques
**Description**: Pytest allows for advanced parametrization techniques, including generating parameters dynamically, using custom IDs, and combining multiple parameter sets.

**Lab Activity**:
1. **Dynamic Parametrization**:
   - Add the following code to dynamically generate parameters:
     ```python
     def pytest_generate_tests(metafunc):
         if "param" in metafunc.fixturenames:
             metafunc.parametrize("param", range(5))

     def test_dynamic_param(param):
         assert param < 5
     ```
   - This dynamically generates parameters for the test based on the range provided.

2. **Custom ID Function**:
   - Add the following code to use a custom function for generating test IDs:
     ```python
     def idfn(val):
         return f"param_{val}"

     @pytest.mark.parametrize("a,b,expected", [
         (1, 2, 3),
         (4, 5, 9),
         (10, 20, 30),
     ], ids=idfn)
     def test_addition_custom_ids(a, b, expected):
         assert a + b == expected
     ```
   - This uses a custom function to generate IDs for the test cases.

3. **Combining Multiple Parameter Sets**:
   - Add the following code to combine multiple parameter sets:
     ```python
     @pytest.mark.parametrize("a", [1, 2])
     @pytest.mark.parametrize("b", [10, 20])
     def test_combined_params(a, b):
         assert a + b in [11, 21, 12, 22]
     ```
   - This will run the test with all combinations of the parameters `a` and `b`.

### Best Practices for Parametrization
**Description**: When using parametrization, it's important to follow best practices to ensure your tests are maintainable and readable. Use descriptive parameter names, provide custom IDs for clarity, and avoid overly complex parameter sets.

**Lab Activity**:
1. **Descriptive Parameter Names**:
   - Ensure your parameter names are descriptive and meaningful.
   - Example:
     ```python
     @pytest.mark.parametrize("number,expected_square", [
         (2, 4),
         (3, 9),
         (4, 16),
     ])
     def test_square(number, expected_square):
         assert number ** 2 == expected_square
     ```

2. **Using Custom IDs**:
   - Use custom IDs to make test output more readable.
   - Example:
     ```python
     @pytest.mark.parametrize("number,expected_square", [
         pytest.param(2, 4, id="square_of_2"),
         pytest.param(3, 9, id="square_of_3"),
         pytest.param(4, 16, id="square_of_4"),
     ])
     def test_square_with_ids(number, expected_square):
         assert number ** 2 == expected_square
     ```

3. **Avoid Overly Complex Parameter Sets**:
   - Keep parameter sets simple and focused on the specific aspect being tested.
   - Example:
     ```python
     @pytest.mark.parametrize("input,expected", [
         ("3+5", 8),
         ("2+4", 6),
         ("6*9", 54),
     ])
     def test_eval(input, expected):
         assert eval(input) == expected
     ```

These activities will help you understand how to use parametrization in Pytest, including running tests with multiple sets of data, using the `@pytest.mark.parametrize` decorator effectively, and applying advanced techniques. If you need further assistance or additional sections, feel free to ask!
