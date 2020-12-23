from snakesandladder.models.player import Player
from snakesandladder.services.playerServiceInterface import PlayerServiceInterface

class PlayerService(PlayerServiceInterface):

    player_details = {}

    def addPlayer(self, id, name):
        self.player = Player()
        self.player.setId(id)
        self.player.setName(name)
        PlayerService.player_details[id] = self.player
        return self.player