from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.globals import functions
from mython import ListCurse


ListCurse.ActivateCurse()
obj = Object(Rect(0,0,250,250))
obj.border = 50,50,50,50
obj.border = list(obj.border).get_modified(3,10000000)
print(obj.all_attrs)



