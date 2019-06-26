import pytest
import Boot
from config.Config import Config

@pytest.fixture( scope = "module" )
def client():
    Boot.app.config['TESTING'] = True
    client = Boot.app.test_client()

    yield client

@pytest.fixture( scope = "module" )
def config():
    yield Config()
