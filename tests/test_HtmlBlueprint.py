import pytest
from flask import json

def test_index(client):
    """Test the /index endpoint"""

    r = client.get(
        '/index')
    assert r.status_code == 200
    assert b'Hello There!' in r.data

def test_param(client):
    """Test the /param endpoint"""

    r = client.get('/param?p=hi')
    assert r.status_code == 200
    assert b'hi' in r.data
