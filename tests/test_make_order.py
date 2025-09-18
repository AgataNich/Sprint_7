import pytest
import requests
import allure
from data import DataForOrder, Flags
from urls import Url

@allure.epic('Order API. Handle: /api/v1/orders')
class TestMakeOrder:

    @allure.title('Успешное создание заказа с разными вариантами выбора цвета')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_create_order_with_diff_colors(self, scooter_color, cancel_order):
        with allure.step('Подготовка данных заказа'):
            order_data = DataForOrder.order_data.copy()  # копируем, чтобы не мутировать исходные данные
            order_data['color'] = scooter_color

        with allure.step(f'Отправка POST запроса на создание заказа с цветом: {scooter_color}'):
            resp = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', json=order_data)
            data = resp.json()

        with allure.step('Проверка кода ответа'):
            assert resp.status_code == 201

        with allure.step('Проверка, что в ответе есть track номера заказа'):
            assert Flags.SUCCESSFUL_ORDER_CREATION in data
            assert data[Flags.SUCCESSFUL_ORDER_CREATION] is not None

        cancel_order(data[Flags.SUCCESSFUL_ORDER_CREATION])
