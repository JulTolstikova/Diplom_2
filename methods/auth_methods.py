import allure
import requests

from data import BASE_URL, AUTH_URL


class AuthMethods:

    @allure.step('Cоздать пользователя')
    def register_user(self, params):
        response = requests.post(f"{BASE_URL}{AUTH_URL}register", json=params)
        return response.status_code, response.json()

    @allure.step('Авторизовать пользователя')
    def authorization_user(self, params):
        response = requests.post(f"{BASE_URL}{AUTH_URL}login", json=params)
        return response

    @allure.step('Изменить пользователя')
    def change_user(self, headers, params):
        response = requests.patch(f"{BASE_URL}{AUTH_URL}user", headers=headers, json=params)
        return response

    @allure.step('Удалить пользователя')
    def delete_user(self, headers):
        response = requests.delete(f"{BASE_URL}{AUTH_URL}user", headers=headers)
        return response
