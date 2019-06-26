import pytest
from blueprints.jsonApiBlueprint.library.PostgresLibrary import PostgresLibrary
from blueprints.jsonApiBlueprint.library.Models import Book

def book():
    return Book(
        title = "The Best Book, The Sequel",
	    authorId = 1,
	    bookId = 1235)

def test_addBook(config):
    pl = PostgresLibrary(config.db_url)
    assert pl.addBook(book())

def test_getAllBooks(config):
    pl = PostgresLibrary(config.db_url)
    books = pl.getAllBooks()
    assert book() in books

def test_deleteBook(config):
    pl = PostgresLibrary(config.db_url)
    assert pl.deleteBook(book().bookId)
