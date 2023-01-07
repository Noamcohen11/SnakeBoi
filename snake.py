##############################################################################
#                                   Imports                                  #
##############################################################################

from typing import Optional
from directions_consts import *

##############################################################################
#                                   Functions                                #
##############################################################################


class Snake:
    """
    A class representing a snake that can move around the screen.
    """

    def __init__(
        self, size: int, direction: str, head_pos: tuple[int, int], color: str
    ) -> None:
        """Initialize the snake object
        :param size: The size of the snake.
        :param color: The color of the snake.
        :param direction: The direction of the snake.
        :param head_pos: The position of the head of the snake."""
        self.size = size
        self.color = color
        # Check if direction is valid
        if direction not in MOVEMENT_DIRECTIONS:
            raise ValueError(
                "Invalid direction {} for snake.".format(direction)
            )
        else:
            self.direction = direction

        # Add entire snake to positions.
        self.positions = []
        for block in range(size):
            self.positions.append(
                tuple(
                    head_pos[i] - MOVMENT_VECTOR[direction][i] * block
                    for i in range(BOARD_DIM)
                )
            )

    def move(self) -> None:
        """Move the snake one step in the current direction."""
        if self.positions == []:
            return

        self.positions.pop()
        self.positions.insert(
            0,
            tuple(
                self.positions[0][i] + MOVMENT_VECTOR[self.direction][i]
                for i in range(BOARD_DIM)
            ),
        )

    def change_direction(self, direction: str) -> bool:
        """Change the direction of the snake
        :param direction: The new direction of the snake.
        :return: True if the direction was changed, False otherwise."""
        if (
            self.direction in HORIZONTAL_DIRECTIONS
            and direction in VERTICAL_DIRECTIONS
        ) or (
            self.direction in VERTICAL_DIRECTIONS
            and direction in HORIZONTAL_DIRECTIONS
        ):
            self.direction = direction
            return True
        return False

    def get_head_pos(self) -> tuple[int, int]:
        """Get the position of the head of the snake.
        :return: The position of the head of the snake."""
        if self.positions != []:
            return self.positions[0]
        return None

    def get_snake_pos(self) -> list[tuple[int, int]]:
        """Get the position of the snake.
        :return: The position of the snake."""
        return self.positions

    def get_color(self) -> str:
        """Get the color of the snake.
        :return: The color of the snake."""
        return self.color
