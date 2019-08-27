from ..Responses import *
from .library.InMemoryLibrary import InMemoryLibrary
from .library.JsonEncoder import LibraryJsonEncoder
from .library.Models import Book
from .library.PostgresLibrary import PostgresLibrary
from helperModels.Success import Success
from helperModels.Failure import Failure
from helperModels.Attempt import Attempt

from flask import Blueprint, request, jsonify

class JsonApiBlueprint(object):
    def __init__(self, db_url):
        super(JsonApiBlueprint, self).__init__()
        self.library = PostgresLibrary(db_url) #InMemoryLibrary()
        jsonApiBlueprint = Blueprint("Json_Api_Blueprint", __name__)

        def _dbReady():
            return isinstance(self.library.ready, Success)

        @jsonApiBlueprint.route("/all_books")
        def allBooks():
            if ( _dbReady() ):
                books = self.library.getAllBooks()
                return jsonify( books = books)
            else:
                return BadGateway()

        @jsonApiBlueprint.route("/add_book", methods = ["POST"])
        def add():
            try:
                jsonData = request.get_json()
                title = jsonData['title']
                authorId = int(jsonData['authorId'])
                bookId = int(jsonData['bookId'])
                book = Book(title, authorId, bookId)
            except:
                return BadRequest()

            if ( _dbReady() ):
                added = self.library.addBook(book)
                if (added):
                    return NoContent()
                else:
                    return BadRequest()
            else:
                return BadGateway()

        @jsonApiBlueprint.route("/delete_book", methods = ["DELETE"])
        def delete():
            try:
                jsonData = request.get_json()
                bookId = jsonData["bookId"]
            except Exception as e:
                return BadRequest()

            if ( _dbReady() ):
                deleted = self.library.deleteBook(bookId)
                if (deleted):
                    return NoContent()
                else:
                    return BadRequest()
            else:
                return BadGateway()

        @jsonApiBlueprint.route("/search_by_title", methods = ["POST"])
        def searchByTitle():
            return NotImplemented()

        self.jsonApiBlueprint = jsonApiBlueprint
        self.jsonApiBlueprint.json_encoder = LibraryJsonEncoder
