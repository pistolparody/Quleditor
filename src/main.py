import pygame as pg
from mygame.structures.Pos import Pos
import mygame.os.EventHolder as eventHolder
from mygame.structures.Rect import Rect
from mygame.drawables.Object import Object
from mygame.globals import functions
from mython.mylist import mylist
from mygame.structures.Color import Color,ColorConstants
from mygame.os.Window import Window

pg.init()
window = Window(Pos(800,600),Pos(500,500))

while not window.should_quit:
    window.get_events()
    window.render_and_update()

