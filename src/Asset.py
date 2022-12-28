import pygame as pg

import pathlib

from Structures import Constants as c
from Structures.Sprite import Sprite
from Structures.Pos import Pos
from Structures.Rect import Rect
from Structures.Color import Color


class Asset :

    def __init__( self, path: str = None, surface: pg.surface.Surface = None ) :
        self.path = pathlib.PurePath(path)
        self.name = self.path.name

        self.max_size = None
        if path is not None and surface is None:
            self.sprite = Sprite(path)
        elif surface is not None :
            self.sprite = Sprite(surface=surface)

        self.max_size: Pos = None


        self.should_render_debug = True
        self.background_color = c.BLACK.copy().set_alpha(int(0.35 * 255))

        self.padding_left = 10
        self.padding_right = 10
        self.padding_top = 10
        self.padding_bottom = 10

        self.rect = Rect(0,0,0,0)


    def set_max_size( self, max_size: Pos ) :
        self.max_size = max_size
        self.sprite.max_size = self.max_size.copy()
        self.rect = Rect.fromPos(Pos(0,0),self.get_padded_size())
        return self

    def set_padding(self,padding_left:int=0,padding_right:int=0,
                            padding_top:int=0,padding_bottom:int=0):

        self.padding_left = padding_left
        self.padding_right = padding_right
        self.padding_bottom = padding_bottom
        self.padding_top = padding_top

    def transform_sprite( self ) :
        if self.max_size is not None :
            self.sprite.transform_max_size(self.max_size)
            self.sprite.transform_image()


    def set_render_debug( self, render_debug: bool = False ) :
        self.should_render_debug = render_debug
        self.sprite.should_render_debug = self.should_render_debug


    def get_size( self ) :
        result = self.max_size
        return result


    def get_padded_size( self ) -> Pos :
        result = self.max_size.copy()
        result.x += self.padding_right + self.padding_left
        result.y += self.padding_top + self.padding_bottom
        return result


    def get_width( self ) :
        return self.get_size().x


    def get_height( self ) :
        return self.get_size().y

    def render_debug( self, surface: pg.surface.Surface, top_left: Pos = None, center: Pos = None ) :
        if top_left is not None : blit_point = top_left
        elif center is not None : blit_point = center
        else : blit_point = self.rect.get_pos().copy()

        sprite_rect = Rect.fromPos(
            Pos(blit_point.x + self.padding_left, blit_point.y + self.padding_top), self.get_size())

        pg.draw.rect(surface, c.RED.copy().set_alpha(125), sprite_rect, 1)

        pg.draw.rect(surface, c.WHITE, Rect.fromPos(blit_point, self.get_padded_size()), 1)

    def render( self, surface: pg.surface.Surface, top_left: Pos = None, center: Pos = None ) :
        if top_left is not None : blit_point = top_left
        elif center is not None : blit_point = center
        else : blit_point = self.rect.get_pos().copy()

        sprite_rect = Rect.fromPos(
            Pos(blit_point.x + self.padding_left, blit_point.y + self.padding_top), self.get_size())

        self.sprite.render(surface, center=sprite_rect.get_center())

        if self.should_render_debug:
            self.render_debug(surface, top_left, center)



