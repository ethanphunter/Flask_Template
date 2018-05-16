from .library.InMemoryLibrary import InMemoryLibrary
from .library.JsonEncoder import LibraryJsonEncoder
from .library.Models import Book
from .Responses import *
from flask import Blueprint, request, jsonify

jsonApiBlueprint = Blueprint("Json_Api_Blueprint", __name__)
jsonApiBlueprint.json_encoder = LibraryJsonEncoder

library = InMemoryLibrary()

@jsonApiBlueprint.route("/all_books")
def allBooks():
    books = library.getAllBooks()
    return jsonify({ "books": books })

@jsonApiBlueprint.route("/add_book", methods = ["POST"])
def add():
    try:
        jsonData = request.get_json()
        title = jsonData['title']
        authorId = int(jsonData['authorId'])
        bookId = int(jsonData['bookId'])
        book = Book(title, authorId, bookId)
        added = library.addBook(book)
        if (added):
            return NoContent()
        else:
            return BadRequest()
    except:
        return BadRequest()

@jsonApiBlueprint.route("/delete_book", methods = ["POST"])
def delete():
    try:
        jsonData = request.get_json()
        bookId = jsonData["bookId"]
        deleted = library.deleteBook(bookId)
        if (deleted):
            return NoContent()
        else:
            return BadRequest()
    except:
        return BadRequest()

@jsonApiBlueprint.route("/search_by_title", methods = ["POST"])
def searchByTitle():
    return NotImplemented()
