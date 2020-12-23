class GameController:
    def __init__(self, boardService, diceService, playerService):
        self.boardService = boardService
        self.diceService = diceService

    def addSnakes(self, snakes):
        self.boardService.addSnakes(snakes)

    def addPlayers(self, players):
        self.playersQueue = []
        self.initialNumberOfPlayers = len(players)
        playerPositions =  {}
        for player in players:
            self.playersQueue.append(player)
            playerPositions[player.getId()] = 0
        self.boardService.setPlayersCurrentPosition(playerPositions)

    def addLadders(self, ladders):
        self.boardService.addLadders(ladders)

    def isGameOver(self):
        # Winner will be removed from player queue after winning
        return self.initialNumberOfPlayers > len(self.playersQueue)

    def movePlayer(self, player, diceVal):
        oldPos = self.boardService.getPlayersCurrentPosition()[player.getId()]
        newPos = oldPos+diceVal
        print(f"Moving {player.getName()} from {oldPos} to {newPos}")
        boardSize = self.boardService.getSize()
        if newPos > boardSize:
            newPos = oldPos
        else:
            newPos = self.getNewPositionAfterDiceRoll(player, newPos)

        self.boardService.getPlayersCurrentPosition()[player.getId()] = newPos

    def weHaveTheWinner(self, player):
        return self.boardService.getPlayersCurrentPosition()[player.getId()] == self.boardService.getSize()

    def getNewPositionAfterDiceRoll(self, player, pos):
        while True:
            for ladder in self.boardService.getLadders():
                if ladder.getStart() == pos:
                    print(f"Hurray.....There is a ladder at {pos} for {player.getName()}")
                    pos = ladder.getEnd()
                    print(f"{player.getName()} moved to {pos}...... :)")
                    continue

            for snake in self.boardService.getSnakes():
                if snake.getHead() == pos:
                    print(f"Awwwwww {player.getName()} you got a snake bite..... :(" )
                    pos = snake.getTail()
                    print(f"{player.getName()} goes down to {pos}......")
                    continue
            break
        return pos

    def startGame(self):
        print("The Game is about to Begin........")
        while not self.isGameOver():
            print("Initializing the Players....")
            player = self.playersQueue.pop(0)
            print(f"{player.getName()}....is rolling the dice")
            diceVal = self.diceService.roll()
            print(f"....Its {diceVal}....for {player.getName()}")
            self.movePlayer(player, diceVal)
            if self.weHaveTheWinner(player):
                print(f"Hurray......{player.getName()} ..is the WINNERRRRRRR..... : )")
                del self.boardService.getPlayersCurrentPosition()[player.getId()]
            else:
                print(f"Its the turn of the next player....")
                self.playersQueue.append(player)




