##############################################################################
#                                   Imports                                  #
##############################################################################

from typing import Optional
from game_display import GameDisplay
from snake import Snake
from movemenet_consts import *

##############################################################################
#                                   Functions                                #
##############################################################################


class SnakeGame:
    def __init__(self, width: int, height: int, snake) -> None:
        """
        Initialize the snake game object.
        :param width: The width of the game board.
        :param height: The height of the game board.
        """
        self.height = height
        self.width = width
        self.__snake = snake
        self.__key_clicked = None

    def read_key(self, key_clicked: Optional[str]) -> None:
        """Read the key that was clicked and change the direction of the snake.
        :param key_clicked: The key that was clicked."""
        self.__key_clicked = key_clicked
        self.__snake.change_direction(self.__key_clicked)

    def update_objects(self) -> None:
        """Update the snake in the game."""
        self.__snake.move()

    def draw_board(self, gd: GameDisplay) -> None:
        """Draw the snake on the game board.
        :param gd: The game display object."""
        for pos in self.__snake.get_snake_pos():
            x, y = pos
            if x > 0 and x < self.width and y > 0 and y < self.height:
                gd.draw_cell(x, y, SNAKE_COLOR)

        if len(self.__apples_handler.get_apples()) > 0:
            for apple in self.__apples_handler.get_apples():
                gd.draw_cell(apple.get_x(), apple.get_y(), "green")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        """Check if the game is over.
        meaning the snake is out of bounds or eating itself.
        :return: True if the game is over, False otherwise."""

        # Check if snake is out of bounds
        for pos in self.__snake.get_snake_pos():
            if (
                pos[0] < 0
                or pos[0] >= self.width
                or pos[1] < 0
                or pos[1] >= self.height
            ):
                return True

        # Check if snake is eating itself
        set_snake_pos = set(self.__snake.get_snake_pos())
        if len(set_snake_pos) != len(self.__snake.get_snake_pos()):
            return True

        """Check if the game is over.
        meaning the snake is out of bounds or eating itself.
        :return: True if the game is over, False otherwise."""

        # Check if snake is out of bounds
        pos = self.__snake.get_head_pos()
        # If the snake is in length 0, it is not out of bounds.
        if pos is None:
            return False

        if (
            pos[0] < 0
            or pos[0] >= self.width
            or pos[1] < 0
            or pos[1] >= self.height
        ):
            return True

        # Check if snake is eating itself
        set_snake_pos = set(self.__snake.get_snake_pos())
        if len(set_snake_pos) != len(self.__snake.get_snake_pos()):
            return True

        return False
