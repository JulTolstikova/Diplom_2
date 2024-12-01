import allure
import pytest

from methods.auth_methods import AuthMethods
from preconditions.user_precondition import data_user, data_authorization_user


class TestAuthСhangeUser:
    @allure.title('Успешное изменение пользователя')
    def test_change_user_successful(self, create_user):
        auth_methods = AuthMethods()
        login_data, access_token = create_user
        new_data_user = data_user()
        response = auth_methods.change_user(headers=access_token, params=new_data_user)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Неуспешное изменение неавторизованного пользователя')
    def test_change_user_unauthorized(self, create_user):
        auth_methods = AuthMethods()
        _, access_token = create_user
        new_data_user = data_user()
        response = auth_methods.change_user(headers=None, params=new_data_user)
        assert response.status_code == 401 and response.json() == {"success": False,
                                                                   "message": "You should be authorised"
                                                                   }
