import pygame as pg
from pygame.locals import *

from ..structures.Rect import Rect
from .EventHolder import EventHolder,EventConstants
from ..structures.Pos import Pos
from ..drawables.Object import Object
from ..structures.Color import ColorConstants as colors


class Window(EventHolder,Object):
    def __init__(self,size:Pos):
        super(Window, self).__init__(super_args=Rect(0,0,int(size.x),int(size.y)))
        self.listen_list = EventConstants.ALL_EVENTS()
        self.surface = pg.display.set_mode(self.margined_rect.size,RESIZABLE)
        self.margin = 25,25,25,25
        self.border = 5,5,5,5
        self.padding = 30,30,30,30
        self.color = colors.RED, colors.GREEN, colors.BLUE, colors.BLACK

        print(self.surface)

    def get_events( self ,event_list:list or None=None):
        if event_list is None: event_list = pg.event.get()

        super(Window, self).get_events(event_list)

        if K_ESCAPE in self.keyboard_pressed_keys:
            self.should_quit = True


    def check_events( self ):
        ...

    def render_and_update( self ):
        Object.render(self,self.surface)

        pg.display.update()

