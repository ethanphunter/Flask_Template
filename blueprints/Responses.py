from flask import Response
from http import HTTPStatus

class NoContent(Response):
    """docstring for NoContent."""
    def __init__(self):
        super(NoContent, self).__init__(
            response = None,
            status = HTTPStatus.NO_CONTENT,
            mimetype = "application/json")

class BadRequest(Response):
    """docstring for BadRequest."""
    def __init__(self):
        super(BadRequest, self).__init__(
            response = None,
            status = HTTPStatus.BAD_REQUEST,
            mimetype = "application/json")

class NotImplemented(Response):
    """docstring for NotImplemented."""
    def __init__(self):
        super(NotImplemented, self).__init__(
            response = None,
            status = HTTPStatus.NOT_IMPLEMENTED,
            mimetype = "application/json")

class BadGateway(Response):
    """docstring for NotImplemented."""
    def __init__(self):
        super(BadGateway, self).__init__(
            response = None,
            status = HTTPStatus.BAD_GATEWAY,
            mimetype = "application/json")
