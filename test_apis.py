import requests
import json
import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
    ) -> Generator[APIRequestContext, None, None]:
    headers = {
        # We set this header per GitHub guidelines.
        # Add authorization token to all requests.
        # Assuming personal access token available in the environment.
    }
    request_context = playwright.request.new_context(
    )
    yield request_context
    request_context.dispose()


def test_apis_get():
    url = "https://api.restful-api.dev/objects"

    headers = {
        }

    response = requests.get(url, headers=headers)

    print(response.json())

def test_apis_post():
    url = 'https://www.w3schools.com/python/demopage.php'

    myobj = {
            "name": "Apple MacBook Pro 16",
            "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                     }
            }

    x = requests.post(url, json = myobj)
    print(x.status_code)


def test_api_get_post(api_request_context: APIRequestContext) -> None:
    url = 'https://www.w3schools.com/python/demopage.php'
    print(url)
    data = {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
           }
    new_issue = api_request_context.post(url, data=data)
    assert new_issue.ok
    print(new_issue.status)

    issues = api_request_context.get(url)
    assert issues.ok

    print(issues.status_text)