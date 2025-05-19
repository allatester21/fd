import requests


def test_find_rest(api_url, rest_name):
    headers = {
        'Content-Type': "application/json"
    }

    body = {
        "text": rest_name,
        "filters": [],
        "location": {
            "longitude": 37.742438184543616,
            "latitude": 55.712111901220766
        }
    }

    response = requests.post(api_url + '/eats/v1/full-text-search/v1/search', headers=headers, json=body)
    cafe = response.json()['blocks'][0]['payload'][0]['title']

    return (cafe, response)


def get_menu(api_url, slug):
    headers = {
        'Content-Type': "application/json"
    }

    param = {
        "longitude": 37.742438184543616,
        "latitude": 55.712111901220766
    }

    response = requests.get(api_url + '/api/v2/menu/retrieve/' + slug, headers=headers, params=param)
    menu = response.json()['payload']['categories']

    return (menu, response)


def add_dish(api_url, item_id):
    body = {
        "item_id": item_id,
        "quantity": 2,
        "place_slug": "foodband_xfuie",
        "place_business": "restaurant",
        "item_options": []
    }

    param = {
        "longitude": 37.742438184543616,
        "latitude": 55.712111901220766,
        "screen": "menu",
        "shippingType": "delivery",

    }
    headers = {
        'Content-Type': "application/json"
    }

    response = requests.post(api_url + '/api/v1/cart', params=param, headers=headers, json=body)
    try:
        checkaut = int(response.json()['cart']['items'][0]['quantity'])
        id_prod = response.json()['id']
        id_basket = response.json()['cart']['id']
    except:
        checkaut = None
        id_prod = None
        id_basket = None

    return (checkaut, id_basket, id_prod, response)
