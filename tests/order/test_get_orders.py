import allure

from methods.order_methods import OrderMethods


class TestGetOrders:

    @allure.title('Успешное получение данных заказа с авторизацией')
    def test_get_order_auth_successful(self, create_user):
        order_methods = OrderMethods()
        _, access_token = create_user
        status_code, order_response = order_methods.get_order(headers=access_token)
        assert status_code == 200 and order_response["success"] is True

    @allure.title('Получение данных заказа без авторизации')
    def test_get_order_without_auth(self, create_user):
        order_methods = OrderMethods()
        status_code, order_response = order_methods.get_order()
        assert status_code == 401 and order_response == {'success': False,
                                                         'message': 'You should be authorised'}
