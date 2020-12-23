import abc


class LadderServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addLadder(self, id, start, end):
        pass