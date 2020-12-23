import abc


class BoardServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setPlayersCurrentPosition(self, playersPos):
        pass

    @abc.abstractmethod
    def addSnakes(self, snakes):
        pass

    @abc.abstractmethod
    def addLadders(self, ladders):
        pass





