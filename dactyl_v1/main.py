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

data_pin_1 = board.TX if str(getmount('/').label).endswith("L") else board.RX
data_pin_2 = board.RX if str(getmount('/').label).endswith("L") else board.TX  # Future use

# Split Keyboard
split = Split(split_type=SplitType.UART, use_pio=True, data_pin=data_pin_1)
keyboard.modules.append(split)

# Hold Tap
holdtap = HoldTap()
holdtap.tap_time = 500
holdtap.tap_interupted = False
holdtap.prefer_hold = False
holdtap.repeat = HoldTapRepeat.TAP
keyboard.modules.append(holdtap)

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
        send_string("!"),
    )
)
VIM_WR = simple_key_sequence(
    (
        KC.ESC,     
        send_string(":"),
        KC.W,
    )
)
VIM_WR_QUIT = simple_key_sequence(
    (
        KC.ESC,
        send_string(":"),
        KC.W,
        KC.Q,
        send_string("!"),
    )
)

keyboard.keymap = [
    [   # Layer 0
        KC.GRAVE,    KC.N1,       KC.N2,           KC.N3,          KC.N4,        KC.N5,        KC.N6,          KC.N7,       KC.N8,         KC.N9,          KC.N0,          KC.BSPACE,
        KC.TAB,      KC.Q,        KC.W,            KC.E,           KC.R,         KC.T,         KC.Y,           KC.U,        KC.I,          KC.O,           KC.P,           KC.BSLS,
        L1,          KC.A,        KC.S,             KC.D,           KC.F,         KC.G,         KC.H,           KC.J,        KC.K,          KC.L,           KC.SCLN,        KC.QUOTE,
        L2,          KC.Z,        KC.X,            KC.C,           KC.V,         KC.B,         KC.N,           KC.M,        KC.COMM,       KC.DOT,         KC.SLSH,        XXXXX,
        XXXXX,       XXXXX,       KC.LCTRL,        KC.LSHIFT,      KC.LALT,      XXXXX,        XXXXX,          KC.ESC,      KC.ENTER,      KC.SPACE,       XXXXX,          XXXXX,
                                                                   XXXXX,        KC.LGUI,
    ],
    [
        # Layer 1 
        XXXXX,       KC.F1,       KC.F2,           KC.F3,          KC.F4,        KC.F5,        KC.F6,          KC.F7,       KC.F8,         KC.F9,          KC.F10,         KC.DEL,
        XXXXX,       VIM_QUIT,    VIM_WR_QUIT,     XXXXX,          XXXXX,        XXXXX,        KC.MINUS,       KC.EQUAL,    KC.UP,         KC.LBRACKET,    KC.RBRACKET,    XXXXX,
        XXXXX,       XXXXX,       VIM_WR,          XXXXX,          MEH,          XXXXX,        HASH_ROCKET,    KC.LEFT,     KC.DOWN,       KC.RIGHT,       DOUBLE_COLON,   WALRUS,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,        XXXXX,        XXXXX,          XXXXX,       LEFT_ARROW,    RIGHT_ARROW,    XXXXX,          XXXXX,
        XXXXX,       XXXXX,       KC.LCTRL,        KC.LSHIFT,      KC.LALT,      XXXXX,        XXXXX,          XXXXX,       XXXXX,         XXXXX,          KC.F11,         KC.F12,
                                                                   XXXXX,        XXXXX,
    ],
    [
        # Layer 2
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,        XXXXX,        XXXXX,          XXXXX,       XXXXX,         XXXXX,          XXXXX,          XXXXX,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,        XXXXX,        XXXXX,          XXXXX,       KC.PGUP,       XXXXX,          XXXXX,          XXXXX,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,        XXXXX,        XXXXX,          KC.HOME,     KC.PGDN,       KC.END,         XXXXX,          XXXXX,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,        XXXXX,        XXXXX,          XXXXX,       XXXXX,         XXXXX,          XXXXX,          XXXXX,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,        XXXXX,        XXXXX,          XXXXX,       XXXXX,         XXXXX,          XXXXX,          XXXXX,
                                                                   XXXXX,        XXXXX,    
    ],
]

if __name__ == '__main__':
    keyboard.go()
