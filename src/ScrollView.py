import pygame as pg

from Structures.Pos import Pos
from Structures.Color import Color
from Structures.Rect import Rect
from Structures import Constants as c


class ScrollView :

    def __init__( self, surface_rect: Rect ) :
        self.rect = surface_rect
        self.background_color: Color = c.DARK_ICE
        self.surface: pg.surface.Surface = pg.surface.Surface(
            surface_rect.get_size()).convert_alpha()
        self.content_list: list[pg.surface.Surface] = []


    def update_surface( self ) :
        self.surface.fill(self.background_color)
        blit_point = Pos(0, 0)
        for i in self.content_list :
            self.surface.blit(i, blit_point)
            blit_point.y += i.get_height()


    def check_events( self ) :
        pass


    def render( self, surface: pg.surface.Surface ) :
        surface.blit(self.surface,self.rect.get_pos())

