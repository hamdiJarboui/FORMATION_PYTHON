# Course Plan for Pytest Using Python

## 9. Plugins and Extensions

### Introduction to Plugins
**Description**: Plugins in Pytest are add-ons that extend its functionality. They allow you to customize and enhance Pytest to suit your specific testing needs. Plugins can add new features, modify existing behaviors, and integrate with other tools and services. Pytest has a rich ecosystem of plugins, both built-in and third-party, that can help you with various aspects of testing.

**Lab Activity**:
1. **Explore Built-in Plugins**:
   - Pytest comes with several built-in plugins that provide core functionality. You can list all active plugins by running the command:
     ```sh
     pytest --trace-config
     ```
   - This command will show all the plugins currently active in your Pytest environment.

2. **Install a Third-Party Plugin**:
   - Install a popular third-party plugin using pip. For example, to install `pytest-cov` for coverage reporting, run:
     ```sh
     pip install pytest-cov
     ```
   - Verify the installation by running:
     ```sh
     pytest --cov
     ```

### Popular Plugins
**Description**: There are many useful plugins available for Pytest that can help you with different aspects of testing. Here are some popular ones:

- **pytest-cov**: Provides coverage reporting, showing which lines of code have been tested and which have not.
- **pytest-xdist**: Allows you to run tests in parallel across multiple CPUs or machines, speeding up the test execution.
- **pytest-django**: Integrates Pytest with Django, making it easier to write tests for Django applications.
- **pytest-bdd**: Supports behavior-driven development (BDD) by allowing you to write tests in a natural language style.
- **pytest-mock**: Provides a simple interface for mocking objects in your tests.
- **pytest-html**: Generates HTML reports for your test results.
- **pytest-rerunfailures**: Automatically re-runs failed tests a specified number of times.

**Lab Activity**:
1. **Install and Use `pytest-cov`**:
   - Install the plugin:
     ```sh
     pip install pytest-cov
     ```
   - Add the following code to a test file to use coverage reporting:
     ```python
     def test_example():
         assert 1 + 1 == 2
     ```
   - Run the tests with coverage reporting:
     ```sh
     pytest --cov=.
     ```

2. **Install and Use `pytest-xdist`**:
   - Install the plugin:
     ```sh
     pip install pytest-xdist
     ```
   - Run tests in parallel using the `-n` option:
     ```sh
     pytest -n 4
     ```

3. **Install and Use `pytest-html`**:
   - Install the plugin:
     ```sh
     pip install pytest-html
     ```
   - Generate an HTML report for your test results:
     ```sh
     pytest --html=report.html
     ```

### Writing Custom Plugins
**Description**: Writing custom plugins allows you to extend Pytest's functionality to meet your specific needs. Custom plugins can add new hooks, modify existing behaviors, and integrate with other tools. Pytest provides a flexible plugin architecture that makes it easy to create and distribute your own plugins.

**Lab Activity**:
1. **Create a Simple Plugin**:
   - Create a new file named `myplugin.py`.
   - Add the following code to define a simple plugin that adds a custom marker:
     ```python
     import pytest

     def pytest_configure(config):
         config.addinivalue_line("markers", "custom: Custom marker for demonstration")

     @pytest.mark.custom
     def test_custom_marker():
         assert 1 + 1 == 2
     ```

2. **Use the Custom Plugin**:
   - Create a `pytest.ini` file in your project directory and add the following content to register the custom plugin:
     ```ini
     [pytest]
     addopts = -p myplugin
     ```
   - Run the tests to see the custom marker in action:
     ```sh
     pytest
     ```

3. **Implement a Hook Function**:
   - Modify `myplugin.py` to implement a hook function that prints a message before each test:
     ```python
     def pytest_runtest_setup(item):
         print(f"Setting up {item.name}")
     ```

4. **Distribute the Plugin**:
   - Package your plugin for distribution by creating a `setup.py` file:
     ```python
     from setuptools import setup

     setup(
         name="myplugin",
         version="0.1",
         py_modules=["myplugin"],
         entry_points={"pytest11": ["myplugin = myplugin"]},
     )
     ```
   - Install the plugin locally:
     ```sh
     pip install -e .
     ```

These activities will help you understand what plugins are, how to use popular plugins, and how to create and distribute your own custom plugins in Pytest. If you need further assistance or additional sections, feel free to ask!
