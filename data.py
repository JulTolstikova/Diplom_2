import random
import string

BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
AUTH_URL = 'auth/'
ORDERS_URL = 'orders'
INGREDIENTS_URL = 'ingredients'

FAKE_INGRIDIENT = "609646e4dc916e00276b2870"


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def delete_field(payload, field):
    payload.pop(field)
    return payload
