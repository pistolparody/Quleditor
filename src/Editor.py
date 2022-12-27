import pygame as pg
from pygame.locals import *

import time

from Structures.Pos import Pos
from Structures import Constants as c
from Structures.Rect import Rect
from Structures.Color import Color
from Structures.Functions import safe_image_load
from Asset import Asset
from AssetPanel import AssetPanel
from ScrollView import ScrollView

class Editor :

    def __init__( self, screen_size: Pos ) :
        self.screen_size: Pos = screen_size # reference
        self.background_color = c.WOODEN
        self.should_render_debug = False

        self.last_dropped_files = []

        self.scroll_view = ScrollView(Rect(0,0,screen_size.x*0.7,screen_size.y))

        self.asset_panel = AssetPanel(Rect(0,0,screen_size.x*0.7,screen_size.y))
        self.asset_panel.update_surface()

    def get_events( self, event_list: list ) :

        for i in event_list:
            if i.type == MOUSEWHEEL:
                self.scroll_view.scroll_request.y = i.y
                self.scroll_view.scroll_timer = time.time()



    def load_assets( self ):
        assets = [Asset(surface=i) for i in
            [safe_image_load(i) for i in self.last_dropped_files]
            if i is not None
        ]

        self.asset_panel.update_assets(assets)
        self.scroll_view.content_list=[self.asset_panel.surface]
        self.scroll_view.update_surface(True)


    def check_events( self ) :
        if len(self.last_dropped_files): self.load_assets()

        self.scroll_view.check_events()

    def render_debug( self ,surface: pg.surface.Surface):
        pg.draw.line(surface, c.WHITE, [self.screen_size.x / 2, 0],
            [self.screen_size.x / 2, self.screen_size.y])

        pg.draw.line(surface, c.WHITE, [self.screen_size.x, self.screen_size.y / 2],
            [0, self.screen_size.y / 2])

    def render( self, surface: pg.surface.Surface ) :
        surface.fill(self.background_color)

        self.scroll_view.render(surface)

        if self.should_render_debug: self.render_debug(surface)


