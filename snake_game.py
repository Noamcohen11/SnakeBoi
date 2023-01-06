from typing import Optional
from game_display import GameDisplay


class SnakeGame:
    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def update_objects(self) -> None:
        if (self.__key_clicked == "Left") and (self.__x > 0):
            self.__x -= 1
        elif (self.__key_clicked == "Right") and (self.__x < 40):
            self.__x += 1

    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False

    ##############################################################################
    #                                  head check                                #
    # MOVMENT_VECTOR = {
    #     "Up": (0, 1),
    #     "Down": (0, -1),
    #     "Left": (-1, 0),
    #     "Right": (1, 0),
    # }
    # Check if head_pos is valid
    # for i in head_pos:
    #     if i + MOVMENT_VECTOR[direction] < 0:
    #         raise ValueError(
    #             "Invalid head_pos {} for snake.".format(head_pos)
    #         )
    # else:
    #     self.head_pos = head_pos
    ##############################################################################
