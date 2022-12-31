import pygame as pg

class Pos(pg.math.Vector2):
    def __init__( self,x:float=0,y:float=0,pos=None ) -> None :
        if pos is not None:
            super().__init__(pos)
            return

        super().__init__(x,y)

