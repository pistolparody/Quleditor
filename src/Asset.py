import pygame as pg

from Structures import Constants as c
from Structures.Sprite import Sprite
from Structures.Pos import Pos
from Structures.Color import Color

class Asset:
    def __init__( self , path:str=None , surface:pg.surface.Surface=None):
        self.path = path
        self.max_size = None
        if path is not None:
            self.sprite = Sprite(path)
        elif surface is not None:
            self.sprite = Sprite(surface=surface)

        self.width = None
        self.height = None

        self.should_render_debug = False

        self.padding = {
            c.RIGHT:0,
            c.LEFT:0,
            c.UP:0,
            c.DOWN:0
        }

    def get_size( self ):
        result = self.sprite.get_transformed_size()
        result.x += self.padding[c.LEFT]
        result.y += self.padding[c.UP]
        return result

    def get_width( self ):
        return self.get_size().x

    def get_height( self ):
        return self.get_size().y


    def render( self , surface:pg.surface.Surface , top_left:Pos=None,center:Pos=None):
        self.sprite.render(surface,top_left=top_left)