##############################################################################
#                                   Imports                                  #
##############################################################################

from typing import Optional
from directions_consts import *

##############################################################################
#                                   Functions                                #
##############################################################################


class Wall:
    """
    A class representing a wall that can be drawn on the screen.
    """

    def __init__(
        self, size: int, direction: str, mid_pos: tuple[int, int], color: str
    ) -> None:
        """Initialize the snake object
        :param size: The size of the wall.
        :param direction: The direction of the wall.
        :param mid_pos: The position of the middle of the wall.
        :param color: The color of the wall."""
        self.size = size
        self.color = color
        # Check if direction is valid.
        if direction in VERTICAL_DIRECTIONS:
            pos_f = lambda x, y, i: (x, y - (size - 1) // 2 + i)
        elif direction in HORIZONTAL_DIRECTIONS:
            pos_f = lambda x, y, i: (x - (size - 1) // 2 + i, y)
        else:
            raise ValueError(
                "Invalid direction {} for snake.".format(direction)
            )

        # Add entire wall to positions.
        x, y = mid_pos
        self.positions = []
        for block in range(size):
            self.positions.append(pos_f(x, y, block))

    def get_positions(self) -> list[tuple[int, int]]:
        """Return the positions of the wall."""
        return self.positions

    def get_color(self) -> str:
        """Return the color of the wall."""
        return self.color
