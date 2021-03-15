import pytest
import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True


def test_index(client):
    r = client.get('/')
    assert r == '/'

