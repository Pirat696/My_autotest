import requests

from used_data.api.api_url import GET_USER_INFO_URL
from used_data.models.user_data import Model


def test_get_user_info(get_bearer_token):
    response = requests.get(url=GET_USER_INFO_URL, headers=get_bearer_token)
    assert response.status_code == 200
    Model.parse_raw(response.text)
