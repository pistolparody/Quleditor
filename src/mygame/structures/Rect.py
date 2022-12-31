import pygame as pg
from .Pos import Pos

class Rect(pg.rect.Rect):

    def __init__( self,x:float=0,y:float=0,width:float=0,height:float=0,rect=None ) -> None :
        if rect is not None:
            super().__init__(rect)
            return

        super().__init__(x,y,width,height)




    def get_pos( self ) -> Pos:
        return Pos(self.x,self.y)

    def get_size( self ) -> Pos:
        return Pos(self.width,self.height)

    def reset_pos( self,x:float=0,y:float=0,pos:Pos=None ):
        if pos is not None:
            self.x,self.y = pos.x,pos.y
            return

        self.x,self.y = x,y


    def reset_size( self, width: float = 0, height: float = 0, size: Pos = None ) :
        if size is not None :
            self.width, self.height = size.x, size.y
            return

        self.width, self.height = width, height
