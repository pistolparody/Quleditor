import pygame as pg

class Pos(pg.math.Vector2):
    def __init__( self,x:float=0,y:float=0,pos=None ) -> None :
        if pos is not None:
            super().__init__(pos)
            return

        super().__init__(x,y)

    def reset( self,new_x:float=0,new_y:float=0,pos=None, ):
        if pos is not None:
            self.x,self.y = pos.x,pos.y
            return

        self.x,self.y = new_x,new_y
