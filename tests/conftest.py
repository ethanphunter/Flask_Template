import pytest
import Boot

@pytest.fixture(scope="module")
def client():
    Boot.app.config['TESTING'] = True
    client = Boot.app.test_client()

    yield client
