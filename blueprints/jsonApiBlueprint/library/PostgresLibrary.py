from helperModels.Attempt import Attempt
from helperModels.Success import Success
from helperModels.Failure import Failure
from postgres.Postgres import Postgres
from .Library import Library
from .Models import Book
from typing import List

class PostgresLibrary(Postgres):
    """ An implementation of Library that stores the collection in postgres """
    def __init__(self, url):
        super(PostgresLibrary, self).__init__(url)
        self.db_url = url

    def _bookExists(self, bookId) -> Attempt:
        maybeBookCount = self.getQuery("""select count(*) from Books where id = %s""", (bookId,))
        if ( not maybeBookCount.isFailure() ):
            bookCount = maybeBookCount.get()
            if (bookCount[0][0] == 1):
                return Success(True)
            else:
                return Failure("Book does not exist")
        else:
            return maybeBookCount

    def _tupleListToBookList(self, l):
        accum = []
        for b in l:
            accum.append(Book( bookId = b[0], title =  b[1], authorId = b[2]))
        return accum

    def addBook(self, book: Book) -> bool:
        maybeBookCount = self.getQuery("""select count(*) from Books where id = %s""", (book.bookId,))
        if (not maybeBookCount.isFailure()):
            bookCount = maybeBookCount.get()
            if (bookCount[0][0] == 0):
                w = self.writeQuery("""insert into Books values (%s, %s, %s)""", (book.bookId, book.title, book.authorId))
                return not w.isFailure()
            else:
                return False
        else:
            return False

    def searchByTitle(self, title: str) -> List[Book]:
        pass

    def deleteBook(self, bookId) -> bool:
        be = self._bookExists(bookId)
        if ( not be.isFailure() and be.get() == True ):
            deleteBook = self.writeQuery("""delete from Books where id = %s""", (bookId, ))
            return not deleteBook.isFailure()
        else:
            return False

    def getAllBooks(self) -> List[Book]:
        maybeBooks = self.getQuery("""select * from Books""", None)
        if ( not maybeBooks.isFailure() ):
            return self._tupleListToBookList(maybeBooks.get())
        else:
            print("Failure to get all Books")
            return []
