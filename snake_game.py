##############################################################################
#                                   Imports                                  #
##############################################################################

from typing import Optional
from game_display import GameDisplay
from snake import Snake
from directions_consts import *
from apple import ApplesHandler
from wall import WallsHandler

##############################################################################
#                                   Functions                                #
##############################################################################


class SnakeGame:
    def __init__(self, width: int, height: int, snake: Snake, max_apples: int, max_walls: int) -> None:
        """
        Initialize the snake game object.
        :param width: The width of the game board.
        :param height: The height of the game board.
        """
        self.height = height
        self.width = width
        self.__snake = snake
        self.__key_clicked = None
        self.__apples_handler = ApplesHandler(max_apples)
        self.__walls_handler = WallsHandler(max_walls)
        self.__round = 0

    def read_key(self, key_clicked: Optional[str]) -> None:
        """Read the key that was clicked and change the direction of the snake.
        :param key_clicked: The key that was clicked."""
        self.__key_clicked = key_clicked
        self.__snake.change_direction(self.__key_clicked)

    def update_objects(self) -> None:
        """Update the snake in the game."""
        self.__snake.move()
        # Check if snake ate an apple
        (x, y) = self.__snake.get_head_pos()        
        if self.__apples_handler.remove_apple(x, y):
            self.__snake.grow()            
        
        # Check if new apple spawned in snake. If so, remove it.
        snake_coords = self.__snake.get_snake_pos()
        new_apple_pos = self.__apples_handler.add_apple()
        if new_apple_pos in snake_coords:
            self.__apples_handler.remove_apple(new_apple_pos[0], new_apple_pos[1])

        for wall in self.__walls_handler.get_walls():
            if self.__round % 2 == 0:
                wall.move()
            (x, y) = wall.get_positions()[-1]
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                # print("DEBBUG: Removing wall")
                self.__walls_handler.remove_wall(x, y)

        # Spawn a new wall
        
        new_wall_coordinates = self.__walls_handler.add_wall()
        

        self.__round += 1

        

    def draw_board(self, gd: GameDisplay) -> None:
        """Draw the snake on the game board.
        :param gd: The game display object."""
        for pos in self.__snake.get_snake_pos():
            x, y = pos
            if x >= 0 and x < self.width and y >= 0 and y < self.height:
                gd.draw_cell(x, y, self.__snake.get_color())
        
        for apple in self.__apples_handler.get_apples():
            x, y = apple.get_x(), apple.get_y()
            gd.draw_cell(x, y, apple.get_color())
        
        for wall in self.__walls_handler.get_walls():
            for pos in wall.get_positions():
                (x, y) = pos
                if x >= 0 and x < self.width and y >= 0 and y < self.height:
                    gd.draw_cell(x, y, wall.get_color())

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
        
        #  Check of snake is eating a wall or if wall is eating snake
        for wall in self.__walls_handler.get_walls():
            for pos in wall.get_positions():
                if pos == self.__snake.get_head_pos():
                    return True
                if pos in self.__snake.get_snake_pos():
                    self.__snake.cut(pos)

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
