import pytest
import allure
import requests
from data import Url, Flags

@allure.epic('Order list API. Handle: /api/v1/orders')
class TestGetOrderList:

    @allure.title('Успешный возврат списка заказов')
    def test_success_get_order_list(self):
        with allure.step('Отправка GET запроса на получение списка заказов'):
            resp = requests.get(f'{Url.BASE_URL}{Url.GET_ORDER_LIST}')
            data = resp.json()

        with allure.step('Проверка кода ответа'):
            assert resp.status_code == 200

        with allure.step(f'Проверка наличия ключа {Flags.SUCCESSFUL_GET_ORDER_LIST} в ответе'):
            assert Flags.SUCCESSFUL_GET_ORDER_LIST in data

        with allure.step(f'Проверка, что {Flags.SUCCESSFUL_GET_ORDER_LIST} является списком'):
            assert isinstance(data[Flags.SUCCESSFUL_GET_ORDER_LIST], list)

        with allure.step(f'Проверка, что список {Flags.SUCCESSFUL_GET_ORDER_LIST} не пустой'):
            assert len(data[Flags.SUCCESSFUL_GET_ORDER_LIST]) > 0
