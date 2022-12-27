import pygame as pg

import itertools
from .Color import Color
from .Pos import Pos
from . import Constants


class TextHolder :

    def __init__( self, text: str, font: pg.font.Font, max_width: float = None ) :
        self.__color = Color( 255, 255, 255 )
        self.__text = text
        self.__font = font
        self.__max_width = max_width
        if max_width is None: max_width = 0
        self.__size = Pos( max_width, 0 )

        self.__text_list = []
        self.__surface_list = []
        self.__surface = None
        self.update_text()


    def get_surface( self ) :
        return self.__surface


    def get_size( self ) :
        return self.__size


    def update_text( self, text: str = None ) :
        if text is None : self.__text = self.__text

        self.generate_texts()
        self.generate_surfaces()
        self.generate_surface()


    def generate_texts( self ) :
        counter = 0

        if self.__max_width is None :
            self.__text_list.append( self.__text )
            return

        while counter <= len( self.__text ) :
            first = self.__text[:counter + 1]
            second = self.__text[counter + 1 :]
            next_step = self.__text[:counter + 2]

            if self.__font.size( next_step )[0] > self.__max_width :
                self.__text = second
                self.__text_list.append( first )
                counter = 0
            else :
                counter += 1

        if len( self.__text ) != 0 : self.__text_list.append( self.__text )


    def generate_surfaces( self ) :
        for i in self.__text_list :
            text_surface = self.__font.render( i, True, self.__color )
            if self.__max_width is None : self.__max_width = text_surface.get_width()

            self.__surface_list.append( text_surface )


    def generate_surface( self ) :
        top_left_pos = Pos( 0, 0 )

        height = 0
        for i in self.__surface_list :
            height += i.get_height()
        self.__size.reset( self.__max_width, height )

        self.__surface = pg.surface.Surface( self.__size.get_tuple() ).convert_alpha()
        self.__surface.fill( Constants.GLASS )

        for i in self.__surface_list :
            self.__surface.blit( i, top_left_pos.get_tuple() )
            top_left_pos.y += i.get_height()


    def render( self, surface: pg.surface.Surface, top_left_pos: Pos = None ) :
        if top_left_pos is None : top_left_pos = Pos( 0, 0 )

        surface.blit( self.__surface, top_left_pos.get_tuple() )



