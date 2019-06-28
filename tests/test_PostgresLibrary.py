import pytest
from blueprints.jsonApiBlueprint.library.Models import Book

def book():
    return Book(
        title = "The Best Book, The Sequel",
	    authorId = 1,
	    bookId = 1235)

def test_addBook(postgresLibrary):
    assert postgresLibrary.addBook(book())
    assert not postgresLibrary.addBook(book())

def test_getAllBooks(postgresLibrary):
    books = postgresLibrary.getAllBooks()
    assert book() in books

def test_deleteBook(postgresLibrary):
    assert postgresLibrary.deleteBook(book().bookId)
    assert not postgresLibrary.deleteBook(book().bookId)

def test_getAllBooksRemoved(postgresLibrary):
    books = postgresLibrary.getAllBooks()
    assert not book() in books
