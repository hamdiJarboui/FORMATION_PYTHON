
## 6. Fixtures

### Introduction to Fixtures
**Description**: Fixtures are a powerful feature in Pytest that allow you to set up and tear down resources needed for your tests. They help in creating reusable and maintainable test code by providing a way to define and manage the setup and teardown logic. Fixtures can be used to provide data, initialize objects, or perform any setup required before running tests. They can also be used to clean up after tests, ensuring that the test environment is reset to a known state.

**Lab Activity**:
1. **Basic Fixture Example**:
   - Create a new file named `test_fixtures.py`.
   - Add the following code to define a simple fixture:
     ```python
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
     ```
   - This fixture provides a dictionary with sample data that can be used in the test function. Debug messages are printed to show when the fixture is created and destroyed.

### Creating Fixtures
**Description**: Creating fixtures in Pytest is straightforward. You define a fixture using the `@pytest.fixture` decorator. Fixtures can return any value, which will be passed to the test functions that request them. Fixtures can also request other fixtures, allowing for complex setup dependencies to be managed in a clean and organized manner.

**Lab Activity**:
1. **Create a Fixture for Database Connection**:
   - Add the following code to `test_fixtures.py` to create a fixture for a database connection:
     ```python
     @pytest.fixture
     def db_connection():
         print("\nSetup: Establishing database connection")
         connection = {"host": "localhost", "port": 5432}
         yield connection
         print("\nTeardown: Closing database connection")
         # Teardown code (if any) goes here
         connection.close()

     def test_db_connection(db_connection):
         assert db_connection["host"] == "localhost"
         assert db_connection["port"] == 5432
     ```
   - This fixture sets up a mock database connection and yields it to the test function. Debug messages are printed to show when the fixture is created and destroyed.

### Fixture Scope
**Description**: Fixture scope determines how long a fixture will be active. Pytest supports several scopes: `function`, `class`, `module`, and `session`. The default scope is `function`, meaning the fixture is set up and torn down for each test function. Other scopes allow fixtures to be shared across multiple tests.

- **Function Scope**: The fixture is created and destroyed for each test function. This is the default scope.
- **Class Scope**: The fixture is created once per test class and shared among all test methods in the class.
- **Module Scope**: The fixture is created once per module and shared among all test functions in the module.
- **Session Scope**: The fixture is created once per test session and shared among all test functions in the session.

**Lab Activity**:
1. **Function Scope**:
   - Add the following code to `test_fixtures.py` to demonstrate function scope:
     ```python
     @pytest.fixture(scope="function")
     def function_scope_fixture():
         print("\nSetup: Function scope fixture")
         yield "function scope"
         print("\nTeardown: Function scope fixture")

     def test_function_scope(function_scope_fixture):
         assert function_scope_fixture == "function scope"
     ```
   - This fixture is created and destroyed for each test function. Debug messages are printed to show when the fixture is created and destroyed.

2. **Class Scope**:
   - Add the following code to demonstrate class scope:
     ```python
     @pytest.fixture(scope="class")
     def class_scope_fixture():
         print("\nSetup: Class scope fixture")
         yield "class scope"
         print("\nTeardown: Class scope fixture")

     class TestClassScope:
         def test_class_scope_1(self, class_scope_fixture):
             assert class_scope_fixture == "class scope"

         def test_class_scope_2(self, class_scope_fixture):
             assert class_scope_fixture == "class scope"
     ```
   - This fixture is created once per test class and shared among all test methods in the class. Debug messages are printed to show when the fixture is created and destroyed.

3. **Module Scope**:
   - Add the following code to demonstrate module scope:
     ```python
     @pytest.fixture(scope="module")
     def module_scope_fixture():
         print("\nSetup: Module scope fixture")
         yield "module scope"
         print("\nTeardown: Module scope fixture")

     def test_module_scope_1(module_scope_fixture):
         assert module_scope_fixture == "module scope"

     def test_module_scope_2(module_scope_fixture):
         assert module_scope_fixture == "module scope"
     ```
   - This fixture is created once per module and shared among all test functions in the module. Debug messages are printed to show when the fixture is created and destroyed.

4. **Session Scope**:
   - Add the following code to demonstrate session scope:
     ```python
     @pytest.fixture(scope="session")
     def session_scope_fixture():
         print("\nSetup: Session scope fixture")
         yield "session scope"
         print("\nTeardown: Session scope fixture")

     def test_session_scope_1(session_scope_fixture):
         assert session_scope_fixture == "session scope"

     def test_session_scope_2(session_scope_fixture):
         assert session_scope_fixture == "session scope"
     ```
   - This fixture is created once per test session and shared among all test functions in the session. Debug messages are printed to show when the fixture is created and destroyed.

### Using Fixtures with Dependencies
**Description**: Fixtures can depend on other fixtures, allowing for complex setup scenarios to be managed in a clean and organized manner. This is done by simply including the dependent fixture as an argument in the fixture function.

**Lab Activity**:
1. **Create Dependent Fixtures**:
   - Add the following code to `test_fixtures.py` to create dependent fixtures:
     ```python
     @pytest.fixture
     def first_entry():
         print("\nSetup: First entry fixture")
         yield "a"
         print("\nTeardown: First entry fixture")

     @pytest.fixture
     def order(first_entry):
         print("\nSetup: Order fixture")
         order_list = [first_entry]
         yield order_list
         print("\nTeardown: Order fixture")

     def test_order(order):
         order.append("b")
         assert order == ["a", "b"]
     ```
   - The `order` fixture depends on the `first_entry` fixture. When `order` is requested, Pytest will first execute `first_entry` and pass its result to `order`. Debug messages are printed to show when each fixture is created and destroyed.

These activities will help you understand what fixtures are, how to create and use them, how to manage their scope, and how to handle dependencies between fixtures in Pytest. The debug messages will provide clear visibility into when fixtures are created and destroyed. If you need further assistance or additional sections, feel free to ask!
