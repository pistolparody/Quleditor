import pygame as pg
from .Pos import Pos


class Sprite :

    def __init__( self, path: str = None, surface: pg.surface.Surface = None ) :
        self.path = path
        if path is None :
            self.__raw_image = surface
        else :
            self.__raw_image = pg.image.load( path )

        self.auto_transform = False

        self.__x_flip = False
        self.__y_flip = False
        self.__angle = 0
        self.__scale = Pos( 1, 1 )

        self.__transformed_image = self.__raw_image
        self.transform_image()


    def reload( self, path: str = None, surface: pg.surface.Surface = None ) :
        self.path = path
        if path is None :
            self.__raw_image = surface
        else :
            self.__raw_image = pg.image.load( path )

        self.transform_image()


    def get_raw_image( self ) :
        return self.__raw_image


    def get_raw_size( self ) :
        return Pos.fromTuple( self.__raw_image.get_size() )


    def get_transformed_size( self ) :
        return Pos.fromTuple( self.__transformed_image.get_size() )


    def get_transformed_image( self ) :
        return self.__transformed_image


    def get_flips( self ) :
        return self.__x_flip, self.__y_flip


    def get_angle( self ) :
        return self.__angle


    def get_scale( self ) :
        return self.__scale


    def reset_flips( self, x_flip: bool = False, y_flip: bool = False ) :
        self.__x_flip, self.__y_flip = x_flip, y_flip
        if self.auto_transform : self.transform_image()

        return self


    def reset_angle( self, angle: float = 0 ) :
        self.__angle = angle
        if self.auto_transform : self.transform_image()

        return self


    def reset_scale( self, scale: Pos = None ) :
        if scale is None :
            self.__scale.reset( 1, 1 )
        else :
            self.__scale = scale

        if self.auto_transform : self.transform_image()

        return self


    def transform_image( self ) :
        self.__transformed_image = self.__raw_image
        if any( [self.__x_flip, self.__y_flip] ) :
            self.__transformed_image = pg.transform.flip( self.__transformed_image, self.__x_flip,
                self.__y_flip )

        if self.__angle != 0 :
            self.__transformed_image = pg.transform.rotate( self.__transformed_image, self.__angle )

        self.__transformed_image = pg.transform.scale( self.__transformed_image,
            Pos.fromTuple( self.get_raw_image().get_size() ).mult_transform( self.__scale.x,
                self.__scale.y ).get_tuple() )

        return self


    def render( self, surface: pg.surface.Surface, center: Pos ) :
        surface.blit( self.__transformed_image,
            center.join( self.get_transformed_size().get_transformed_pos( mult=-0.5 ) ).get_tuple() )
