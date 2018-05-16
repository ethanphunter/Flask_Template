from .Library import Library
from .Models import Book
from typing import List

class InMemoryLibrary(Library):
    """ An implementation of Library that stores the collection in memory """
    def __init__(self):
        super(InMemoryLibrary, self).__init__()
        self.books: List[Book] = []

    def addBook(self, book: Book) -> bool:
        x = lambda bookOne, bookTwo: bookOne.bookId == bookTwo.bookId
        y = lambda bookOne: x(bookOne, book)
        if (len(list(filter(y, self.books))) == 0):
            self.books.append(book)
            return True
        else:
            return False

    def searchByTitle(self, title: str) -> List[Book]:
        pass

    def deleteBook(self, bookId) -> bool:
        bookToRemove = Book(None, None, bookId)
        if (bookToRemove in self.books):
            self.books.remove(bookToRemove)
            return True
        else:
            return False

    def getAllBooks(self) -> List[Book]:
        return self.books
