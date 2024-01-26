import allure
import jsonschema
from allure_commons.types import Severity
from petstore_api_project_api_files.utils.load_schema import load_schema
from petstore_api_project_api_files.utils.help_functions import post_request, get_request_with_json_response, \
    delete_request, create_pet


@allure.tag("petstore-api-project_tests")
@allure.severity(Severity.NORMAL)
@allure.feature("Create pet")
def test_create_pet(default_url):
    schema = load_schema('create_pet.json')
    headers = {'Content-Type': 'application/json'}
    body = {
        "id": 95,
        "category": {
            "id": 95,
            "name": "dog"
        },
        "name": "Pluto1",
        "photoUrls": [
            "https://images.app.goo.gl/PmXpnRsuY6L8XdBd9"
        ],
        "tags": [
            {
                "id": 95,
                "name": "dog"
            }
        ],
        "status": "available"
    }
    with allure.step('Отправить POST запрос на эндпоинт "/v2/pet"'):
        result = post_request('/v2/pet', default_url, json=body, headers=headers)
    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)
    with allure.step(f'Проверить, что значение параметра id в ответе равно 95'):
        assert result.json()['id'] == 95


@allure.tag("petstore-api-project_tests")
@allure.severity(Severity.NORMAL)
@allure.feature("Get pet by status = available")
def test_get_pet_by_status_available(default_url):
    schema = load_schema('get_status_pet.json')
    with allure.step('Отправить GET запрос на эндпоинт "/v2/pet/findByStatus"'):
        result = get_request_with_json_response('/v2/pet/findByStatus' + '?status=available', default_url)

    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200

    with allure.step('Проверить, что питомцы со статусом available'):
        assert isinstance(result.json(), list)
        pets = result.json()
        assert any(pet.get('status') == 'available' for pet in pets)
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)


@allure.tag("petstore-api-project_tests")
@allure.severity(Severity.NORMAL)
@allure.feature("Get pet by status = pending")
def test_get_pet_by_status_pending(default_url):
    schema = load_schema('get_status_pet.json')
    with allure.step('Отправить GET запрос на эндпоинт "/v2/pet/findByStatus"'):
        result = get_request_with_json_response('/v2/pet/findByStatus' + '?status=pending', default_url)

    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200

    with allure.step('Проверить, что питомцы со статусом pending'):
        assert isinstance(result.json(), list)
        pets = result.json()
        assert any(pet.get('status') == 'pending' for pet in pets)
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)


@allure.tag("petstore-api-project_tests")
@allure.severity(Severity.NORMAL)
@allure.feature("Get pet by status = sold")
def test_get_pet_by_status_sold(default_url):
    schema = load_schema('get_status_pet.json')
    with allure.step('Отправить GET запрос на эндпоинт "/v2/pet/findByStatus"'):
        result = get_request_with_json_response('/v2/pet/findByStatus' + '?status=sold', default_url)

    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200

    with allure.step('Проверить, что питомцы со статусом sold'):
        assert isinstance(result.json(), list)
        pets = result.json()
        assert any(pet.get('status') == 'sold' for pet in pets)
    with allure.step('Проверить json схему ответа'):
        jsonschema.validate(result.json(), schema)


@allure.tag("petstore-api-project_tests")
@allure.severity(Severity.NORMAL)
@allure.feature("Delete pet by id")
def test_delete_pet(default_url):
    pet_id = create_pet(default_url)
    with allure.step(f'Отправить DELETE запрос на эндпоинт "/v2/pet/{pet_id}"'):
        result = delete_request(f'/v2/pet/{pet_id}', default_url)
    with allure.step('Проверить, что статус код равен 200'):
        assert result.status_code == 200
