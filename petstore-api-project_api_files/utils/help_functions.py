import logging
import allure
import requests
from allure_commons.types import AttachmentType

def create_pet(default_url):
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
    result = requests.post(default_url +'/v2/pet', json=body, headers=headers)
    result_id = result.json()['id']
    return result_id

def attach_and_loging(result):
    allure.attach(body=result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
    allure.attach(body=result.request.method, name="Request method", attachment_type=AttachmentType.TEXT)
    allure.attach(body=str(result.status_code), name="Response status code", attachment_type=AttachmentType.TEXT,
                  extension='txt')
    logging.info("Request: " + result.request.url)
    logging.info("Response code " + str(result.status_code))
    logging.info("Response: " + result.text)


def get_request_with_json_response(url, default_url, **kwargs):
    result = requests.get(url=default_url + url, **kwargs)
    attach_and_loging(result)
    return result


def get_request_without_json_response(url, default_url, **kwargs):
    result = requests.get(url=default_url + url, **kwargs)
    attach_and_loging(result)
    return result


def delete_request(url, default_url, **kwargs):
    result = requests.delete(url=default_url + url, **kwargs)
    attach_and_loging(result)
    return result


def post_request(url, default_url, **kwargs):
    result = requests.post(url=default_url + url, **kwargs)
    attach_and_loging(result)
    return result
