from helperModels.Failure import Failure
from helperModels.Success import Success

from abc import ABC
import psycopg2

class Postgres(ABC):
    """docstring for Postgres."""

    def __init__(self, url, test = False):
        super(Postgres, self).__init__()
        self._parseUrl(url)
        if (not test):
            self.connection = psycopg2.connect(
                database = self.database,
                user = self.username,
                password = self.password,
                host = self.host,
                port = self.port)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

    def _parseUrl(self, url: str) -> None:
        y = url.split("@")
        self.username, self.password = y[0].split("://")[-1].split(":")
        self.host = y[-1].split(":")[0]
        self.port = int(y[-1].split("/")[0].split(":")[-1])
        self.database = y[-1].split("/")[-1]

    def getQuery(self, queryString, parameters):
        try:
            self.cursor.execute(queryString, parameters)
            rows = self.cursor.fetchall()
            result = Success(rows)
            return result
        except Exception as e:
            print("Error executing get query: " + str(e))
            return Failure("Error executing get query")

    def writeQuery(self, queryString, parameters):
        try:
            x = self.cursor.execute(queryString, parameters)
            return Success("Write Query Successful")
        except Exception as e:
            print("Error executing write query: " + str(e))
            return Failure("Error executing write query")
