from typing import Optional

##############################################################################
#                                   Constants                                #
##############################################################################

HORIZONTAL_DIRECTIONS = {"Left", "Right"}
VERTICAL_DIRECTIONS = {"Up", "Down"}
MOVEMENT_DIRECTIONS = HORIZONTAL_DIRECTIONS | VERTICAL_DIRECTIONS
MOVMENT_VECTOR = {
    "Up": (0, 1),
    "Down": (0, -1),
    "Left": (-1, 0),
    "Right": (1, 0),
}

##############################################################################
#                                   Functions                                #
##############################################################################


class Snake:
    """
    A class representing a snake that can move around the screen.
    """

    def __init__(
        self, size: int, color: str, direction: str, head_pos: tuple(int, int)
    ) -> None:
        """Initialize the snake object
        :param size: The size of the snake.
        :param color: The color of the snake.
        :param direction: The direction of the snake.
        :param head_pos: The position of the head of the snake."""
        self.color = color
        self.size = size
        # Check if direction is valid
        if direction not in MOVEMENT_DIRECTIONS:
            raise ValueError(
                "Invalid direction {} for snake.".format(direction)
            )
        else:
            self.direction = direction

        # Add entire snake to positions.
        self.positions = []
        for block in size:
            self.positions.append(head_pos - MOVMENT_VECTOR[direction] * block)

    def move(self) -> None:
        """Move the snake one step in the current direction."""
        self.positions.pop()
        self.positions.insert(
            0, self.positions[0] + MOVMENT_VECTOR[self.direction]
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
