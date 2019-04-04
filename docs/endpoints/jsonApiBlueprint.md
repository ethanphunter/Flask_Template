# Endpoint documentation for JsonApiBlueprint

This blueprint provides a library to store books.


### GET /all_books
No parameters

This endpoint returns all books in the library

### POST /add_book
jsonBody:
```
{
	"title": "The Best Book, The Sequel",
	"authorId": 1,
	"bookId": 1235
}
```

This endpoint adds a book provided in the request body to the library

Responses
 - 204 NoContent - Book successfully added
 - 400 BadRequest - Book was not added OR the body of the request was invalid

### POST /delete_book
jsonBody:
```
{
	"bookId": 1235
}
```

Deletes a book by the given bookId from the library

Responses
 - 204 NoContent - Successfully removed the book from the library
 - 400 BadRequest - Book was not deleted OR the body of the request was invalid

### POST /search_by_title
NotImplemented

Searches the library for a book with the given title

Responses
 - 501 - Not Implemented
