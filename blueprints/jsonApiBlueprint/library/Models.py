from typing import List

class Book(object):
    """ Holds data about a book """

    def __init__(self, title: str, authorId: int, bookId: int):
        super(object, self).__init__()
        self.title = title
        self.authorId = authorId
        self.bookId = bookId

    def __eq__(self, other) -> bool:
        return self.bookId == other.bookId

    def __dict__(self):
        return { 'title': self.title, 'authorId': self.authorId, 'bookId': self.bookId }

    def __str__(self):
        return str(self.title)
