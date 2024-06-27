import board

from kb import KMKKeyboard

from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType

from storage import getmount

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

data_pin_1 = board.TX if str(getmount("/").label).endswith("L") else board.RX
data_pin_2 = (
    board.RX if str(getmount("/").label).endswith("L") else board.TX
)  # Future use

# Split Keyboard
split = Split(split_type=SplitType.UART, use_pio=True, data_pin=data_pin_1)
keyboard.modules.append(split)

# Hold Tap
# holdtap = HoldTap()
# holdtap.tap_time = 200
# holdtap.tap_interupted = False
# holdtap.prefer_hold = False
# holdtap.repeat = HoldTapRepeat.TAP
# keyboard.modules.append(holdtap)

L1_F = KC.LT(1, KC.F, prefer_hold=False, tap_time=200)
L2_A = KC.LT(2, KC.A, prefer_hold=False, tap_time=200)


HASH_ROCKET = send_string("=>")
HASH_BRACKET = send_string("#[]")
LEFT_ARROW = send_string("<-")
RIGHT_ARROW = send_string("->")
WALRUS = send_string(":=")
DOUBLE_COLON = send_string("::")
MEH = KC.LCTRL(KC.LSFT(KC.LALT))

# Layer keys
L1 = KC.MO(1)
L2 = KC.MO(2)


# Easier to see in layout
_____ = KC.TRNS
XXXXX = KC.NO

VIM_QUIT = simple_key_sequence(
    (
        KC.ESC,
        send_string(":"),
        KC.Q,
        KC.MACRO_SLEEP_MS(100),
        send_string("!"),
    )
)
VIM_RAGE_QUIT = simple_key_sequence(
    (
        KC.ESC,
        send_string(":"),
        KC.Q,
        KC.A,
        KC.MACRO_SLEEP_MS(100),
        send_string("!"),
    )
)
VIM_WR = simple_key_sequence(
    (
        KC.ESC,
        send_string(":"),
        KC.W,
        KC.MACRO_SLEEP_MS(100),
        KC.ENTER,
    )
)
VIM_WR_QUIT = simple_key_sequence(
    (
        KC.ESC,
        send_string(":"),
        KC.W,
        KC.Q,
        KC.MACRO_SLEEP_MS(100),
        send_string("!"),
    )
)

keyboard.keymap = [
    [  # Layer 0
        KC.GRAVE,
        KC.N1,
        KC.N2,
        KC.N3,
        KC.N4,
        KC.N5,
        KC.N6,
        KC.N7,
        KC.N8,
        KC.N9,
        KC.N0,
        KC.BSPACE,
        KC.TAB,
        KC.Q,
        KC.W,
        KC.E,
        KC.R,
        KC.T,
        KC.Y,
        KC.U,
        KC.I,
        KC.O,
        KC.P,
        KC.BSLS,
        KC.MO(1),
        KC.A,
        KC.S,
        KC.D,
        KC.F,
        KC.G,
        KC.H,
        KC.J,
        KC.K,
        KC.L,
        KC.SCLN,
        KC.QUOTE,
        KC.MO(2),
        KC.Z,
        KC.X,
        KC.C,
        KC.V,
        KC.B,
        KC.N,
        KC.M,
        KC.COMM,
        KC.DOT,
        KC.SLSH,
        XXXXX,
        XXXXX,
        XXXXX,
        KC.LCTRL,
        KC.LSHIFT,
        KC.LALT,
        KC.LCTRL,
        XXXXX,
        KC.ESC,
        KC.ENTER,
        KC.SPACE,
        XXXXX,
        XXXXX,
        KC.LGUI,
        KC.LGUI,
    ],
]

if __name__ == "__main__":
    keyboard.go()
