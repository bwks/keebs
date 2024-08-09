// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

enum layers
{
    LR0,
    LR1,
    LR2,
};

enum custom_keycodes
{
    HSH_RKT = SAFE_RANGE,
    HSH_BRK,
    LFT_ARW,
    RGT_ARW,
    WALRUS,
    DBL_CLN,
    VIM_QIT,
    VIM_RQT,
    VIM_WR,
    VIM_WRQ,
    NVM_QIT,
};

bool process_record_user(uint16_t keycode, keyrecord_t *record)
{
    switch (keycode)
    {
    case HSH_RKT:
        if (record->event.pressed)
        {
            SEND_STRING("=>");
        }
        break;

    case HSH_BRK:
        if (record->event.pressed)
        {
            SEND_STRING("#[]");
        }
        break;

    case LFT_ARW:
        if (record->event.pressed)
        {
            SEND_STRING("<-");
        }
        break;

    case RGT_ARW:
        if (record->event.pressed)
        {
            SEND_STRING("->");
        }
        break;

    case WALRUS:
        if (record->event.pressed)
        {
            SEND_STRING(":=");
        }
        break;

    case DBL_CLN:
        if (record->event.pressed)
        {
            SEND_STRING("::");
        }
        break;

    case VIM_QIT:
        if (record->event.pressed)
        {
            SEND_STRING(SS_TAP(X_ESC) SS_DELAY(50) ":" SS_DELAY(50) "q" SS_DELAY(50) "!");
        }
        break;

    case VIM_WR:
        if (record->event.pressed)
        {
            SEND_STRING(SS_TAP(X_ESC) SS_DELAY(50) ":" SS_DELAY(50) "w" SS_DELAY(50) SS_TAP(X_ENT));
        }
        break;

    case VIM_WRQ:
        if (record->event.pressed)
        {
            SEND_STRING(SS_TAP(X_ESC) SS_DELAY(50) ":" SS_DELAY(50) "w" SS_DELAY(50) "q" SS_DELAY(50) "!");
        }
        break;

    case VIM_RQT:
        if (record->event.pressed)
        {
            SEND_STRING(SS_TAP(X_ESC) SS_DELAY(50) ":" SS_DELAY(50) "q" SS_DELAY(50) "a" SS_DELAY(50) "!");
        }
        break;

    case NVM_QIT:
        if (record->event.pressed)
        {
            SEND_STRING(SS_TAP(X_ESC) SS_DELAY(50) SS_TAP(X_SPC) SS_DELAY(50) "b" SS_DELAY(50) "d");
        }
        break;
    }
    return true;
};

