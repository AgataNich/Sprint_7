## Финальный проект 7 спринта
<hr>

## Студент: Агата Ничипорчик

## <h>Когорта: #28</h>
<hr>

## <h>Project: Яндекс.Самокат</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла         | Содержание файла                  |
|------------------------|-----------------------------------|
| Tests dir              | Директория с тестами              |
| test_create_courier.py | Проверка создания новоого курьера |
| test_get_order_list.py | Проверка получения списка заказов |
| test_login_courier.py  | Проверка авторизации курьера      |
| test_make_order.py     | Проверка оформления заказа        |
| conftest.py            | Фикстуры                          |
| data.py                | Данные для входа, регистрации     |
| urls.py                | Url и API ручки                   |
| requirements.txt       | Файл с зависимостями              |
| allure_results.dir     | Папка с отчетами Allure           |
| README.md              | Документация                      |
