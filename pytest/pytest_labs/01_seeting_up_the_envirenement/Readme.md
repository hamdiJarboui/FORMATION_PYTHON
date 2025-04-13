

## 2. Setting Up the Environment

### Installing Python
**Description**: Ensure Python is installed on your system. Python can be downloaded from the official Python website. Follow the instructions for your operating system to install Python.

**Lab Activity**:
1. **Download and Install Python**: Visit the Python downloads page and download the latest version of Python. Follow the installation instructions for your operating system.
2. **Verify Installation**: Open a terminal or command prompt and run the command `python --version` to verify that Python is installed correctly.

### Setting Up a Virtual Environment
**Description**: A virtual environment is an isolated environment that allows you to manage dependencies for your Python projects without affecting other projects. This is useful for maintaining different versions of packages for different projects.

**Lab Activity**:
1. **Create a Virtual Environment**:
   - Open a terminal or command prompt.
   - Navigate to your project directory.
   - Run the command `python -m venv venv` to create a virtual environment named `venv`.
2. **Activate the Virtual Environment**:
   - On Windows: Run `venv\Scripts\activate`.
   - On macOS and Linux: Run `source venv/bin/activate`.
3. **Verify Activation**: The command prompt should change to indicate that the virtual environment is active. Run `pip list` to see the installed packages (it should be a minimal list).

### Installing Pytest
**Description**: Pytest is a popular testing framework for Python. It can be easily installed using pip, Python's package installer.

**Lab Activity**:
1. **Install Pytest**: With the virtual environment activated, run the command `pip install pytest` to install Pytest.
2. **Verify Installation**: Run `pytest --version` to verify that Pytest is installed correctly.
3. **Create a Simple Test**:
   - Create a new file named `test_sample.py`.
   - Add the following code to the file:
     ```python
     def test_example():
         assert 1 + 1 == 2
     ```
   - Run the test using the command `pytest test_sample.py`.

These activities will help you set up your Python environment, create and activate a virtual environment, and install Pytest. If you need further assistance or additional sections, feel free to ask!
