from used_data.api.api_urls import POST_CREAT_USER_URL
import requests


def test_del_user(post_creat_user):
    endpoint = response.json()["list"][0]["id"]
    delete_url = f"{POST_CREAT_USER_URL}/{endpoint}"
    response = requests.delete(url=delete_url, headers=get_bearer_token)
    assert response.status_code == 204
