from .Color import Color
from .Enumerator import Enumerator

GLASS = Color(0,0,0,0)
DARK_BLUE = Color(30,30,70)
WOODEN = Color( 70, 40, 40 )
DEEP_DARK_RED = Color(38,12,18)
DARK_ICE = Color(30,43,120)


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

Enumerator.reset("Padding")
RIGHT = Enumerator.get_next()
LEFT = Enumerator.get_next()
UP = Enumerator.get_next()
DOWN = Enumerator.get_next()

Enumerator.reset("Size-Boundary")
GROW_BOUND = Enumerator.get_next()
SHRINK_BOUND = Enumerator.get_next()


