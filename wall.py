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
        """Initialize the wall object
        :param size: The size of the wall.
        :param direction: The direction of the wall.
        :param mid_pos: The position of the middle of the wall.
        :param color: The color of the wall."""
        self.size = size
        self.color = color
        self.__direction = direction
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
    
    def get_middle_position(self) -> tuple[int, int]:
        """Return the middle position of the wall."""
        return self.positions[len(self.positions) // 2]

    def get_color(self) -> str:
        """Return the color of the wall."""
        return self.color
    
    def move(self):
        """Move the wall one step in the current direction."""
        if self.positions == []:
            return

        self.positions.pop()
        self.positions.insert(
            0,
            tuple(
                self.positions[0][i] + MOVMENT_VECTOR[self.__direction][i]
                for i in range(BOARD_DIM)
            ),
        )


class WallsHandler:
    WALL_SIZE = 3

    def __init__(self, number_of_walls: int = 0) -> None:
        """Initialize the walls handler."""
        self.__walls = []
        self.__num_walls = number_of_walls
    
    def add_wall(self)-> tuple[int, int]:
        """
        Adds a wall to the game.
        :return: the coordinates of the wall
        """
        if len(self.__walls) == self.__num_walls:
            return None
        
        from game_utils import get_random_wall_data

        (x, y, direction) = get_random_wall_data()            

        wall_positions = [wall.get_positions()[1] for wall in self.__walls]
        if (x, y) in wall_positions:
            return None
        
        self.__walls.append(Wall(self.WALL_SIZE, direction, (x, y), "black"))
        return (x, y)

    def remove_wall(self, x: int, y: int) -> None:
        """Removes a wall from the game."""
        for wall in self.__walls:
            if wall.get_positions()[-1] == (x, y):
                self.__walls.remove(wall)
                break
    
    def get_walls(self) -> list[Wall]:
        """Return a list of all the walls in the game."""
        # wall_positions = [wall.get_positions()[1] for wall in self.__walls]
        return self.__walls

        
        