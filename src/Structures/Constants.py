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

Enumerator.reset("Window-Mode")
BLIT_STRETCH = Enumerator.get_next()
REAL_SIZE = Enumerator.get_next()

Enumerator.reset("Player-Direction")
NORTH = Enumerator.get_next()
SOUTH = Enumerator.get_next()
EAST = Enumerator.get_next()
WEST = Enumerator.get_next()

Enumerator.reset("Player-State")
IDLE = Enumerator.get_next()
WALK = Enumerator.get_next()
RUN = Enumerator.get_next()
CLIMB = Enumerator.get_next()
PUSH = Enumerator.get_next()
SWING = Enumerator.get_next()



