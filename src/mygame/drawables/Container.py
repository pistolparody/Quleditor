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
        self.object_list :list[Sprite] = []


    def render( self,surface:pg.surface.Surface,pos_adjust:Pos = None ):
        temp_surface = pg.surface.Surface(self.margined_rect.size)
        super(Container, self).render(temp_surface,self.margined_rect.pos.transform(mult_xy=-1))
        for i in self.object_list:
            i.render(temp_surface,self.margined_rect.pos.transform(mult_xy=-1))

        surface.blit(temp_surface,self.margined_rect.pos.join(pos_adjust))

    def resize_objects( self,scale:float ):

        for i in self.object_list:

            last_margin_rect = i.margined_rect.copy()
            i.margined_rect.reset_size(
                                 pos=i.margined_rect.size.transform(mult_xy=scale))

            if (i.content_rect.width < 0 or i.content_rect.height < 0) and scale < 1:
                i.margined_rect = last_margin_rect

            elif (i.content_rect.width > 100 or i.content_rect.height > 100) and scale >1:
                i.margined_rect = last_margin_rect

            elif type(i) == Sprite:
                i.update()

        self.sync_objects()

    def create_object( self,object_size:Pos ):
        new_sprite = Sprite(Rect(self.content_rect.x,self.content_rect.y
                                    ,object_size.x,object_size.y))
        zero = 0,0,0,0
        new_sprite.margin = 5,5,5,5
        new_sprite.border = 5,5,5,5
        new_sprite.padding = 5,5,5,5

        # new_sprite.margin = new_sprite.border = new_sprite.padding = zero

        new_sprite.color = ColorConstants.BLUE,ColorConstants.BLACK\
                                ,ColorConstants.RED,ColorConstants.HOT_RED
        new_sprite.color = [Color.randomColor(True) for _ in range(4)]
        new_sprite.alpha_support = True

        new_sprite.update()

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


