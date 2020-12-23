from snakesandladder.models.ladder import Ladder
from snakesandladder.services.ladderServiceInterface import LadderServiceInterface

class LadderService(LadderServiceInterface):

    ladder_details = {}
    def addLadder(self, id, start, end):
        self.ladder = Ladder()
        self.ladder.setId(id)
        self.ladder.setStart(start)
        self.ladder.setEnd(end)
        LadderService.ladder_details[id] = self.ladder
        return self.ladder