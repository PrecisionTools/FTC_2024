Version 4
SymbolType BLOCK
LINE Normal -10 8 -13 9
LINE Normal -5 -5 -10 8
LINE Normal -2 -32 -5 -5
LINE Normal -1 28 -2 -32
LINE Normal 2 15 -1 28
LINE Normal 5 6 2 15
LINE Normal 10 5 5 6
LINE Normal 19 5 10 5
LINE Normal -80 -31 -112 -31
LINE Normal -80 -44 -80 -31
LINE Normal -47 -44 -80 -44
LINE Normal 79 -44 57 -44
LINE Normal 79 -32 79 -44
LINE Normal 112 -32 79 -32
RECTANGLE Normal -160 -56 176 56
TEXT -85 41 Left 2 AD3552R glitch
TEXT -37 -47 Left 2 current
WINDOW 0 8 -56 Bottom 2
WINDOW 123 0 74 Center 2
WINDOW 39 1 100 Center 2
WINDOW 40 22 131 Center 2
SYMATTR Value2 offset = 0
SYMATTR SpiceLine period = 8
SYMATTR SpiceLine2 amplitude = 1
PIN -160 32 LEFT 8
PINATTR PinName code
PINATTR SpiceOrder 1
PIN -160 0 LEFT 8
PINATTR PinName SCLK
PINATTR SpiceOrder 2
PIN -160 -32 LEFT 8
PINATTR PinName IN
PINATTR SpiceOrder 3
PIN 176 -32 RIGHT 8
PINATTR PinName OUT
PINATTR SpiceOrder 4
PIN 176 32 RIGHT 8
PINATTR PinName glitch
PINATTR SpiceOrder 5
PIN 176 0 RIGHT 8
PINATTR PinName trigger
PINATTR SpiceOrder 6