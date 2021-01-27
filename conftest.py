import pytest
from app import index

@pytest.fixture
def homepage():
    homepage = index()
    yield homepage

@pytest.fixture
def client(homepage):
    return homepage.test_client()
