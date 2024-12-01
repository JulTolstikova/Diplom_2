import allure
import pytest

from conftest import create_user
from methods.auth_methods import AuthMethods
from preconditions.user_precondition import data_authorization_user


class TestAuthorizationUser:

    @allure.title('Успешная авторизация пользователя')
    def test_authorization_user_successful(self, create_user):
        auth_methods = AuthMethods()
        login_data, _ = create_user
        auth_data = data_authorization_user(login_data)
        response = auth_methods.authorization_user(auth_data)
        assert response.status_code == 200 and response.json()["success"] is True

    @pytest.mark.parametrize("invalid_email", ["", "validation_failed@test.ru", "invalid_email"])
    @allure.title('Неуспешая авторизация с невалидной почтой')
    def test_authorization_user_invalid_email(self, create_user, invalid_email):
        auth_methods = AuthMethods()
        login_data, _ = create_user
        login_data["email"] = invalid_email
        response = auth_methods.authorization_user(data_authorization_user(login_data))
        assert response.status_code == 401 and response.json() == {'success': False,
                                                                   'message': 'email or password are incorrect'}

    @pytest.mark.parametrize("invalid_password", ["", "123"])
    @allure.title('Неуспешная авторизация с невалидным паролем')
    def test_authorization_user_invalid_password(self, create_user, invalid_password):
        auth_methods = AuthMethods()
        login_data, _ = create_user
        login_data["password"] = invalid_password
        response = auth_methods.authorization_user(data_authorization_user(login_data))
        assert response.status_code == 401 and response.json() == {'success': False,
                                                                   'message': 'email or password are incorrect'}
