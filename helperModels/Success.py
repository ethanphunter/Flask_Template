from .Attempt import Attempt

class Success(Attempt):
    """docstring for Success."""

    def __init__(self, value):
        super(Success, self).__init__()
        self.value = value

    def getOrElse(self, elseValue):
        return self.value

    def get(self):
        return self.value

    def isFailure(self):
        return False
