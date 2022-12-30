from .Color import Color
from .Enumerator import Enumerator


class ColorTemplate:
    GLASS = Color(0,0,0,0)
    DARK_BLUE = Color(30,30,70)
    WOODEN = Color( 70, 40, 40 )
    DEEP_DARK_RED = Color(38,12,18)
    DARK_ICE = Color(30,43,120)

    GREEN = Color(45,154,93)

    BLACK = Color(0,0,0)
    GRAY = Color(127,127,127)
    WHITE = Color(255,255,255)
    RED = Color(255,0,0)

    P1_MINT = Color(text="#C0EEE4")
    P1_YELLOW = Color(text="#F8F988")
    P1_PEACH = Color(text="#FFCAC8")




Enumerator.reset("Window-Mode")
WINDOW_BLIT_STRETCH = Enumerator.get_next()
WINDOW_REAL_SIZE = Enumerator.get_next()

Enumerator.reset("Event")
MOUSE_LEFT = Enumerator.get_next('MOUSE_LEFT')
MOUSE_MIDDLE = Enumerator.get_next('MOUSE_MIDDLE')
MOUSE_RIGHT = Enumerator.get_next('MOUSE_RIGHT')
MOUSE_KEYS = Enumerator.get_next([MOUSE_LEFT,MOUSE_MIDDLE,MOUSE_RIGHT])
