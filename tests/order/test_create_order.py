import allure

from data import FAKE_INGRIDIENT
from methods.order_methods import OrderMethods


class TestCreateOrders:

    @allure.title('Успешное создание заказа без авторизации')
    def test_create_order_successful(self, get_ingredients):
        order_methods = OrderMethods()
        ingredients = get_ingredients
        ingredient_ids = [ingredient["_id"] for ingredient in ingredients[:3]]
        order_data = {
            "ingredients": ingredient_ids
        }
        status_code, order_response = order_methods.create_order(params=order_data)
        assert status_code == 200 and order_response["success"] is True

    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_auth_successful(self, create_user, get_ingredients):
        order_methods = OrderMethods()
        _, access_token = create_user
        ingredients = get_ingredients
        ingredient_ids = [ingredient["_id"] for ingredient in ingredients[:3]]
        order_data = {
            "ingredients": ingredient_ids
        }
        headers = access_token
        status_code, order_response = order_methods.create_order(params=order_data, headers=headers)
        assert status_code == 200 and order_response["success"] is True

    @allure.title('Создание заказа без ингридиентов')
    def test_create_order_without_ingridients(self):
        order_methods = OrderMethods()
        order_data = {
            "ingredients": []
        }
        status_code, order_response = order_methods.create_order(params=order_data)
        assert status_code == 400 and order_response == {'success': False,
                                                         'message': 'Ingredient ids must be provided'}

    @allure.title('Создание заказа с несуществующим ингридиентом')
    def test_create_order_fake_ingridients(self):
        order_methods = OrderMethods()
        order_data = {
            "ingredients": [FAKE_INGRIDIENT]
        }
        status_code, order_response = order_methods.create_order(params=order_data)
        assert status_code == 400 and order_response == {'success': False,
                                                         'message': 'One or more ids provided are incorrect'}
