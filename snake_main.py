import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay


def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = SnakeGame(args.width, args.height)
    gd.show_score(0)
    # DRAW BOARD
    game.draw_board(gd)
    # END OF ROUND 0
    while not game.is_over():
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()
        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


if __name__ == "__main__":
    print("You should run:\n" "> python game_display.py")

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
