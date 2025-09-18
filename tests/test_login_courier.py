import pytest
import requests
import allure
import generators
from data import ResponseBody
from urls import Url


@allure.epic('Login courier API. Handle: /api/v1/courier/login')
class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_successful_courier_login(self, create_courier):
        with allure.step('Формирование данных для логина'):
            login_data = {'login': create_courier['login'], 'password': create_courier['password']}

        with allure.step('Отправка POST запроса на авторизацию курьера'):
            resp = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data)

        with allure.step('Проверка кода ответа'):
            assert resp.status_code == 200

        with allure.step('Проверка, что в ответе присутствует id'):
            assert 'id' in resp.json() and resp.json()['id'] != ''

    @allure.title('Авторизация несуществующего курьера')
    def test_unregistered_courier_login(self):
        with allure.step('Генерация случайного логина и пароля'):
            login_data = {'login': generators.login_generator(), 'password': generators.password_generator()}

        with allure.step('Отправка POST запроса на авторизацию несуществующего курьера'):
            resp = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_data)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert resp.status_code == 404
            assert resp.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND

    @allure.title('Ошибка при пустом пароле')
    def test_courier_login_empty_password_error(self, create_courier):
        with allure.step('Формирование данных с пустым паролем'):
            data_response = {'login': create_courier['login'], 'password': ''}

        with allure.step('Отправка POST запроса'):
            resp = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=data_response)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert resp.status_code == 400
            assert resp.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA

    @allure.title('Ошибка при пустом логине')
    def test_courier_login_empty_login_error(self, create_courier):
        with allure.step('Формирование данных с пустым логином'):
            data_response = {'login': '', 'password': create_courier['password']}

        with allure.step('Отправка POST запроса'):
            resp = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=data_response)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert resp.status_code == 400
            assert resp.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA

    @allure.title('Ошибка при неверном пароле')
    def test_wrong_password_error(self, create_courier):
        with allure.step('Формирование данных с неверным паролем'):
            wrong_password = {'login': create_courier['login'], 'password': 'wrong123'}

        with allure.step('Отправка POST запроса'):
            resp = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=wrong_password)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert resp.status_code == 404
            assert resp.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND
