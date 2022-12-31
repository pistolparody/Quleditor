from pygame.surface import Surface as pg_surface

from .Pos import Pos
from .Color import Color
from .Constants import Positions as p

class Surface(pg_surface):
    def __init__(self,size:Pos):
        super().__init__(size)

    def glassic_fill( self,color:Color ):
        surface = Surface(Pos(pos=self.get_size()))
        if color.a != 255: surface.convert_alpha()
        surface.fill(color)
        self.blit(surface,p.origin)


