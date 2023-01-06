

class Apple:
    """A class that represents an apple in the game"""
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        self.__color = "green"
    
    def get_x(self) -> int:
        """Returns the x coordinate of the apple"""
        return self.__x
    def get_y(self) -> int:
        """Returns the y coordinate of the apple"""
        return self.__y


class ApplesHandler:
    """A class that handles the apples in the game"""

    def __init__(self, number_of_apples = 0):
        self.__apples = []
        self.__num_apples = number_of_apples
    
    def add_apple(self) -> tuple(int, int):
        """
        Adds an apple to the game.
        :return: the coordinates of the apple
        """
        if len(self.__apples) == self.__num_apples:
            return None

        from game_utils import get_random_apple_data

        x, y = get_random_apple_data()
        self.__apples.append(Apple(x, y))
        return (x, y)

    def remove_apple(self, x: int, y: int) -> None:
        """
        Removes an apple from the game.
        :param x: the x coordinate of the apple
        :param y: the y coordinate of the apple
        :return: None
        """
        for apple in self.__apples:
            if apple.get_x() == x and apple.get_y() == y:
                self.__apples.remove(apple)
                break

    def get_apples(self) -> list:
        """Returns the list of apples"""
        return self.__apples.copy()