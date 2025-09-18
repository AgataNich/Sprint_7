class DataForOrder:
    order_data = {
        "firstName": "Ola",
        "LastName": "Lola",
        "address": "Vatutina, 17",
        "metroStation": 4,
        "phone": "+78001231213",
        "rentTime": 5,
        "deliveryDate": "2025-10-01",
        "comment": "Bla-bla-bla"
    }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message':'Этот логин уже используется. Попробуйте другой.'}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code' : 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'



class NegativeCourierData:
    BAD_DATA_LIST = [
        {'firstName': 'Saske', 'password': '12345'},
        {'firstName': 'Saske', 'login': 'saske123'}
    ]

