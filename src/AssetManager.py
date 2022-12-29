import pygame as pg
from pygame.locals import *

import os
import time

from Structures.Pos import Pos
from Structures import Constants as c
from Structures.Rect import Rect
from Structures.Color import Color
from Structures.Functions import safe_image_load
from Asset import Asset
from AssetGroup import AssetGroup
from ScrollView import ScrollView


class AssetManager :

    def __init__( self, screen_size: Pos ) :
        self.screen_size: Pos = screen_size  # reference
        self.background_color = c.WOODEN
        self.should_render_debug = False

        self.mouse_pos = Pos(0, 0)

        self.pressed_mouse_keys = []
        self.held_mouse_keys = []

        target_folder = '/home/yolo/Workstation/Assets/Small Forest Asset Pack/All/'
        self.last_dropped_files = [target_folder + "/" + i for i in os.listdir(target_folder)]

        self.scroll_view = ScrollView(Rect(0, 0, screen_size.x * 0.7, screen_size.y))

        self.asset_group = AssetGroup(Rect(0, 0, screen_size.x * 0.7, screen_size.y))
        self.asset_group.update_surface()
        self.load_assets()


    def set_mouse_data( self, mouse_pos: Pos, pressed_mouse_keys: list, held_mouse_keys: list ) :
        self.mouse_pos = mouse_pos
        self.pressed_mouse_keys = pressed_mouse_keys
        self.held_mouse_keys = held_mouse_keys

        self.asset_group.set_mouse_data(
            mouse_pos.copy().join(self.scroll_view.scroll_rel.get_flipped()), pressed_mouse_keys,
            held_mouse_keys)


    def get_events( self, event_list: list = None ) :
        if event_list is None : event_list = []

        self.asset_group.get_events(event_list=event_list)

        for i in event_list :
            if i.type == MOUSEWHEEL :
                self.scroll_view.scroll_request.y = i.y
                self.scroll_view.scroll_timer = time.time()


    def load_assets( self ) :
        assets = [Asset(surface=i[0], path=i[1]) for i in
            [(safe_image_load(i), i) for i in self.last_dropped_files] if i[0] is not None]

        self.asset_group.update_assets(assets)

        self.scroll_view.content_list = [self.asset_group.surface]
        self.scroll_view.update_surface(True)


    def check_events( self ) :
        if len(self.last_dropped_files) :
            self.load_assets()
            self.last_dropped_files.clear()

        if self.scroll_view.scroll_request.is_origin():
            self.asset_group.check_events()

        if self.asset_group.was_updated:
            self.scroll_view.content_list = [self.asset_group.surface]
            self.scroll_view.update_surface(False)

        self.scroll_view.check_events()


    def render_debug( self, surface: pg.surface.Surface ) :
        pg.draw.line(surface, c.WHITE, [self.screen_size.x / 2, 0],
            [self.screen_size.x / 2, self.screen_size.y])

        pg.draw.line(surface, c.WHITE, [self.screen_size.x, self.screen_size.y / 2],
            [0, self.screen_size.y / 2])


    def render( self, surface: pg.surface.Surface ) :
        surface.fill(self.background_color)
        # self.asset_panel.render(surface)

        self.scroll_view.render(surface)

        if self.should_render_debug : self.render_debug(surface)
