from models.board import Board
from models.snake import Snake
from snakesandladder.services.boardServiceInterface import BoardServiceInterface

class BoardService(BoardServiceInterface):

    board_status = {}

    def __init__(self):
        self.board = Board()

    def addSnakes(self, snakes):
        self.board.setSnakes(snakes)

    def getSnakes(self):
        return self.board.getSnakes()

    def addLadders(self, ladders):
        self.board.setLadders(ladders)

    def getLadders(self):
        return self.board.getLadders()

    def setPlayersCurrentPosition(self, playersPos):
        self.board.setPlayersCurrentPosition(playersPos)

    def getPlayersCurrentPosition(self):
        return self.board.getPlayersCurrentPosition()

    def getSize(self):
        return self.board.getSize()


