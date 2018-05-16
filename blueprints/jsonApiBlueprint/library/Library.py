from .Models import Book
from abc import ABC, abstractmethod
from typing import List

class Library(ABC):
    """ A abstract class for a Library """
    def __init__(self):
        super(Library, self).__init__()

    @abstractmethod
    def addBook(self, book: Book) -> bool:
        pass

    @abstractmethod
    def searchByTitle(self, title: str) -> List[Book]:
        pass

    @abstractmethod
    def deleteBook(self, bookId) -> bool:
        pass

    @abstractmethod
    def getAllBooks(self) -> List[Book]:
        pass
