import pytest

from methods.auth_methods import AuthMethods
from methods.order_methods import OrderMethods
from preconditions.user_precondition import data_user, data_authorization_user

@pytest.fixture()
def create_user():
    auth_methods = AuthMethods()
    login_data = data_user()
    auth_methods.register_user(login_data)
    response = auth_methods.authorization_user(data_authorization_user(login_data))
    access_token = {"Authorization": response.json()["accessToken"]}
    yield login_data, access_token
    auth_methods.delete_user(access_token)

@pytest.fixture
def get_ingredients():
    order_methods = OrderMethods()
    status_code, ingredients_response = order_methods.create_ingredients(params={})
    ingredients = ingredients_response["data"]
    return ingredients
