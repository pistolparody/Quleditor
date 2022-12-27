import pygame as pg
import time

from .Pos import Pos
from .Sprite import Sprite


class MSprite :

    def __init__( self, sprite_list: list[Sprite] = None, animation_interval: float = 0.1 ) :
        if sprite_list is None : sprite_list = []

        self.__sprite_list = sprite_list
        self.__active_sprite_index = 0

        self.__animation_interval = animation_interval
        self.__last_tick_time = 0

        self.auto_transform = False
        self.__x_flip = False
        self.__y_flip = False
        self.__angle = 0
        self.__scale = None


    def add_sprite( self , sprite:Sprite ):
        if self.auto_transform :
            sprite.reset_flips( self.__x_flip, self.__y_flip )
            sprite.reset_angle( self.__angle )
            sprite.reset_scale( self.__scale )

            sprite.transform_image()

        self.__sprite_list.append(sprite)


    def insert_sprite( self , sprite:Sprite , index:int = 0 ):
        if self.auto_transform:
            sprite.reset_flips( self.__x_flip, self.__y_flip )
            sprite.reset_angle( self.__angle )
            sprite.reset_scale( self.__scale )

            sprite.transform_image()

        self.__sprite_list.insert(index,sprite)

    def get_flips( self ) :
        return self.__x_flip, self.__y_flip


    def get_angle( self ) :
        return self.__angle


    def get_scale( self ) :
        return self.__scale

    def get_sprite_list( self ):
        return self.__sprite_list

    def reset_flips( self, x_flip: bool = False, y_flip: bool = False ) :
        self.__x_flip, self.__y_flip = x_flip, y_flip

        for i in self.__sprite_list :
            i.reset_flips( self.__x_flip, self.__y_flip )

        if self.auto_transform :
            self.transform_images()

        return self


    def reset_angle( self, angle: float = 0 ) :
        self.__angle = angle

        for i in self.__sprite_list :
            i.reset_angle( self.__angle )

        if self.auto_transform :
            self.transform_images()

        return self


    def reset_scale( self, scale: Pos = None ) :
        self.__scale = scale

        for i in self.__sprite_list :
            i.reset_scale( self.__scale )

        if self.auto_transform : self.transform_images()

        return self


    def transform_images( self ) :
        for i in self.__sprite_list :
            i.transform_image()


    def check_events( self ) :
        current_time = time.time()

        if current_time  > self.__last_tick_time + self.__animation_interval:

            self.__last_tick_time = current_time
            self.tick()



    def render( self, surface: pg.surface.Surface , center:Pos) :
        self.__sprite_list[self.__active_sprite_index].render(surface,center)


    def tick( self ) :
        self.__active_sprite_index += 1
        if self.__active_sprite_index > len( self.__sprite_list ) - 1 :
            self.__active_sprite_index = 0

