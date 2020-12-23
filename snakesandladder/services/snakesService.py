from snakesandladder.models.snake import Snake
from snakesandladder.services.snakeServiceInterface import SnakeServiceInterface

class SnakeService(SnakeServiceInterface):

    # since we are not storing anything in DB , will keep everything in hashmap
    snakes_details = {}

    def addSnake(self, id, head, tail):
        self.snake = Snake()
        self.snake.setId(id)
        self.snake.setHead(head)
        self.snake.setTail(tail)
        SnakeService.snakes_details[id] = self.snake
        return self.snake