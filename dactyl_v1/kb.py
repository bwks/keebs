import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.D4,
        board.D5,
        board.D6,
        board.D7,
        board.D8,
        board.D9,
    )
    row_pins = (
        board.A1,
        board.A0,
        board.SCK,
        board.MISO,
        board.MOSI,
        board.D10,
    )
    diode_orientation = DiodeOrientation.COL2ROW

    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,          41, 40, 39, 38, 37, 36,
        6,  7,  8,  9,  10, 11,         47, 46, 45, 44, 43, 42,
        12, 13, 14, 15, 16, 17,         53, 52, 51, 50, 49, 48,
        18, 19, 20, 21, 22, 23,         59, 58, 57, 56, 55, 54,
        24, 25, 26, 27, 28, 29,         65, 64, 63, 62, 61, 60,
                            35,         71,
    ]
