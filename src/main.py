import pygame as pg
from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.drawables.Container import Container
from mygame.globals import functions
from mython.mylist import mylist
from mygame.structures.Color import Color, ColorConstants
from mygame.os.Window import Window

colors = ColorConstants

pg.init()

content_size = Pos(800,600)
window_size = Pos(1100,800)
window = Window(window_size, content_size)

cont = Container(Rect(0, 0, int(content_size.x), int(content_size.y)))
cont.color = [i.lerp(Color(255,255,0),0.1) for i in
    [colors.DEAD_BLUE,colors.HOT_RED,colors.DEAD_BLUE,colors.GRAY_SKY]
    ]
cont.margin = 10, 10, 10, 10
cont.border = 5, 5, 5, 5
cont.padding = 20, 20, 20, 20

for i in range(100):
    cont.create_object(Pos(47,47))

just_started = True

while not window.should_quit :
    window.get_events()
    if window.window_size_changed or just_started:
        cont.margined_rect = window.content_rect.copy()
        cont.sync_objects()


    window.check_events()
    window.render_screen()
    cont.render(window.surface)


    window.update()

    just_started = False