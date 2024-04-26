import requests
import json
import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext
from search_api import save_multiple_keys


def test_apis_get():
    ## This script in fetching the Dirk offer API and saves it in the dirk_offer_list.txt file
    url = "https://www.dirk.nl/api/offers/1"

    headers = {
        }

    response = requests.get(url, headers=headers)
    res = response.json()
    # print(json.dumps(res, indent=4))

    # List of keys to save
    keys_to_save = ["headerText", "normalPrice", "offerPrice", "packaging"]

    # Call the function to save the specified keys
    save_multiple_keys(res, keys_to_save)

  



