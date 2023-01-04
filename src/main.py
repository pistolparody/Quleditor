import pygame as pg
from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.globals import functions
from mython.mylist import mylist
from mygame.structures.Color import Color, ColorConstants
from mygame.os.Window import Window

colors = ColorConstants

pg.init()

content_size = Pos(800,600)
window_size = Pos(800,600)
window = Window(window_size, content_size)
obj = Object(Rect(0, 0, int(content_size.x), int(content_size.y)))
obj.color = [i.lerp(Color(255,255,0),0.1) for i in
    [colors.DEAD_BLUE,colors.HOT_RED,colors.DEAD_BLUE,colors.GRAY_SKY]
    ]
obj.margin = 10, 10, 10, 10
obj.border = 5, 5, 5, 5
obj.padding = 20, 20, 20, 20

while not window.should_quit :
    obj.margined_rect = window.content_rect.copy().reset_size(pos=
        window.content_rect.size.transform(sum_xy=3))

    window.get_events()
    window.check_events()
    window.render_screen()
    obj.render(window.surface)
    window.update()
