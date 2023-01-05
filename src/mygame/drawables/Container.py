import pygame as pg
from typing import Optional
from .Object import Object
from .Sprite import Sprite
from ..structures.Rect import Rect
from ..structures.Pos import Pos
from ..structures.Color import Color,ColorConstants

class Container(Object):
    def __init__(self,rect:Rect):
        super(Container, self).__init__(rect)
        self.object_list :list[Object] = []

    def render( self,surface:pg.surface.Surface ):
        super(Container, self).render(surface)
        for i in self.object_list:
            i.render(surface)

    def create_object( self,object_size:Pos ):
        new_sprite = Sprite(Rect(self.content_rect.x,self.content_rect.y
                                    ,object_size.x,object_size.y))
        new_sprite.margin = 5,5,5,5
        new_sprite.border = 2,2,2,2
        new_sprite.padding = 5,5,5,5

        new_sprite.color = [Color.randomColor(True) for i in range(4)]
        new_sprite.alpha_support = True

        self.object_list.append(new_sprite)

        self.sync_objects()

    def sync_objects( self ):
        pos = self.content_rect.pos.copy()

        last_line_max_height = 0

        last_i = None
        for i in self.object_list:

            if last_i is not None:
                if pos.x + last_i.width + i.width < self.content_rect.x + self.content_rect.width:
                    pos.x += last_i.width
                    if i.height > last_line_max_height :
                        last_line_max_height = i.height
                else:
                    pos.x = self.content_rect.x
                    pos.y += last_line_max_height
                    last_line_max_height = i.height




            i.margined_rect.reset_pos(pos=pos)

            last_i = i


