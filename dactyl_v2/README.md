# Dactyl Version 2

## Microcontroller Pinout

Cheap controller from Aliexpress with a similar pinout to the Elite-Pi

[https://circuitpython.org/board/maple_elite_pi/](https://circuitpython.org/board/maple_elite_pi/)

```
 
 Pinout is similar to Elite-Pi
 
 |--- USB ----|
 | D10    D11 |
 | D0     5V  |
 | D1     G   |
 | G      RST |
 | G      3V3 |
 | D2     D29 |
 | D3     D28 |
 | D4     D27 |
 | D5     D26 |
 | D6     D22 |
 | D7     D20 |
 | D8     D23 |
 | D9     D21 |
 |____________|

```

## Wiring Diagram

7 columns x 6 rows

`X` below refers to a position without a key

```
0   1   2   3   4   5   X    X   43  44  45  46  47  48
7   8   9   10  11  12  X    X   50  51  52  53  54  55
14  15  16  17  18  19  X    X   57  58  59  60  61  62
21  22  23  24  25  26  X    X   64  65  66  67  68  69
X   X   30  31  32  33  34   70  71  72  73  74  X   X
X   X   X   X   X   40  41   77  78  X   X   X   X   X
```

## Co-ordinate Mapping

```
0,  1,  2,  3,  4,  5,            43, 44, 45, 46, 47, 48,
7,  8,  9,  10, 11, 12,           50, 51, 52, 53, 54, 55,
14, 15, 16, 17, 18, 19,           57, 58, 59, 60, 61, 62,
21, 22, 23, 24, 25, 26,           64, 65, 66, 67, 68, 69,
        30, 31, 32, 33, 34,   70, 71, 72, 73, 74,
                    40, 41,   77, 78,
```
