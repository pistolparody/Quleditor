from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.globals import functions

obj = Object(Rect(0,0,250,250))
obj.border = 50,50,50,50
obj.border = tuple(list(obj.border[:2])+[10]+list(obj.border[3:]))
print(obj.all_attrs)
