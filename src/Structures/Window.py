import pygame as pg
from pygame.locals import *

from . import Constants
from .Enumerator import Enumerator
from . import TextBox
from .Pos import Pos


class Window :

    def __init__( self, size: Pos, mask_size: Pos, title: str, fps ,
                            render_mode:Enumerator = None) :

        if render_mode is None: render_mode = Constants.BLIT_STRETCH

        self.is_running = True
        self.__size_changed = False
        self.__mouse_in = False
        self.__mouse_entered = False
        self.__mouse_moved = False
        self.window_size_changed = False

        self.__render_mode = render_mode

        self.__fps = fps
        self.__last_dropped_file = None

        self.__window_size = size
        self.__mask_size = mask_size

        self.__mouse_init_pos = self.__mask_size.get_transformed_pos( mult=0.5 )
        self.__mouse_pos = Pos.copy( self.__mouse_init_pos )

        self.__clock = pg.time.Clock()
        self.__mask = pg.surface.Surface( self.__mask_size.get_tuple() )
        self.__window = pg.display.set_mode( self.__window_size.get_tuple(), RESIZABLE )

        self.__window_title = title

        pg.display.set_caption( self.__window_title )


    def get_window( self ) -> pg.surface.Surface :
        return self.__window

    def get_mask( self ) -> pg.surface.Surface :
        return self.__mask

    def get_window_size( self ) -> Pos :
        return self.__window_size

    def get_mask_size( self ) -> Pos :
        return self.__mask_size

    def get_mouse_pos( self ) -> Pos :
        return self.__mouse_pos

    def get_transformed_mouse_pos( self ) :
        copy_pos = self.__mouse_pos.copy()
        x_scale = self.__window_size.x / self.__mask_size.x
        y_scale = self.__window_size.y / self.__mask_size.y

        copy_pos.x /= x_scale
        copy_pos.y /= y_scale

        return copy_pos


    def get_dropped_file( self ) -> str or None :
        return self.__last_dropped_file

    def set_render_mode( self , render_mode:Enumerator ):
        self.__render_mode = render_mode

    def set_fps( self , fps:int ):
        self.__fps = fps

    def check_events( self ) :
        if self.__mouse_in :
            if not self.__mouse_entered :
                pass
                # pg.mouse.set_pos( self.__mouse_init_pos.get_tuple() )

            self.__mouse_pos.x, self.__mouse_pos.y = pg.mouse.get_pos()
            self.__mouse_in = False
            self.__mouse_entered = True

        if self.__mouse_moved:
            self.__mouse_pos.x, self.__mouse_pos.y = pg.mouse.get_pos()
            self.__mouse_moved = False


    def render_and_update( self ) :
        if self.__render_mode == Constants.BLIT_STRETCH:
            transformed_mask = pg.transform.scale( self.__mask, self.__window_size.get_tuple() )

            self.__window.blit( transformed_mask, [0, 0] )


        pg.display.update()


    def get_events( self, event_list=None ) :

        self.window_size_changed = False

        if event_list is None : event_list = list()

        if len( event_list ) == 0 : event_list = pg.event.get()

        for i in event_list :

            if i.type == MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0] : print( self.__mouse_pos )

            if i.type == MOUSEMOTION:
                self.__mouse_moved = True

            if i.type == DROPFILE :
                self.__last_dropped_file = i.file

            if i.type == WINDOWENTER :
                self.__mouse_in = True

            if i.type == WINDOWSIZECHANGED :
                self.__window_size.reset( i.x, i.y )
                self.window_size_changed = True

            if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE :
                self.is_running = False


    def tick( self ) :
        self.__clock.tick( self.__fps )

    def run( self , event_list:list=None):
        self.get_events(event_list)
        self.check_events()
        self.render_and_update()
        self.tick()
