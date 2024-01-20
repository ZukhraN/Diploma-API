import json
import logging
import allure
import requests
from allure_commons.types import AttachmentType

def create_pet():
    headers = {'Content-Type': 'application/json'}
    body = {
            "id": 125,
            "category": {
                "id": 125,
                "name": "dog"
            },
            "name": "Pluto1",
            "photoUrls": [
                "https://images.app.goo.gl/PmXpnRsuY6L8XdBd9"
            ],
            "tags": [
                {
                    "id": 125,
                    "name": "dog"
                }
            ],
            "status": "available"
    }
    result = requests.post('https://petstore.swagger.io/v2/pet', json=body, headers=headers)
    result_id = result.json()['id']
    return result_id


def get_request_with_json_response(url, **kwargs):
    result = requests.get(url='https://petstore.swagger.io' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response body",
                  attachment_type=AttachmentType.JSON, extension="json")
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result


def get_request_without_json_response(url, **kwargs):
    result = requests.get(url='https://petstore.swagger.io' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result


def delete_request(url, **kwargs):
    result = requests.delete(url='https://petstore.swagger.io' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result


def post_request(url, **kwargs):
    result = requests.post(url='https://petstore.swagger.io' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.body, name="Request body", attachment_type=AttachmentType.JSON,
                  extension="json")
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response body",
                  attachment_type=AttachmentType.JSON, extension="json")
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result

'''
def put_request(url, **kwargs):
    result = requests.put(url='https://petstore.swagger.io' + url, **kwargs)
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.body, name="Request body", attachment_type=AttachmentType.JSON,
                  extension="json")
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True), name="Response body",
                  attachment_type=AttachmentType.JSON, extension="json")
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)
    return result'''
