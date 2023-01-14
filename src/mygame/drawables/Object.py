from typing import Optional

import pygame as pg

from ..structures.Pos import Pos
from ..structures.Rect import Rect
from ..structures.Color import Color,ColorConstants
from ..structures.Surface import Surface

colors = ColorConstants

# It could have been DrawableObject but that's not finger friendly
class Object(object) :
    """
    "Object" contains the information about how something should be rendered
    on the screen.
    The content to be rendered is provided by subclasses that use this class
     it has padding, border and margin properties.
    But its functionality is completely different from HTML drawable objects.
    Since the rect parameter which is fed to this Object while initialization determines
     an absolute rendering point and  DOES NOT CHANGE IN RELATION TO OTHER OBJECTS.
    So the rectangular size of the content to be rendered is:
        content_width = rect.width - padding_horizontal + border_horizontal + margin_horizontal
        content_height = rect.height - padding_vertical + border_vertical + margin_vertical

    """
    def __init__( self, rect: Rect ) :

        self.__rect: Rect = rect

        self.alpha_support:bool = False

        self.margined_color: Optional[Color,None] = None
        self.bordered_color: Optional[Color,None] = None
        self.padded_color: Optional[Color,None] = None
        self.content_color: Optional[Color,None] = None

        self.padding_left = 0
        self.padding_right = 0
        self.padding_top = 0
        self.padding_bottom = 0

        self.margin_left = 0
        self.margin_right = 0
        self.margin_top = 0
        self.margin_bottom = 0

        self.border_left_width = 0
        self.border_right_width = 0
        self.border_top_width = 0
        self.border_bottom_width = 0

        self.color = colors.BLUE,colors.BLACK,colors.GREEN,colors.WHITE


        super(Object, self).__init__()

    def __str__(self):
        return f'Object{{\n\trect:{self.margined_rect}\n\tmargin:{self.margin}'\
               f'\n\tborder:{self.border}'\
               f'\n\tpadding:{self.padding}\n}}'

    @property
    def color( self ):
        return self.margined_color,self.bordered_color,self.padded_color,self.content_color

    @color.setter
    def color( self,colors_:tuple[Color,Color,Color,Color] ):
        self.margined_color = colors_[0]
        self.bordered_color = colors_[1]
        self.padded_color = colors_[2]
        self.content_color = colors_[3]

    @property
    def x( self ):
        return self.__rect.x

    @property
    def y( self ) :
        return self.__rect.y

    @property
    def width( self ) :
        return self.__rect.width

    @property
    def height( self ) :
        return self.__rect.height

    @property
    def margined_rect( self ):
        return self.__rect

    @margined_rect.setter
    def margined_rect( self,p_rect:Rect ):
       self.__rect.reset(p_rect)

    @property
    def bordered_rect( self ):
        rect = self.margined_rect.copy()

        rect.x += self.margin_left
        rect.width -= self.margin_right * 2

        rect.y += self.margin_top
        rect.height -= self.margin_bottom * 2

        return rect

    @property
    def padded_rect( self ):
        rect = self.bordered_rect.copy()

        rect.x += self.border_left_width
        rect.width -= self.border_right_width * 2

        rect.y += self.border_top_width
        rect.height -= self.border_bottom_width * 2

        return rect


    @property
    def content_rect( self ) :
        rect = self.padded_rect.copy()

        rect.x += self.padding_left
        rect.width -= self.padding_right * 2

        rect.y += self.padding_top
        rect.height -= self.padding_bottom * 2

        return rect



    @property
    def padding( self ) -> tuple[float,float,float,float]:
        return self.padding_left, self.padding_top, self.padding_right, self.padding_bottom


    @padding.setter
    def padding( self, new_padding: tuple[float, float, float, float] ) :
        self.padding_left, self.padding_top = new_padding[:2]
        self.padding_right, self.padding_bottom = new_padding[2 :]


    @property
    def margin( self ) -> tuple[float,float,float,float] :
        return self.margin_left, self.margin_top, self.margin_right, self.margin_bottom


    @margin.setter
    def margin( self, new_margin: tuple[float, float, float, float] ) :
        self.margin_left, self.margin_top = new_margin[:2]
        self.margin_right, self.margin_bottom = new_margin[2 :]


    @property
    def border( self ) -> tuple[int, int, int, int] :
        return self.border_left_width, self.border_top_width,\
            self.border_right_width, self.border_bottom_width

    @border.setter
    def border( self, new_border: tuple[int, int, int, int] ) :
        self.border_left_width, self.border_top_width = new_border[:2]
        self.border_right_width, self.border_bottom_width = new_border[2 :]

    def render( self,surface:pg.surface.Surface,pos_adjust:Pos = None ) :
        if pos_adjust is None: pos_adjust = Pos(0,0)

        margined_rect = self.margined_rect.copy().transform_pos(pos_adjust.x,pos_adjust.y)
        bordered_rect = self.bordered_rect.copy().transform_pos(pos_adjust.x,pos_adjust.y)
        padded_rect = self.padded_rect.copy().transform_pos(pos_adjust.x,pos_adjust.y)
        content_rect = self.content_rect.copy().transform_pos(pos_adjust.x,pos_adjust.y)

        if self.alpha_support:
            temp_surface = pg.surface.Surface(margined_rect.size).convert_alpha()

            diff = Pos(-self.x - pos_adjust.x, -self.y - pos_adjust.y)

            pg.draw.rect(temp_surface, self.margined_color
                            , margined_rect.copy().transform_pos(sum_xy=diff.x, sum_y=diff.y))

            pg.draw.rect(temp_surface, self.bordered_color,
                bordered_rect.copy().transform_pos(sum_xy=diff.x, sum_y=diff.y))

            pg.draw.rect(temp_surface, self.padded_color,
                padded_rect.copy().transform_pos(sum_xy=diff.x, sum_y=diff.y))

            pg.draw.rect(temp_surface, self.content_color,
                content_rect.copy().transform_pos(sum_xy=diff.x, sum_y=diff.y))

            surface.blit(temp_surface,margined_rect)
        else:
            pg.draw.rect(surface,self.margined_color,margined_rect)
            pg.draw.rect(surface,self.bordered_color,bordered_rect)
            pg.draw.rect(surface,self.padded_color,padded_rect)
            pg.draw.rect(surface,self.content_color,content_rect)

    def all_attrs( self ) -> str :
        text = "Object {\n"
        L = vars(self)
        for i in L :
            text += "\t" + str(i) + " = " + str(L[i]) + "\n"
        text += "}"
        return text
