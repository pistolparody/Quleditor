import pygame as pg

from Asset import Asset
from Structures.Rect import Rect
from Structures.Pos import Pos
from Structures import Constants as c


class AssetPanel :

    def __init__( self, surface_rect: Rect ) :
        self.surface_rect = surface_rect
        self.assets: list[Asset] = []
        self.surface = pg.surface.Surface(surface_rect.get_size()).convert_alpha()
        self.background_color = c.DARK_BLUE.copy().set_alpha(int(0.5 * 255))
        self.asset_max_size = Pos(100, 100)
        self.asset_padding_left = 10
        self.asset_padding_right = 10
        self.asset_padding_top = 10
        self.asset_padding_bottom = 10


    def update_assets( self, asset_list: list[Asset] ) :
        self.assets = asset_list

        self.update_surface()


    def update_surface( self ) :
        self.surface.fill(self.background_color)
        blit_point = Pos(0, 0)
        for i in self.assets :
            i.should_render_debug = True
            i.set_max_size(self.asset_max_size.copy())
            i.set_padding(self.asset_padding_left, self.asset_padding_right,
                            self.asset_padding_bottom, self.asset_padding_top)
            i.transform_sprite()
            padded_size = i.get_padded_size()

            if blit_point.x + padded_size.x > self.surface_rect.width :
                blit_point.reset(0, blit_point.y + padded_size.y)

            i.render(self.surface, blit_point)
            blit_point.x += padded_size.x


    def get_events( self ) :
        pass


    def check_events( self ) :
        pass


    def render( self, surface: pg.surface.Surface ) :
        surface.blit(self.surface, self.surface_rect.get_pos())
