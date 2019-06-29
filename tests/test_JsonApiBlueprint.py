from flask import json
import pytest

def test_add_book_route(client):
    """Test the /add_book endpoint"""

    r = client.post(
        '/api/add_book',
        data = json.dumps({ 'title': 'The Best Book, The Sequel', 'authorId': 1, 'bookId': 1235 }),
        content_type = 'application/json')
    assert r.status_code == 204

def test_all_books_route(client):
    """Test the /all_books endpoint"""

    r = client.get('/api/all_books')
    assert r.status_code == 200
    assert b'The Best Book, The Sequel' in r.data

def test_delete_book(client):
    """Test the /delete_book endpoint"""

    r = client.delete(
        '/api/delete_book',
        data = json.dumps({'bookId': 1235}),
        content_type = 'application/json')

    assert r.status_code == 204
