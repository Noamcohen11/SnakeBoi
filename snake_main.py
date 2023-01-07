##############################################################################
#                                   Imports                                  #
##############################################################################

import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay
from snake import Snake
from wall import Wall

##############################################################################
#                                   Constants                                #
##############################################################################

SNAKE_COLOR = "black"
SNAKE_INIT_SIZE = 3
SNAKE_INIT_DIRECTION = "Up"

WALL_COLOR = "blue"
WALL_SIZE = 3

##############################################################################
#                                   Functions                                #
##############################################################################


def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    snake_len = SNAKE_INIT_SIZE    
    max_apples = args.apples
    # If we are in debug, use a dummy snake.
    if args.debug:
        snake_len = 0
    # Create snake.
    snake = Snake(
        snake_len,
        SNAKE_INIT_DIRECTION,
        (args.width // 2, args.height // 2),
        SNAKE_COLOR,
    )
    game = SnakeGame(args.width, args.height, snake, max_apples)
    gd.show_score(0)
    # DRAW BOARD
    game.draw_board(gd)
    # END OF ROUND 0
    round = 0
    while not (game.is_over() or round == args.rounds):
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
        round += 1


if __name__ == "__main__":
    print("You should run:\n" "> python game_display.py")
