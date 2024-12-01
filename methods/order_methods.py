import allure
import requests

from data import BASE_URL, ORDERS_URL, INGREDIENTS_URL


class OrderMethods:

    @allure.step('Создать заказ')
    def create_order(self, params, headers=None):
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=params, headers=headers)
        return response.status_code, response.json()

    @allure.step('Получить данные заказа')
    def get_order(self, headers=None):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}", headers=headers)
        return response.status_code, response.json()

    @allure.step('Получить данные об ингридиентах')
    def create_ingredients(self, params):
        response = requests.get(f"{BASE_URL}{INGREDIENTS_URL}", json=params)
        return response.status_code, response.json()
