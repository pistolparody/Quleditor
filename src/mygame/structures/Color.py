from pygame.color import Color as pg_color


class Color(pg_color) :

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

    def get_tuple( self ):
        return self.r,self.g,self.b,self.a

    def lerp_me( self,color,amount:float ):
        lerped_me = self.lerp(color,amount)
        self.r,self.g,self.b,self.a = color.get_tuple()

class Constants:
    BLACK = Color(0,0,0)