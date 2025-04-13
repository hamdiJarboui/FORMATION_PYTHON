Continuous Integration with Pytest
# 11. Continuous Integration
## Integrating with CI/CD

Setting up Pytest with CI tools like Jenkins, GitHub Actions, and GitLab CI involves the following steps:

    Install Pytest:

    pip install pytest

    Configure CI Tool:
        GitHub Actions: Create a workflow file (.github/workflows/pytest.yml).
        GitLab CI: Create a GitLab CI configuration file (.gitlab-ci.yml).
        Jenkins: Add a pipeline script to run Pytest.

### Example GitHub Actions Workflow

name: Python package

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
    - name: Run tests
      run: |
        pytest

### Example GitLab CI Configuration

stages:
  - test

pytest:
  stage: test
  image: python:3.8
  before_script:
    - pip install pytest
  script:
    - pytest

Example Jenkins Pipeline

pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install pytest'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}

###  Automating Test Runs

Best practices for automated testing in CI pipelines include:

    Run tests on every commit: Ensure that tests are run on every push or pull request.
    Use virtual environments: Isolate dependencies using virtual environments.
    Parallel testing: Speed up test runs by running tests in parallel.
    Test coverage: Measure and report test coverage.

###  Pytest Options

Here are some commonly used Pytest command-line options:

    -s: Disable output capturing (show print statements).
    -k EXPRESSION: Only run tests that match the given expression.
    -m MARKEXPR: Only run tests matching the given mark expression.
    -v: Increase verbosity.
    --maxfail=NUM: Stop after the first NUM failures.
    --tb=style: Set traceback print mode (auto/long/short/line/native/no).
    --durations=NUM: Show slowest NUM test durations.
    --junitxml=path: Create a JUnit XML-style report file at the given path.
    --cov=MODULE: Measure code coverage for the specified module.

Example usage:

pytest -v -s --maxfail=2 --tb=short --durations=10

For more detailed information on Pytest options, refer to the Pytest documentation.