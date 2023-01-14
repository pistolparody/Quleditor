import pygame as pg
from pygame.locals import *

from random import randint as rand

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

def print_objects():
    print("Container {")
    for i in cont.object_list:
        print("\t",i.margined_rect)
    print("}")

just_started = True
clock = pg.time.Clock()
fps = 60
adjust_pos = Pos(0,0)
adjust_step = 2
while not window.should_quit :
    window.get_events()
    if window.window_size_changed or just_started:
        cont.margined_rect = window.content_rect.copy()
        cont.sync_objects()


    if K_a in window.keyboard_held_keys:
        cont.create_object(Pos(rand(50,50),rand(50,50)))


    if K_s in window.keyboard_pressed_keys:
        cube = rand(40,40)
        cont.create_object(Pos(cube,cube))

    if K_d in window.keyboard_held_keys or K_c in window.keyboard_pressed_keys:
        cont.resize_objects(0.95)

    if K_f in window.keyboard_held_keys or K_v in window.keyboard_pressed_keys:
        cont.resize_objects(1.05)

    if K_q in window.keyboard_pressed_keys:
        cont.object_list.clear()

    if K_UP in window.keyboard_held_keys: adjust_pos.y -= adjust_step
    if K_DOWN in window.keyboard_held_keys : adjust_pos.y += adjust_step
    if K_RIGHT in window.keyboard_held_keys : adjust_pos.x += adjust_step
    if K_LEFT in window.keyboard_held_keys : adjust_pos.x -= adjust_step

    window.check_events()
    window.render_screen()
    cont.render(window.surface,adjust_pos)


    window.update()
    clock.tick(fps)

    just_started = False