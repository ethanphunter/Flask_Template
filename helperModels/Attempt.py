from abc import ABC, abstractmethod

class Attempt(ABC):
    """ Either a Success or a Failure """

    def __init__(self):
        super(Attempt, self).__init__()

    @abstractmethod
    def getOrElse(self, elseValue):
        pass

    @abstractmethod
    def isFailure(self):
        pass
