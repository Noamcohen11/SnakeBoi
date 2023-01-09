##############################################################################
#                                   Functions                                #
##############################################################################


class Apple:
    """A class that represents an apple in the game"""

    def __init__(self, x: int, y: int, color: str) -> None:
        self.__x = x
        self.__y = y
        self.__color = color

    def get_x(self) -> int:
        """Returns the x coordinate of the apple"""
        return self.__x

    def get_y(self) -> int:
        """Returns the y coordinate of the apple"""
        return self.__y

    def get_color(self):
        """Returns the color of the apple"""
        return self.__color


class ApplesHandler:
    """A class that handles the apples in the game"""

    def __init__(self, number_of_apples: int = 0, apples_color: str = "green"):
        self.__apples = {}
        self.__num_apples = number_of_apples
        self.__apples_color = apples_color

    def add_apple(self) -> tuple[int, int]:
        """
        Adds an apple to the game.
        :return: the coordinates of the apple
        """
        if len(self.__apples) == self.__num_apples:
            return None
        from game_utils import get_random_apple_data

        apple_coordinates = get_random_apple_data()
        x, y = apple_coordinates[0], apple_coordinates[1]

        if (
            x,
            y,
        ) in self.__apples.keys():
            return None

        self.__apples[(x, y)] = Apple(x, y, self.__apples_color)
        return (x, y)

    def remove_apple(self, x: int, y: int) -> bool:
        """
        Removes an apple from the game.
        :param x: the x coordinate of the apple
        :param y: the y coordinate of the apple
        :return: True if the apple was removed, False otherwise
        """
        try:
            self.__apples.pop((x, y))
            return True
        except KeyError:
            return False

    def get_apples(self) -> list:
        """Returns a list of apples"""
        return self.__apples.values()
