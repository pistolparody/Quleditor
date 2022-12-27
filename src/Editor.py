import pygame as pg
from pygame.locals import *

from Structures.Pos import Pos
from Structures import Constants as c
from Structures.Color import Color
from Structures.Functions import safe_image_load
from Asset import Asset


class Editor :

    def __init__( self, screen_size: Pos ) :
        self.screen_size: Pos = screen_size # reference
        self.background_color = c.WOODEN
        self.should_render_debug = False

        self.last_dropped_files = []
        self.assets:list[Asset] = []
        self.assets_surface:pg.surface.Surface = None

    def get_events( self, event_list: list ) :
        for i in event_list :
            if i.type == DROPFILE:
                pass


    def load_assets( self ):
        self.assets = [Asset(surface=i) for i in
            [safe_image_load(i) for i in self.last_dropped_files]
            if i is not None
        ]

        self.assets_surface = pg.surface.Surface(
            self.screen_size.get_transformed_pos(mult=0.5)
        ).convert_alpha()

        self.assets_surface.fill(c.GLASS)
        for i in self.assets:
            i.set_max_size(Pos(50,50))
            i.transform_sprite()

        blit_pos = Pos(0,0)
        for i in self.assets:
            if blit_pos.x + i.get_width() > self.assets_surface.get_width():
                blit_pos.reset(0,blit_pos.y+i.get_height())

            i.render(self.assets_surface,top_left=blit_pos)
            blit_pos.x += i.get_width()

    def check_events( self ) :
        if len(self.last_dropped_files): self.load_assets()

    def render_debug( self ,surface: pg.surface.Surface):
        pg.draw.line(surface, c.WHITE, [self.screen_size.x / 2, 0],
            [self.screen_size.x / 2, self.screen_size.y])

        pg.draw.line(surface, c.WHITE, [self.screen_size.x, self.screen_size.y / 2],
            [0, self.screen_size.y / 2])

    def render( self, surface: pg.surface.Surface ) :
        surface.fill(self.background_color)

        if self.assets_surface is not None:
            surface.blit(self.assets_surface,[0,0])

        if self.should_render_debug: self.render_debug(surface)


