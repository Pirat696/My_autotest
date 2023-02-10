import pytest
import requests

from used_data.api.api_urls import LOGIN_URL
from used_data.api.api_urls import POST_CREAT_USER_URL
from used_data.models.created_user import Model
from used_data.post_data.created_user_data import pyload


@pytest.fixture(scope="session")
def get_bearer_token():

    data = {
        "password": "password!",
        "username": "username"
    }

    response = requests.post(url=LOGIN_URL, data=data)
    assert response.status_code == 201
    token_domofon = response.json()["list"][0]["sid"]

    bearer_token = {
        "Content-Type": "application/json",
        'Authorization': "Bearer " + token_domofon
    }
    return bearer_token


@pytest.fixture(scope="module")
def post_creat_user(get_bearer_token):

    response = requests.post(url=POST_CREAT_USER_URL,
                             headers=get_bearer_token, json=pyload)
    assert response.status_code == 201
    Model.parse_raw(response.text)
