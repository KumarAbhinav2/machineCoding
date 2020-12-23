import abc
class PlayerServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addPlayer(self, id, name):
        pass