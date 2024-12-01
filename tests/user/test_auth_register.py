import allure
import pytest

from data import delete_field
from methods.auth_methods import AuthMethods
from preconditions.user_precondition import data_user


class TestAuthRegister:
    @allure.title('Успешное создание пользователя')
    def test_create_user_successful(self):
        auth_methods = AuthMethods()
        status_code, current_response = auth_methods.register_user(data_user())
        assert status_code == 200 and current_response["success"] is True

    @allure.title('Создание двух одинаковых пользователей')
    def test_create_user_duplicate(self):
        auth_methods = AuthMethods()
        first_user = data_user()
        auth_methods.register_user(first_user)
        status_code, current_response = auth_methods.register_user(first_user)
        assert status_code == 403 and current_response == {'success': False,
                                                           'message': 'User already exists'}

    @pytest.mark.parametrize("deleted_field", ["name", "email", "password"])
    @allure.title('Создание пользователя без обязательного поля')
    def test_create_user_without_field(self, deleted_field):
        auth_methods = AuthMethods()
        request_without_field = delete_field(data_user(), deleted_field)
        status_code, current_response = auth_methods.register_user(request_without_field)
        assert status_code == 403 and current_response == {'success': False,
                                                           'message': 'Email, password and name are required fields'}
