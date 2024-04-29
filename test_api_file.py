import random
import requests
import Helpers


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
    Helpers.save_multiple_keys(res, keys_to_save)


def test_functions():
    a = Helpers.calcs(5.5)
    print(a)

