from pygame.rect import Rect as pg_rect
from .Pos import Pos

class Rect(pg_rect):

    def __init__( self,x:float=0,y:float=0,width:float=0,height:float=0,rect=None ) -> None :
        x,y,width,height = [int(i) for i in [x,y,width,height]]

        if rect is not None:
            super().__init__(rect)
            return

        super().__init__(x,y,width,height)


    def copy( self ):
        return Rect(rect=self)

    def swap( self,rect ):
        self.x,rect.x = rect.x,self.x
        self.y,rect.y = rect.y,self.y
        self.width,rect.width = rect.width,self.width
        self.height,rect.height = rect.height,self.height

        return self

    @property
    def as_tuple( self ):
        return self.x,self.y,self.width,self.height

    def reset( self,rect ):
        self.x,self.y = rect.pos
        self.width,self.height = rect.size
        return self

    def reset_pos( self,x:float=0,y:float=0,pos:Pos=None ):
        x,y = int(x),int(y)

        if pos is not None:
            self.x,self.y = int(pos.x),int(pos.y)
            return self

        self.x,self.y = x,y
        return self


    def transform_pos( self, sum_xy: float = 0, sum_y: float = None, mult_xy: float = 1,
            mult_y: float = None ) :
        copy_cat = self.pos.copy()

        if sum_y is None :
            copy_cat.sum_me(sum_xy, sum_xy)
        else :
            copy_cat.sum_me(sum_xy, sum_y)

        if mult_y is None :
            copy_cat.mult_me(mult_xy, mult_xy)
        else :
            copy_cat.mult_me(mult_xy, mult_y)

        self.reset_pos(pos=copy_cat)

        return self

    def transform_size( self, sum_xy: float = 0, sum_y: float = None, mult_xy: float = 1,
            mult_y: float = None ) :
        copy_cat = self.size.copy()

        if sum_y is None :
            copy_cat.sum_me(sum_xy, sum_xy)
        else :
            copy_cat.sum_me(sum_xy, sum_y)

        if mult_y is None :
            copy_cat.mult_me(mult_xy, mult_xy)
        else :
            copy_cat.mult_me(mult_xy, mult_y)

        self.reset_size(pos=copy_cat)

        return self

    def reset_size( self, x: int = 0, y: int = 0, pos: Pos = None ) :
        x, y = int(x), int(y)
        if pos is not None :
            self.width, self.height = int(pos.x), int(pos.y)
            return self

        self.width, self.height = x, y
        return self

    @property
    def pos( self ) -> Pos:
        return Pos(self.x,self.y)

    @pos.setter
    def pos( self,p_pos:Pos ):
        self.x = int(p_pos.x)
        self.y = int(p_pos.y)

    @property
    def size( self ) -> Pos:
        return Pos(self.width,self.height)

    @size.setter
    def size( self, size: Pos ) :
        self.width = int(size.x)
        self.height = int(size.y)
