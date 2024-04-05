# 🎭 [Playwright](https://playwright.dev) for Python [![PyPI version](https://badge.fury.io/py/playwright.svg)](https://pypi.python.org/pypi/playwright/)

# [![Multi-OS Platform Tests](https://github.com/MishaFrancis/Playwright/actions/workflows/gh_action_multi_os.yml/badge.svg)](https://github.com/MishaFrancis/Playwright/actions/workflows/gh_action_multi_os.yml)

[![Playwright Smoke Tests](https://github.com/MishaFrancis/Playwright/actions/workflows/playwright_smoke.yml/badge.svg)](https://github.com/MishaFrancis/Playwright/actions/workflows/playwright_smoke.yml)

# Playwright - Introduction to install

## Installing Python (Along with Python, 'pip' is also installed which helps to install other supporting packages while working with Python/Playwright)
Windows : https://www.python.org/downloads/windows/

MAC : https://www.python.org/downloads/macos/

## Installing Pytest:
pip install pytest

## Installing Playwright Pytest plugin:
pip install pytest-playwright

## Installing required browsers (Chromium,Firefox,...):
playwright install

## To update Playwright to the latest version:
pip install pytest-playwright playwright -U

# Playwright - How to run tests

## To run the dependencies mentioned in requirements.txt
pip install -r requirements.txt

## Run Pytest:
pytest --headed

## Run specific tests:
pytest test_login.py

## Run specific tests with html reports:
pytest test_login.py --html=reports.html

## Run specific tests which are marked with tags & with html reports:
pytest -m smoke --html=reports.html

## Run tests in parallel
pytest test_example.py -v --html=reports.html --disable-warnings --numprocesses 6