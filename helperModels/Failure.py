from .Attempt import Attempt

class Failure(Attempt):
    """docstring for Failure."""

    def __init__(self, value):
        super(Failure, self).__init__()
        self.value = value

    def getOrElse(self, elseValue):
        return elseValue

    def isFailure(self):
        return True
