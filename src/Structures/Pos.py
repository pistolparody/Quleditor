from pygame.math import Vector2

class Pos(Vector2) :
    @staticmethod
    def fromTuple(pos:tuple[float,float]):
        return Pos(pos[0],pos[1])

    def __init__( self, x: float, y: float ) :
        super().__init__(x,y)


    def __str__( self ) :
        return "[PosObject : ({},{})]".format( self.x, self.y )

    def copy( self ) :
        return Pos( self.x, self.y )

    def reset( self, new_x: float = 0, new_y: float = 0 ) :
        self.x, self.y = new_x, new_y

        return self

    def reset_by_tuple( self, pos: tuple[float, float] ) :
        self.x, self.y = pos
        return self

    def get_tuple( self ) :
        return self.x, self.y

    def mult_transform( self ,x_mult:float = 1,y_mult:float=1):
        self.x,self.y = self.x * x_mult , self.y * y_mult
        return self

    def get_mult_transform( self ):
        return self.copy().mult_transform()

    def transform( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        if not sum_first :
            self.x *= mult
            self.x += Sum
            self.y *= mult
            self.y += Sum
        else :
            self.x += Sum
            self.x *= mult
            self.y += Sum
            self.y *= mult

        return self


    def get_transformed_pos( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return self.copy().transform( Sum, mult, sum_first )

    def get_transformed_tuple( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return self.copy().transform( Sum, mult, sum_first ).get_tuple()

    def join( self, pos ) :
        return Pos( self.x + pos.x, self.y + pos.y )