import pytest

def test_ping_route(client):
    """Test the /ping endpoint."""

    r = client.get('/default/ping')
    assert b'pong' in r.data
