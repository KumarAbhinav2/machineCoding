import random
from snakesandladder.services.diceServiceInterface import DiceServiceInterface

class DiceService(DiceServiceInterface):

    def roll(self):
        return random.randint(1, 6)