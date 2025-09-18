import pytest
import requests
import allure
from data import ResponseBody, NegativeCourierData
from urls import Url

@allure.epic('Courier API. Handle: /api/v1/courier/')
class TestCreateNewCourier:

    @allure.title('Успешное создание курьера')
    def test_success_creation_courier(self, generate_courier_data):
        with allure.step('Формирование данных для создания курьера'):
            create_data = generate_courier_data['create_body']

        with allure.step('Отправка POST запроса на создание курьера'):
            resp = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=create_data)

        with allure.step('Проверка кода ответа и успешного создания'):
            assert resp.status_code == 201
            assert resp.json() == ResponseBody.COURIER_CREATION_SUCCESS

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_creation_courier_clone_error(self, create_courier):
        with allure.step('Повторная отправка запроса с уже существующими данными курьера'):
            courier_body = {
                'login': create_courier['login'],
                'password': create_courier['password'],
                'firstName': create_courier['firstName']
            }
            resp = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=courier_body)
        with allure.step('Проверка кода и сообщения об ошибке'):
            assert resp.status_code == ResponseBody.COURIER_NAME_ALREADY_EXIST['code']
            assert resp.json()['message'] == ResponseBody.COURIER_NAME_ALREADY_EXIST['message']

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert resp.status_code == ResponseBody.COURIER_NAME_ALREADY_EXIST['code']
            assert resp.json()['message'] == ResponseBody.COURIER_NAME_ALREADY_EXIST['message']

    @allure.title('Создание курьера без логина или пароля — 400')
    @pytest.mark.parametrize('bad_data', NegativeCourierData.BAD_DATA_LIST)
    def test_creation_courier_deficit_data_error(self, bad_data):
        with allure.step('Отправка POST запроса с неполными данными'):
            resp = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=bad_data)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert resp.status_code == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA['code']
            assert resp.json()['message'] == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA['message']
