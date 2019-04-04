import pytest

def test_empty_db(client):
    """Test the /ping endpoint."""

    r = client.get('/default/ping')
    assert b'pong' in r.data
