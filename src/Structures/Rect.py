import pygame as pg

from .Pos import Pos

class Rect(pg.rect.Rect):
    @staticmethod
    def fromPos(pos:Pos,size:Pos):
        return Rect(pos.x,pos.y,size.x,size.y)

    def __init__(self,left:float,top:float,width:float,height:float):
        super().__init__(left,top,width,height)

    def copy( self ) :
        return Rect(self.x,self.y,self.width,self.height)

    def get_pos( self ):
        return Pos(self.x,self.y)

    def get_size( self ):
        return Pos( self.width, self.height )

    def get_center( self ):
        return self.get_size().get_transformed_pos(mult=0.5).join(self.get_pos())


    def transform_pos( self , Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        pos = self.get_pos().get_transformed_pos(Sum, mult, sum_first)
        self.x,self.y = pos.get_tuple()
        return self

    def transform_size( self , Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        size = self.get_size().get_transformed_pos( Sum, mult, sum_first )
        self.width,self.height = size.get_tuple()

        return self


    def reset_pos( self, new_x: float = None, new_y: float = None,should_keep:bool=False) :
        if should_keep:
            if new_x is None : new_x = self.x
            if new_y is None : new_y = self.y

            self.x, self.y = new_x, new_y
        else:
            if new_x is None: new_x = 0
            if new_y is None: new_y = 0

            self.x , self.y = new_x , new_y

        return self


    def reset_size( self, new_x: float = None, new_y: float = None ,should_keep:bool=False) :


        if should_keep:
            if new_x is None : new_x = self.width
            if new_y is None : new_y = self.height

            self.width, self.height = new_x, new_y
        else:
            if new_x is None : new_x = 0
            if new_y is None : new_y = 0

            self.width, self.height = new_x, new_y

        return self



