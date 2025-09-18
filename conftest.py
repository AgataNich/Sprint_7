import pytest
import requests
import generators
from urls import Url


@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_body = {'login': login, 'password': password, 'firstName': name}

    # Создание курьера
    resp_create = requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER}', json=create_body)
    assert resp_create.status_code == 201, f"Ошибка создания курьера: {resp_create.text}"

    # Авторизация для получения id
    login_body = {'login': login, 'password': password}
    resp_login = requests.post(f'{Url.BASE_URL}{Url.COURIER_LOGIN}', json=login_body)
    assert resp_login.status_code == 200, f"Ошибка логина курьера: {resp_login.text}"
    courier_id = resp_login.json().get('id')

    yield {
        'login': login,
        'password': password,
        'firstName': name,
        'id': courier_id
    }

    if courier_id:
        requests.delete(f'{Url.BASE_URL}{Url.COURIER_DELETE}{courier_id}')

@pytest.fixture
def generate_courier_data():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    return {
        'create_body': {'login': login, 'password': password, 'firstName': name},
        'login_body': {'login': login, 'password': password}
    }

@pytest.fixture
def cancel_order():
    tracks = []

    def _register(track_number):
        tracks.append(track_number)

    yield _register

    for track in tracks:
        requests.put(f'{Url.BASE_URL}{Url.ORDER_CANCEL}{track}')