from kb import KMKKeyboard

from kmk.modules.macros import Macros, Delay
from kmk.keys import KC
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(Macros())


VIM_LEADER = KC.SPACE
KEY_SEQ_WAIT = 50

HASH_ROCKET = KC.MACRO("=>")
HASH_BRACKET = KC.MACRO("#[]")
LEFT_ARROW = KC.MACRO("<-")
RIGHT_ARROW = KC.MACRO("->")
WALRUS = KC.MACRO(":=")
DOUBLE_COLON = KC.MACRO("::")
MEH = KC.LCTRL(KC.LSFT(KC.LALT))
MEHS = KC.LCTRL(KC.LSFT(KC.LALT(KC.LGUI)))

# Layer keys
L1 = KC.MO(1)
L2 = KC.MO(2)


# Easier to see in layout
_____ = KC.TRNS
XXXXX = KC.NO

NVIM_CLOSE = KC.MACRO(
    KC.ESC,
    Delay(KEY_SEQ_WAIT),
    VIM_LEADER,
    Delay(KEY_SEQ_WAIT),
    KC.B,
    Delay(KEY_SEQ_WAIT),
    KC.D,
)
VIM_QUIT = KC.MACRO(
    KC.ESC,
    Delay(KEY_SEQ_WAIT),
    KC.MACRO(":"),
    Delay(KEY_SEQ_WAIT),
    KC.Q,
    Delay(KEY_SEQ_WAIT),
    KC.MACRO("!"),
)
VIM_RAGE_QUIT = KC.MACRO(
    KC.ESC,
    Delay(KEY_SEQ_WAIT),
    KC.MACRO(":"),
    Delay(KEY_SEQ_WAIT),
    KC.Q,
    Delay(KEY_SEQ_WAIT),
    KC.A,
    Delay(KEY_SEQ_WAIT),
    KC.MACRO("!"),
)
VIM_WR = KC.MACRO(
    KC.ESC,
    Delay(KEY_SEQ_WAIT),
    KC.MACRO(":"),
    Delay(KEY_SEQ_WAIT),
    KC.W,
    Delay(KEY_SEQ_WAIT),
    KC.ENTER,
)
VIM_WR_QUIT = KC.MACRO(
    KC.ESC,
    Delay(KEY_SEQ_WAIT),
    KC.MACRO(":"),
    Delay(KEY_SEQ_WAIT),
    KC.W,
    Delay(KEY_SEQ_WAIT),
    KC.Q,
    Delay(KEY_SEQ_WAIT),
    KC.MACRO("!"),
)

# fmt: off
keyboard.keymap = [
    [   # Layer 0
        KC.GRAVE,    KC.N1,       KC.N2,           KC.N3,          KC.N4,        KC.N5,                                           KC.N6,        KC.N7,       KC.N8,         KC.N9,        KC.N0,          KC.BSPACE,
        KC.TAB,      KC.Q,        KC.W,            KC.E,           KC.R,         KC.T,                                            KC.Y,         KC.U,        KC.I,          KC.O,         KC.P,           KC.BSLS,
        KC.MO(1),    KC.A,        KC.S,            KC.D,           KC.F,         KC.G,                                            KC.H,         KC.J,        KC.K,          KC.L,         KC.SCLN,        KC.QUOTE,
        KC.MO(2),    KC.Z,        KC.X,            KC.C,           KC.V,         KC.B,                                            KC.N,         KC.M,        KC.COMM,       KC.DOT,       KC.SLSH,        XXXXX,
                                  XXXXX,           XXXXX,          KC.LCTRL,     KC.LSHIFT,      KC.LCTRL,         KC.LSHIFT,     KC.ENTER,     KC.SPACE,    XXXXX,         XXXXX,
                                                                                 KC.LALT,        KC.LGUI,          KC.LGUI,       KC.ESC,
    ],
    [   # Layer 1
        XXXXX,       KC.F1,       KC.F2,           KC.F3,          KC.F4,         KC.F5,                                          KC.F6,          KC.F7,       KC.F8,         KC.F9,          KC.F10,         KC.DEL,
        XXXXX,       VIM_QUIT,    VIM_WR_QUIT,     KC.ESC,         VIM_RAGE_QUIT, XXXXX,                                          KC.MINUS,       KC.EQUAL,    KC.UP,         KC.LBRACKET,    KC.RBRACKET,    XXXXX,
        XXXXX,       XXXXX,       VIM_WR,          XXXXX,          MEH,           XXXXX,                                          HASH_ROCKET,    KC.LEFT,     KC.DOWN,       KC.RIGHT,       DOUBLE_COLON,   WALRUS,
        XXXXX,       XXXXX,       NVIM_CLOSE,      XXXXX,          MEHS,          XXXXX,                                          HASH_BRACKET,   XXXXX,       LEFT_ARROW,    RIGHT_ARROW,    XXXXX,          KC.DF(0),
                                  XXXXX,           XXXXX,          KC.LCTRL,      KC.LSHIFT,      KC.LCTRL,        KC.LSHIFT,     KC.ENTER,       KC.SPACE,    KC.F11,        KC.F12,
                                                                                  KC.LALT,        KC.LGUI,         KC.LGUI,       KC.LALT,
    ],
    [   # Layer 2
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,         XXXXX,                                          XXXXX,          XXXXX,       XXXXX,         XXXXX,          XXXXX,          XXXXX,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,         XXXXX,                                          XXXXX,          XXXXX,       KC.PGUP,       XXXXX,          XXXXX,          XXXXX,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,         XXXXX,                                          XXXXX,          KC.HOME,     KC.PGDN,       KC.END,         XXXXX,          XXXXX,
        XXXXX,       XXXXX,       XXXXX,           XXXXX,          XXXXX,         XXXXX,                                          XXXXX,          XXXXX,       XXXXX,         XXXXX,          XXXXX,          KC.DF(0),
                                  XXXXX,           XXXXX,          KC.LCTRL,      KC.LSHIFT,       KC.LCTRL,       KC.LSHIFT,     XXXXX,          XXXXX,       XXXXX,         XXXXX,          
                                                                                  KC.LALT,         XXXXX,          KC.LGUI,       XXXXX,
    ],

]

if __name__ == "__main__":
    keyboard.go()
