import pygame as pg

from .Pos import Pos

class Rect(pg.rect.Rect):
    @staticmethod
    def fromPos(pos:Pos,size:Pos):
        return Rect(pos.x,pos.y,size.x,size.y)

    def __init__(self,left:float,top:float,width:float,height:float):
        super().__init__(left,top,width,height)

    def copy( self ) :
        return Rect(self.left,self.top,self.width,self.height)

    def get_pos( self ):
        return Pos(self.left,self.top)

    def get_size( self ):
        return Pos( self.width, self.height )


    def transform_pos( self , Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        pos = self.get_pos().get_transformed_pos(Sum, mult, sum_first)
        self.left,self.top = pos.get_tuple()
        return self

    def transform_size( self , Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        size = self.get_size().get_transformed_pos( Sum, mult, sum_first )
        self.width,self.height = size.get_tuple()

        return self


    def reset_pos( self, new_x: float = 0, new_y: float = 0 ) :
        self.top , self.left = new_y , new_x

        return self


    def reset_size( self, new_x: float = 0, new_y: float = 0 ) :
        self.width, self.height = new_x, new_y

        return self


