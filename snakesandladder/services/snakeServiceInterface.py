import abc


class SnakeServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addSnake(self, id, head, tail):
        pass