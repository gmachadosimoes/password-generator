import app
import pytest
import requests


url = 'https://pwdg.herokuapp.com/'
response = requests.get(url)


@pytest.mark.app
def test_http_response():
    assert response.status_code == 200


@pytest.mark.app
def test_error_handling():
    if response.status_code != 200:
        assert Exception
