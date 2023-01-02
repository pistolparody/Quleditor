from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.globals import functions
from mython.mylist import mylist
from mygame.structures.Color import Color

obj = Object(Rect(0,0,150,150))
obj.margin = 50,50,50,50
obj.border = 20,20,20,20
obj.padding = 10,10,10,10

c = Color(10,10,10,10)

c.lerp_me(Color(0,0,0),0.5)

print(obj)
print(obj.margined_rect)
print(obj.bordered_rect)
print(obj.padded_rect)
print(obj.content_rect)


