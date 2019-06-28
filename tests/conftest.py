import pytest
import Boot
from config.Config import Config
from blueprints.jsonApiBlueprint.library.PostgresLibrary import PostgresLibrary

@pytest.fixture( scope = "module" )
def client():
    Boot.app.config['TESTING'] = True
    client = Boot.app.test_client()
    yield client

@pytest.fixture( scope = "module" )
def config():
    yield Config()

@pytest.fixture( scope = "module" )
def postgresLibrary(config):
    yield PostgresLibrary(config.db_url)
