from .Models import Book
from flask.json import JSONEncoder

class LibraryJsonEncoder(JSONEncoder):
    """docstring for LibraryJsonEncoder."""
    def default(self, obj):
        if (isinstance(obj, Book)):
            return obj.__dict__
        else:
            return super(LibraryJsonEncoder, self).default(obj)
