import pygame as pg

from .TextHolder import TextHolder
from .Rect import Rect
from .Pos import Pos
from .Color import Color
from . import Constants
from .Sprite import Sprite
from .MSprite import MSprite


class TextBox:
    def __init__(self,rect:Rect,textHolder:TextHolder):

        self.__text_pos = Pos(0,0)
        self.__text_holder = textHolder
        self.__rect = rect
        self.__surface = pg.surface.Surface(self.__rect.get_size().get_tuple()).convert_alpha()

        self.__background_color = Constants.WOODEN
        self.__background_hover_color = Constants.WOODEN.get_summed(Color(50,50,50))

        self.__current_background_color = self.__background_color

        self.__hover_transition_speed_scale = 0.01

        self.border_color = 0

        self.__background_image = None
        self.__background_clip = None

        self.__image_on_top = False
        self.centralize_text()
        self.update_surface()

    def set_pos( self, pos:Pos):
        self.get_rect().reset_pos(pos.x,pos.y)

    def get_rect( self ):
        return self.__rect

    def get_pos( self ):
        return self.__rect.get_pos()

    def get_size( self ):
        return self.__rect.get_pos()

    def get_width( self ):
        return self.get_rect().get_size().x

    def get_height( self ):
        return self.get_rect().get_size().y

    def reset_color( self ,color:Color=None,hover_color:Color=None):
        if color is None: color = Color(0,0,0)
        if hover_color is None: hover_color = Color(0,0,0)

        self.__background_color = color
        self.__background_hover_color = hover_color

        return self

    def reset_hover_transition( self , speed_scale:float = 0.1 ):
        self.__hover_transition_speed_scale = speed_scale

    def set_background_image( self , sprite:Sprite):
        self.__background_clip = None
        self.__background_image = sprite


    def set_background_clip( self , msprite:MSprite ):
        self.__background_image = None
        self.__background_clip = msprite


    def centralize_text( self ):
        self.__text_pos = self.__rect.get_size().get_transformed_pos(mult=0.5).join(
            self.__text_holder.get_size().get_transformed_pos(mult=-0.5)
        )


    def update_surface( self ):
        self.__surface.fill(self.__current_background_color.get_tuple())
        self.__text_holder.render(self.__surface,self.__text_pos)


    def check_events( self ):
        pass

    def render( self , surface:pg.surface.Surface , render_pos:Pos=None):
        if render_pos is None: render_pos = self.__rect.get_pos()

        surface.blit(self.__surface,render_pos.get_tuple())


