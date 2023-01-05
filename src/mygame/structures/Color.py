from pygame.color import Color as pg_color
from random import randint

class Color(pg_color) :
    @staticmethod
    def randomColor(include_alpha:bool=False):
        alpha = 255
        if include_alpha: alpha = randint(0,255)
        return Color(randint(0,255),randint(0,255),randint(0,255),alpha)



    def __init__( self, r: int = None, g: int = None, b: int = None, a: int = None, color=None ) :
        if r is None : r = 0
        if g is None : g = 0
        if b is None : b = 0
        if a is None : a = 255

        if color is not None :
            super().__init__(color)
            return

        super().__init__(r, g, b, a)

    def copy( self ):
        return Color(color=self)

    def swap( self, color ) :
        self.r,color.r = color.r,self.r
        self.g,color.g = color.g,self.g
        self.b,color.b = color.b,self.b
        self.a,color.a = color.a,self.a

        return self

    @property
    def as_tuple( self ):
        return self.r,self.g,self.b,self.a

    def lerp_me( self,color,amount:float ):
        lerped_me = self.lerp(color,amount)
        self.r,self.g,self.b,self.a = lerped_me

        return self

class ColorConstants:
    BLACK = Color(0,0,0)
    WHITE = Color(255,255,255)
    GLASS = Color(0,0,0,0)

    RED = Color(255,0,0)
    GREEN = Color(0,255,0)
    BLUE = Color(0,0,255)

    DEAD_BLUE = Color(150, 150, 220)
    HOT_RED = Color(70, 30, 30)
    HAPPY_BLUE = Color(35, 35, 93)
    GRAY_SKY = Color(180, 180, 195)

