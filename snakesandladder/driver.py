from snakesandladder.services.snakesService import SnakeService
from snakesandladder.services.ladderService import LadderService
from snakesandladder.services.playerService import PlayerService
from snakesandladder.services.boardService import BoardService
from snakesandladder.services.diceService import DiceService
from snakesandladder.controllers.gameController import GameController
import uuid

s = SnakeService()
snakes = []
snakes.append(s.addSnake(uuid.uuid1(), 11, 2))
snakes.append(s.addSnake(uuid.uuid1(), 29, 10))
snakes.append(s.addSnake(uuid.uuid1(), 57, 38))
snakes.append(s.addSnake(uuid.uuid1(), 78, 50))
snakes.append(s.addSnake(uuid.uuid1(), 40, 13))
snakes.append(s.addSnake(uuid.uuid1(), 99, 21))


l = LadderService()
ladders = []
ladders.append(l.addLadder(uuid.uuid1(), 9, 29))
ladders.append(l.addLadder(uuid.uuid1(), 22, 42))
ladders.append(l.addLadder(uuid.uuid1(), 65, 88))
ladders.append(l.addLadder(uuid.uuid1(), 39, 51))
ladders.append(l.addLadder(uuid.uuid1(), 80, 95))

p = PlayerService()
players = []
players.append(p.addPlayer(uuid.uuid1(), 'Abhi'))
players.append(p.addPlayer(uuid.uuid1(), 'Divyank'))
players.append(p.addPlayer(uuid.uuid1(), 'Gyan'))
players.append(p.addPlayer(uuid.uuid1(), 'Pawan'))

d = DiceService()
g = BoardService()
gc = GameController(g, d, p)

gc.addSnakes(snakes)
gc.addLadders(ladders)
gc.addPlayers(players)
gc.startGame()
