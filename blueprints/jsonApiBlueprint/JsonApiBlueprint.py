from ..Responses import *
from .library.InMemoryLibrary import InMemoryLibrary
from .library.JsonEncoder import LibraryJsonEncoder
from .library.Models import Book
from .library.PostgresLibrary import PostgresLibrary

from flask import Blueprint, request, jsonify

class JsonApiBlueprint(object):
    def __init__(self, db_url):
        super(JsonApiBlueprint, self).__init__()
        self.library = PostgresLibrary(db_url) #InMemoryLibrary()
        jsonApiBlueprint = Blueprint("Json_Api_Blueprint", __name__)

        @jsonApiBlueprint.route("/all_books")
        def allBooks():
            books = self.library.getAllBooks()
            return jsonify( books = books)

        @jsonApiBlueprint.route("/add_book", methods = ["POST"])
        def add():
            try:
                jsonData = request.get_json()
                title = jsonData['title']
                authorId = int(jsonData['authorId'])
                bookId = int(jsonData['bookId'])
                book = Book(title, authorId, bookId)
                added = self.library.addBook(book)
                if (added):
                    return NoContent()
                else:
                    return BadRequest()
            except:
                return BadRequest()

        @jsonApiBlueprint.route("/delete_book", methods = ["DELETE"])
        def delete():
            try:
                jsonData = request.get_json()
                bookId = jsonData["bookId"]
                deleted = self.library.deleteBook(bookId)
                if (deleted):
                    return NoContent()
                else:
                    return BadRequest()
            except:
                return BadRequest()

        @jsonApiBlueprint.route("/search_by_title", methods = ["POST"])
        def searchByTitle():
            return NotImplemented()

        self.jsonApiBlueprint = jsonApiBlueprint
        self.jsonApiBlueprint.json_encoder = LibraryJsonEncoder
