import pygame as pg

from ..structures.Rect import Rect
from .EventHolder import EventHolder
from ..structures.Pos import Pos
from ..drawables.Object import Object

class Window(EventHolder,Object):
    def __init__(self,size:Pos):
        super(Window, self).__init__(super_args=Rect(0,0,int(size.x),int(size.y)))
        self.listen_list = EventHolder.Constants.ALL_EVENTS()
        self.screen = pg.display.set_mode(self.margined_rect.size)


    def get_events( self ,event_list:list or None=None):
        if event_list is None: event_list = pg.event.get()

        super(Window, self).get_events(event_list)