// clang-format off

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┬───┬───┐          ┌───┬───┬───┬───┬───┬───┐
     * │ ` │ 1 │ 2 │ 3 │ 4 │ 5 │          │ 6 │ 7 │ 8 │ 9 │ 0 │DEL│
     * ├───┼───┼───┼───┼───┼───┤          ├───┼───┼───┼───┼───┼───┤
     * │Tab│ Q │ W │ E │ R │ T │          │ Y │ U │ I │ O │ P │ \ │
     * ├───┼───┼───┼───┼───┼───┤          ├───┼───┼───┼───┼───┼───┤
     * │Lr1│ A │ S │ D │ F │ G │          │ H │ J │ K │ L │ ; │ ' │
     * ├───┼───┼───┼───┼───┼───┤          ├───┼───┼───┼───┼───┼───┤
     * │lr2| Z │ X │ C │ V │ B |          │ N │ M │ , │ . │ ? │Dfl|
     * └───┴───┼───┼───┼───┼───┼───┐  ┌───┼───┼───┼───┼───┼───┴───┘
     *         │   │   │Ctl│Alt│Ctl│  │Alt│Ent│Spc│   │   │
     *         └───┴───┴───┼───┼───┐  ┌───┼───┼───┴───┴───┘
     *                     │Sft|Spr│  │Spr│Esc|   
     *                     └───┴───┘  └───┴───┘
     */
    
    [LR0] = LAYOUT_ortho_6x14(
    /*=======, =======, =======, =======, =======, =======, =======, -- <L R> --  =======, =======, =======, =======, =======, =======, =======,*/
      KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    XXXXXXX, /* <L R> */  XXXXXXX, KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_BSPC, 
      KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    XXXXXXX, /* <L R> */  XXXXXXX, KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_BSLS, 
      MO(LR1), KC_A,    KC_S,    KC_D,    KC_F,    KC_G,    XXXXXXX, /* <L R> */  XXXXXXX, KC_H,    KC_J,    KC_K,    KC_L,    KC_SCLN, KC_QUOT, 
      MO(LR2), KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    XXXXXXX, /* <L R> */  XXXXXXX, KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_NO,  
      XXXXXXX, XXXXXXX, KC_NO,   KC_NO,   KC_LCTL, KC_LSFT, KC_LCTL, /* <L R> */  KC_LSFT, KC_ENT,  KC_SPC,  KC_NO,   KC_NO,   XXXXXXX, XXXXXXX,
      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC_LALT, KC_LGUI, /* <L R> */  KC_LGUI, KC_ESC,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    /*=======, =======, =======, =======, =======, =======, =======, -- <L R> --  =======, =======, =======, =======, =======, =======, =======,*/
    ),

    [LR1] = LAYOUT_ortho_6x14(
    /*=======, =======, =======, =======, =======, =======, =======, -- <L R> --  =======, =======, =======, =======, =======, =======, =======,*/
      XXXXXXX, KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   XXXXXXX, /* <L R> */  XXXXXXX, KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_DEL, 
      XXXXXXX, VIM_QIT, VIM_WRQ, KC_ESC,  VIM_RQT, KC_NO,   XXXXXXX, /* <L R> */  XXXXXXX, KC_MINS, KC_EQL,  KC_UP,   KC_LBRC, KC_RBRC, KC_NO, 
      XXXXXXX, KC_NO,   VIM_WR,  KC_NO,   KC_MEH,  KC_NO,   XXXXXXX, /* <L R> */  XXXXXXX, HSH_RKT, KC_LEFT, KC_DOWN, KC_RGHT, DBL_CLN, WALRUS, 
      XXXXXXX, KC_NO,   NVM_QIT, KC_NO,   KC_HYPR, KC_NO,   XXXXXXX, /* <L R> */  XXXXXXX, HSH_BRK, KC_NO,   LFT_ARW, RGT_ARW, KC_NO,   DF(LR0),  
      XXXXXXX, XXXXXXX, KC_NO,   KC_NO,   KC_LCTL, KC_LSFT, KC_LCTL, /* <L R> */  KC_LSFT, KC_ENT,  KC_SPC,  KC_F11,  KC_F12,  XXXXXXX, XXXXXXX,
      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC_LALT, KC_LGUI, /* <L R> */  KC_LGUI, KC_ESC,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    /*=======, =======, =======, =======, =======, =======, =======, -- <L R> --  =======, =======, =======, =======, =======, =======, =======,*/
    ),

    [LR2] = LAYOUT_ortho_6x14(
    /*=======, =======, =======, =======, =======, =======, =======, -- <L R> --  =======, =======, =======, =======, =======, =======, =======,*/
      XXXXXXX, KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,   XXXXXXX, /* <L R> */  XXXXXXX, KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO, 
      XXXXXXX, KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,   XXXXXXX, /* <L R> */  XXXXXXX, KC_NO,   KC_NO,   KC_PGUP, KC_NO,   KC_PSCR, KC_INS, 
      XXXXXXX, KC_NO,   KC_NO,   KC_NO,   KC_MEH,  KC_NO,   XXXXXXX, /* <L R> */  XXXXXXX, KC_NO,   KC_HOME, KC_PGDN, KC_END,  KC_NO,   KC_NO, 
      XXXXXXX, KC_NO,   KC_NO,   KC_NO,   KC_HYPR, KC_NO,   XXXXXXX, /* <L R> */  XXXXXXX, KC_NO,   KC_NO,   KC_NO,   KC_NO,   KC_NO,   DF(LR0),  
      XXXXXXX, XXXXXXX, KC_NO,   KC_NO,   KC_LCTL, KC_LSFT, KC_LCTL, /* <L R> */  KC_LSFT, KC_ENT,  KC_SPC,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC_LALT, KC_LGUI, /* <L R> */  KC_LGUI, KC_ESC,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    /*=======, =======, =======, =======, =======, =======, =======, -- <L R> --  =======, =======, =======, =======, =======, =======, =======,*/
    ),
    
};
