# Automated CI Pipeline with GitHub Actions

## Overview

Built an automated Continuous Integration (CI) pipeline using GitHub Actions to run code quality checks and unit tests whenever changes are pushed to the repository or a pull request is opened against the main branch.

## Technologies Used

- GitHub Actions
- Python 3.12
- Pytest
- Ruff

## Project Structure

```text
Assignment-01-CI/
├── app/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   └── test_calculator.py
└── requirements-dev.txt
```

The workflow configuration is located at `.github/workflows/ci.yml` in the repository root.

## Pipeline Workflow

The GitHub Actions workflow performs the following steps:

1. Triggers automatically on pushes and pull requests targeting the main branch.
2. Checks out the repository.
3. Sets up Python 3.12.
4. Installs the required dependencies.
5. Runs Ruff to identify code quality issues.
6. Runs Pytest to execute automated unit tests.

## Testing

Two unit tests were implemented to verify the calculator application's addition and subtraction functions.

The pipeline was successfully executed through GitHub Actions, with both linting and unit testing passing.

## Key Learning Outcomes

- Configuring automated CI workflows using GitHub Actions.
- Understanding workflow triggers and job execution.
- Integrating automated linting and unit testing.
- Using GitHub Actions to validate code changes before merging.
- Troubleshooting workflow configuration and test failures.