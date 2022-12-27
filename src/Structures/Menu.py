import pygame as pg

from . import Constants
from .Pos import Pos
from .Rect import Rect
from .Color import Color
from .Page import Page

from .TextHolder import TextHolder
from .TextBox import TextBox



class Menu :
    class PageDetails :

        def __init__( self ) :
            self.page = None


    class Item :
        __id = 0

        def __init__( self, name: str, page_pointer: str, item_pointer: str ) :
            self.name = name
            self.page_pointer = page_pointer
            self.item_pointer = item_pointer
            self.id = Menu.Item.__id

            self.text_holder = None
            self.text_box = None

            Menu.Item.__id += 1


        def get_item_by_pointer( self, page_dict: dict ) :
            return page_dict[self.page_pointer][1][self.item_pointer]

        def get_page_details_by_pointer( self, page_dict: dict ):
            return page_dict[self.page_pointer][0]


    def __init__( self, surface_size: Pos, surface_pos: Pos = Pos( 0, 0 ) ) :
        self.__surface_rect = Rect.fromPos( surface_pos, surface_size )

        self.__surface = pg.surface.Surface(
            self.__surface_rect.get_size().get_tuple() ).convert_alpha()

        self.__surface_color = Color( 0, 0, 0, 0 )

        self.__page_dict = {}


    def add_page( self, key, page_details: PageDetails, item_list: list[Item] ) :
        self.__page_dict[key] = (page_details, {})
        for i in item_list :
            self.__page_dict[key][1][i.name] = (i.page_pointer, i.item_pointer)


    def set_color( self, color: Color ) :
        self.__surface_color = color


    def get_events( self, event_list=None ) :
        if event_list is None : event_list = list()

        if len( event_list ) == 0 : event_list = pg.event.get()

        for i in event_list :
            pass


    def check_events( self ) :
        pass


    def render( self, surface: pg.surface.Surface ) :
        self.__surface.fill( self.__surface_color.get_tuple() )

        surface.blit( self.__surface, self.__surface_rect.get_pos().get_tuple() )


    def run( self, surface: pg.surface.Surface, event_list: list = None ) :
        self.get_events( event_list )
        self.check_events()
        self.render( surface )

