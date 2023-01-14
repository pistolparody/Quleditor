import time

import pygame as pg
from pygame.locals import *

from typing import Optional
from ..structures.Rect import Rect
from .EventHolder import EventHolder,EventConstants
from ..structures.Pos import Pos
from ..drawables.Object import Object
from ..structures.Color import ColorConstants as colors


class Window(EventHolder,Object):
    def __init__(self,window_size:Pos,content_size:Pos):
        super(Window, self).__init__(super_args=Rect(0,0,int(window_size.x),int(window_size.y)))
        self.listen_list = EventConstants.ALL_EVENTS()
        self.surface = pg.display.set_mode(self.margined_rect.size, RESIZABLE)
        self.window_content_size = content_size
        self.color = colors.DEAD_BLUE, colors.HOT_RED, colors.HAPPY_BLUE, colors.GRAY_SKY
        self.adjust(window_size)
        self.has_boundaries = False


    def adjust( self,window_new_size:Pos ):
        self.margined_rect.reset_size(pos=window_new_size)

        diff_in_size = window_new_size.join(self.window_content_size.transform(mult_xy=-1))

        margin_horizontal = diff_in_size.x * 0.8 / 2
        margin_vertical = diff_in_size.y * 0.8 / 2

        border_horizontal = diff_in_size.x * 0.05 / 2
        border_vertical = diff_in_size.y * 0.05 / 2

        padding_horizontal = diff_in_size.x * 0.15 / 2
        padding_vertical = diff_in_size.y * 0.15 / 2

        self.margin = margin_horizontal,margin_vertical,\
                            margin_horizontal,margin_vertical

        self.border = border_horizontal,border_vertical,\
                            border_horizontal,border_vertical

        self.padding = padding_horizontal,padding_vertical,\
                            padding_horizontal,padding_vertical



    def get_events( self ,event_list:list or None=None):
        if event_list is None: event_list = pg.event.get()

        EventHolder.get_events(self,event_list)

        if K_ESCAPE in self.keyboard_pressed_keys:
            self.should_quit = True

        if self.window_size_changed:
            self.adjust(self.window_size)


    def check_events( self ):
        illegal_size = False

        if self.window_size.x == -1 and self.window_size.y == -1:
            self.window_size = Pos(as_tuple=self.surface.get_size())

        new_x = self.window_size.x
        new_y = self.window_size.y

        if self.window_size.x < self.window_content_size.x:
            illegal_size = True
            new_x = self.window_content_size.x

        if self.window_size.y < self.window_content_size.y:
            illegal_size = True
            new_y = self.window_content_size.y

        if illegal_size and self.has_boundaries:
            self.window_size.reset(new_x,new_y)
            self.surface = pg.display.set_mode([new_x,new_y],RESIZABLE)
            self.adjust(Pos(as_tuple=self.surface.get_size()))


    def render_screen( self ):
        Object.render(self,self.surface)

    def update( self ):
        pg.display.update()

