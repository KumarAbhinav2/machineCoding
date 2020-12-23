import abc

class DiceServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def roll(self):
        pass