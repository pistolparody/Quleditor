from pygame.rect import Rect as pg_rect
from .Pos import Pos

class Rect(pg_rect):

    def __init__( self,x:int=0,y:int=0,width:int=0,height:int=0,rect=None ) -> None :
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

    def get_tuple( self ):
        return self.x,self.y,self.width,self.height

    def reset_pos( self,x:int=0,y:int=0,pos:Pos=None ):
        if pos is not None:
            self.x,self.y = int(pos.x),int(pos.y)
            return

        self.x,self.y = x,y


    def reset_size( self, width: int = 0, height: int = 0, size: Pos = None ) :
        if size is not None :
            self.width, self.height = int(size.x), int(size.y)
            return

        self.width, self.height = width, height

    def get_pos( self ) -> Pos:
        return Pos(self.x,self.y)

    def get_size( self ) -> Pos:
        return Pos(self.width,self.height)
