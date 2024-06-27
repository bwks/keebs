import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

# Pinout is similar to Elite-Pi
# https://circuitpython.org/board/maple_elite_pi/
#
# |--- USB ----|
# | D10    D11 |
# | D0     5V  |
# | D1     G   |
# | G      RST |
# | G      3V3 |
# | D2     D29 |
# | D3     D28 |
# | D4     D27 |
# | D5     D26 |
# | D6     D22 |
# | D7     D20 |
# | D8     D23 |
# | D9     D21 |
# |____________|


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.D3,
        board.D4,
        board.D5,
        board.D6,
        board.D7,
        board.D8,
        board.D9,
    )
    row_pins = (
        board.D27,
        board.D26,
        board.D22,
        board.D20,
        board.D23,
        board.D21,
    )
    diode_orientation = DiodeOrientation.COL2ROW

    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,            43, 44, 45, 46, 47, 48,
        7,  8,  9,  10, 11, 12,           50, 51, 52, 53, 54, 55,
        14, 15, 16, 17, 18, 19,           57, 58, 59, 60, 61, 62,
        21, 22, 23, 24, 25, 26,           64, 65, 66, 67, 68, 69,
                30, 31, 32, 33, 34,   70, 71, 72, 73, 74,
                            40, 41,   77, 78,
    ]
