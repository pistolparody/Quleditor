from pygame.math import Vector2


class Pos(Vector2) :

    def __init__( self, x: float = 0, y: float = 0, pos=None,as_tuple=None ) -> None :
        if as_tuple is not None:
            super(Pos, self).__init__(as_tuple)
            return

        if pos is not None :
            super().__init__(pos)
            return

        super().__init__(x, y)


    def copy( self ) :
        return Pos(pos=self)

    def swap( self,pos ):
        self.x,pos.x = pos.x,self.x
        self.y,pos.y = pos.y,self.y

        return self

    @property
    def as_tuple( self ):
        return self.x,self.y

    def reset( self, new_x: float = 0, new_y: float = 0, pos=None,as_tuple=None ) :
        if as_tuple is not None :
            self.x,self.y = as_tuple[0],as_tuple[1]
            return

        if pos is not None :
            self.x, self.y = pos.x, pos.y
            return

        self.x, self.y = new_x, new_y


    def lerp_me( self, pos, amount: float ) :
        lerped = self.lerp(pos, amount)
        self.x, self.y = lerped.x, lerped.y


    def join( self, pos ) :
        copy_cat = self.copy()
        copy_cat.x += pos.x
        copy_cat.y += pos.y

        return copy_cat


    def join_me( self, pos ) :
        self.x += pos.x
        self.y += pos.y

        return self


    def sum( self, sum_x: float = 0, sum_y: float = 0 ) :
        copy_cat = self.copy()
        copy_cat.x += sum_x
        copy_cat.y += sum_y

        return copy_cat


    def sum_me( self, sum_x: float = 0, sum_y: float = 0 ) :
        self.x += sum_x
        self.y += sum_y

        return self


    def mult( self, x_mult: float = 1, y_mult: float = 1, pos=None ) :
        copy_cat = self.copy()
        if pos is not None :
            copy_cat.x *= pos.x
            copy_cat.y *= pos.y
            return copy_cat

        copy_cat.x, copy_cat.y = copy_cat.x * x_mult, copy_cat.y * y_mult
        return copy_cat


    def mult_me( self, x_mult: float = 1, y_mult: float = 1, pos=None ) :
        if pos is not None :
            self.x *= pos.x
            self.y *= pos.y
            return self

        self.x, self.y = self.x * x_mult, self.y * y_mult
        return self


    def transform_me( self, sum_xy: float = 0, sum_y: float = None, mult_xy: float = 1,
            mult_y: float = None ) :

        if sum_y is None:
            self.sum_me(sum_xy,sum_xy)
        else:
            self.sum_me(sum_xy,sum_y)

        if mult_y is None:
            self.mult_me(mult_xy,mult_xy)
        else:
            self.mult_me(mult_xy,mult_y)

        return self

    def transform( self, sum_xy: float = 0, sum_y: float = None, mult_xy: float = 1,
            mult_y: float = None ) :

        copy_cat = self.copy()

        if sum_y is None :
            copy_cat.sum_me(sum_xy, sum_xy)
        else :
            copy_cat.sum_me(sum_xy, sum_y)

        if mult_y is None :
            copy_cat.mult_me(mult_xy, mult_xy)
        else :
            copy_cat.mult_me(mult_xy, mult_y)

        return copy_cat


    def flip( self, center=None ) :
        if center is None : center = Pos(0, 0)

        copy_cat = self.copy()
        copy_cat.x = center.x * 2 - copy_cat.x
        copy_cat.y = center.y * 2 - copy_cat.y

        return copy_cat


    def flip_me( self, center=None ) :
        if center is None : center = Pos(0, 0)
        self.x = center.x * 2 - self.x
        self.y = center.y * 2 - self.y

        return self

    def reverse( self ):
        copy_cat = self.copy()
        copy_cat.x,copy_cat.y = copy_cat.y,copy_cat.x
        return copy_cat

    def reverse_me( self ):
        self.x,self.y = self.y,self.x
        return self

