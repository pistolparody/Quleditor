import pygame as pg

from . import Enumerator


class Color(pg.color.Color):
    def __init__(self,r:int,g:int,b:int,a:int=255):
        super().__init__(r,g,b,a)

    def get_tuple( self ) :
        return self.r, self.g, self.b, self.a


    def copy( self ) :
        return Color( self.r, self.g, self.b, self.a )


    def reset( self, r: int, g: int, b: int, a: int ) :
        self.r, self.g, self.b, self.a = r, g, b, a
        return self


    def set_alpha( self, alpha: int ) :
        self.a = alpha


    def join( self, color, scale: float = 1, p_scale: float = None ) :
        if p_scale is None : p_scale = 1 - scale
        if scale < 0 or scale > 1 : raise ValueError( Enumerator.InvalidScale.data )

        color = color.copy()

        self.__transform( p_scale )
        color.__transform( scale )

        self.__join( color )

        return self


    def __join( self, color ) :
        result = self
        result.sum_values( color.__red, color.__green, color.__blue, color.__alpha)

        return result


    def get_joined( self, color, scale: float = 1, p_scale: float = None ) :
        return self.copy().join( color, scale, p_scale )


    def __transform( self, mult: float = 1 ) :
        self.r *= mult
        self.g *= mult
        self.b *= mult

        return self


    def sum( self, color ) :
        return self.sum_values( color.r, color.g, self.b )


    def get_summed( self, color ) :
        return self.copy().sum( color )


    def sum_values( self, r_sum: float = 0, g_sum: float = 0, b_sum: float = 0, a_sum: float = 0) :
        self.r += r_sum
        self.g += g_sum
        self.b += b_sum
        self.a += a_sum



        return self


    def make_negative( self ) :
        self.r *= -1
        self.g *= -1
        self.b *= -1
        self.a *= -1

        return self
