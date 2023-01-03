from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.globals import functions
from mython.mylist import mylist
from mygame.structures.Color import Color
from mygame.os.Window import Window

window = Window(Pos(500,500))
print(Window.__mro__)

while not window.should_quit:
    window.get_events()
