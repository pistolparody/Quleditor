import pygame as pg

import os
import pathlib
from ..structures.Rect import Rect
from ..structures.Pos import Pos
from ..structures.Color import Color,ColorConstants
from ..structures.Surface import Surface

from .Object import Object

class Sprite(Object):
    def __init__(self,rect:Rect):
        super(Sprite, self).__init__(rect)

        self.path = "../assets/openme.jpg"
        self.raw = pg.image.load(self.path)



    @Object.margin.setter
    def margin( self, new_margin: tuple[float, float, float, float] ) :
        super(Sprite, self.__class__).margin.fset(self, new_margin)  # type: ignore


    @Object.border.setter
    def border( self, new_border: tuple[float, float, float, float] ) :
        super(Sprite, self.__class__).border.fset(self, new_border)  # type: ignore


    @Object.padding.setter
    def padding( self, new_padding: tuple[float, float, float, float] ) :

        super(Sprite, self.__class__).padding.fset(self, new_padding)  # type: ignore


    def render( self, surface: pg.surface.Surface ) :
        super().render(surface)
        surface.blit(self.raw,self.content_rect)




