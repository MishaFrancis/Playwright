import requests
import json


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