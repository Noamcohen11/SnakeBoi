##############################################################################
#                                   Imports                                  #
##############################################################################

from typing import Optional
from game_display import GameDisplay
from snake import Snake
from movemenet_consts import *

##############################################################################
#                                   Constants                                #
##############################################################################

SNAKE_COLOR = "black"
SNAKE_INIT_SIZE = 3
SNAKE_INIT_DIRECTION = "Up"

##############################################################################
#                                   Functions                                #
##############################################################################


class SnakeGame:
    def __init__(self) -> None:
        self.__snake = Snake(
            SNAKE_INIT_SIZE,
            SNAKE_INIT_DIRECTION,
            (5, 5),
        )
        self.__key_clicked = None

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked
        self.__snake.change_direction(self.__key_clicked)

    def update_objects(self) -> None:
        self.__snake.move()

    def draw_board(self, gd: GameDisplay) -> None:
        for pos in self.__snake.get_snake_pos():
            print(pos)
            snake_x, snake_y = pos
            gd.draw_cell(snake_x, snake_y, SNAKE_COLOR)

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False
