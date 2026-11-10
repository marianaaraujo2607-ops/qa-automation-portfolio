# QA Automation Portfolio

Automated API test suite in Python, running on every push with GitHub Actions.

## Goal
Demonstrate test automation practices: API testing with pytest, clean project structure, and continuous integration.

## Tech Stack
- Python 3
- pytest
- requests
- GitHub Actions (coming soon)

## Getting Started
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest

## Project Structure
- tests/ : test cases
- api/ : API clients and helpers
- utils/ : shared utilities