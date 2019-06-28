from postgres.Postgres import Postgres

import pytest

def test_urlParse():
    p = Postgres(url = "postgres://username:password@host:1234/database", test = True)
    assert p.username == "username"
    assert p.password == "password"
    assert p.host == "host"
    assert p.port == 1234
    assert p.database == "database"
