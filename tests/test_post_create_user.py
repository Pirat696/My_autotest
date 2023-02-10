import requests

from used_data.api.api_url import POST_CREAT_USER_URL
from used_data.models.created_user import Model
from used_data.post_data.created_user_data import pyload


def test_post_creat_user(get_bearer_token):

    response = requests.post(url=POST_CREAT_USER_URL,
                             headers=get_bearer_token, json=pyload)
    assert response.status_code == 201
    Model.parse_raw(response.text)

    # endpoint = response.json()["list"][0]["id"]
    # delete_url = f"{POST_CREAT_USER_URL}/{endpoint}"
    # response = requests.delete(url=delete_url, headers=get_bearer_token)
    # assert response.status_code == 204
