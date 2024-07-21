import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

# YD-RP2040 from Ali Express
# https://circuitpython.org/board/vcc_gnd_yd_rp2040/
#
# |-------- USB -------|
# | GP0           VOUT |
# | GP1           VIN  |
# | GND           GND  |
# | GP2           GP23 |
# | GP3           3V3  |
# | GP4           GP29 |
# | GP5           GP28 |
# | GND           GND  |
# | GP6           GP27 |
# | GP7           GP26 |
# | GP8           RUN  |
# | GP9           GP22 |
# | GND           GND  |
# | GP10          GP21 |
# | GP11          GP20 |
# | GP12          GP19 |
# | GP13          GP18 |
# | GND           GND  |
# | GP14          GP17 |
# | GP15          GP16 |
# |                    |
# | 3V SWDID SWCLK GND |
# |____________________|


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        # left
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        # right
        board.GP22,
        board.GP21,
        board.GP20,
        board.GP19,
        board.GP18,
        board.GP17,
        board.GP16,
    )
    row_pins = (
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
    )
    diode_orientation = DiodeOrientation.COL2ROW

    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,            8,  9,  10, 11, 12, 13,
        14, 15, 16, 17, 18, 19,           22, 23, 24, 25, 26, 27,
        28, 29, 30, 31, 32, 33,           36, 37, 38, 39, 40, 41,
        42, 43, 44, 45, 46, 47,           50, 51, 52, 53, 54, 55, 
                58, 59, 60, 61, 62,   63, 64, 65, 66, 67,
                            75, 76,   77, 78,
    ]
