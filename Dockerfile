FROM mcr.microsoft.com/playwright/python:v1.30.0-focal

WORKDIR /app

COPY test_example.py /app/

RUN pip install --no-cache-dir --upgrade pip