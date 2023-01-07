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
BOARD_DIM = 2
