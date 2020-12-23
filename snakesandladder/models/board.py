class Board:

    def __init__(self):
        # self.size = None
        self.size = 100
        self.snakes = list()
        self.ladders = list()
        self.playersPos = dict()

    def getSnakes(self):
        return self.snakes

    def setSnakes(self, snakes):
        self.snakes = snakes

    def getLadders(self):
        return self.ladders

    def setLadders(self, ladders):
        self.ladder = ladders

    def getSize(self):
        return self.size

    def setSize(self, val):
        self.size = val

    def setPlayersCurrentPosition(self, playersPos):
        self.playersPos = playersPos

    def getPlayersCurrentPosition(self):
        return self.playersPos