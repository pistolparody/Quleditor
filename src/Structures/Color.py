import pygame as pg

from typing import Union,Literal

import random
from . import Enumerator


class Color(pg.color.Color):

    @staticmethod
    def randomColor():
        return Color(container=[random.randint(0,255) for _ in range(3)])

    @staticmethod
    def swap_colors(color,other_color):
        color.r,other_color.r = other_color.r,color.r
        color.g,other_color.g = other_color.g,color.g
        color.b,other_color.b = other_color.b,color.b
        color.a,other_color.a = other_color.a,color.a


    def __init__(self,r:int=0,g:int=0,b:int=0,a:int=255,text:str=None,container:list[int]=None):
        if container is not None: super().__init__(container) ;return
        if text is not None: super().__init__(text) ;return
        super().__init__(r,g,b,a)

    def lerp_me(self, color, amount: float):
        self.reset(color=self.lerp(color,amount))
        return self

    def swap_color( self,color ):
        self.r, color.r = color.r,self.r
        self.g, color.g = color.g,self.g
        self.b, color.b = color.b,self.b
        self.a, color.a = color.a,self.a

        return self


    def swap_max( self ,
            swap_target: Literal['r','g','b']):
        """ swap the bits that are not max """
        if swap_target not in 'rgb': raise ValueError("BadInput")

        Max = 'r'
        container = [self.r,self.g,self.b]
        for name, value in zip('rgb',container):
            if value == max(container):
                Max = name
                break

        med = getattr(self,Max)
        setattr(self,Max,getattr(self,swap_target))
        setattr(self,swap_target,med)

        return self


    def flip( self, center: str ) :
        if center == "r" :
            self.g, self.b = self.b, self.g
        elif center == "g" :
            self.g, self.b = self.b, self.g
        elif center == "b" :
            self.r, self.g = self.g, self.r
        else :
            raise ValueError("BadInput")


    # Max = max('rgb', key=lambda x : getattr(self, x))

    # def flip( self, center: str ) :
    #     """ swap the bits that are not center """
    #     if center not in 'rgb': raise ValueError("BadInput")
    #
    #     (a, b), d = set('rgb') - {center}, self.__dict__
    #     d[a], d[b] = d[b], d[a]




    def get_tuple( self ) :
        return self.r, self.g, self.b, self.a


    def copy( self ) :
        return Color( self.r, self.g, self.b, self.a )


    def reset( self, r: int=0, g: int=0, b: int=0, a: int=255,color=None ) :
        if color is not None:
            self.r,self.g,self.b,self.a = color.r,color.g,color.b,color.a
            return self

        self.r, self.g, self.b, self.a = r, g, b, a
        return self


    def set_alpha( self, alpha: int ) :
        self.a = alpha
        return self


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
