FROM mcr.microsoft.com/playwright/python:v1.30.0-focal

WORKDIR /app

COPY test_in_sync.py /app/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --upgrade pip
RUN pip install playwright
RUN pip install pytest-playwright
RUN playwright install

RUN pytest test_in_sync.py