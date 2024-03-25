# 🎭 [Playwright](https://playwright.dev) for Python [![PyPI version](https://badge.fury.io/py/playwright.svg)](https://pypi.python.org/pypi/playwright/)

# [![My Playwright Tests](https://github.com/MishaFrancis/Playwright/actions/workflows/playwright.yml/badge.svg?branch=main)](https://github.com/MishaFrancis/Playwright/actions/workflows/playwright.yml)

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

## Run Pytest:
pytest --headed

## Run specific tests:
pytest test_login.py

## Run specific tests with html reports:
pytest test_login.py --html=reports.html