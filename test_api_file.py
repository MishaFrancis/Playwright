import requests
import json
import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext
from search_api import search_multiple_values


def test_apis_get():
    url = "https://www.dirk.nl/api/offers/1"

    headers = {
        }

    response = requests.get(url, headers=headers)
    res = response.json()
    # print(json.dumps(res, indent=4))

    keys_to_search = ['productId', 'offerPrice','normalPrice']
    found_values = search_multiple_values(res, keys_to_search)

    # Output the found values
    for key, value in found_values.items():
        print(f"Key: {key}, Value: {value}")
