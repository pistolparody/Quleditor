import pygame as pg
from pygame.locals import *

import os
import time

from Structures.Pos import Pos
from Structures import Constants as c
from Structures.Constants import ColorTemplate as ct
from Structures.Rect import Rect
from Structures.Color import Color
from Structures.Functions import safe_image_load
from Asset import Asset
from AssetGroup import AssetGroup
from ScrollView import ScrollView


class AssetManager :

    def __init__( self, screen_size: Pos ) :
        self.screen_size: Pos = screen_size  # reference
        self.background_color = ct.WOODEN
        self.should_render_debug = False

        self.mouse_pos = Pos(0, 0)
        self.asset_max_size = Pos(50, 50)

        self.asset_group_list: list[AssetGroup] = []
        self.asset_group_limit = 10

        self.pressed_mouse_keys = []
        self.held_mouse_keys = []

        target_folder = '/home/yolo/Workstation/Assets/Small Forest Asset Pack/All/'
        self.last_dropped_files = []

        self.scroll_view = ScrollView(Rect(0, 0, screen_size.x * 0.7, screen_size.y))
        self.scroll_view.background_color = ct.GRAY
        self.load_assets()


    def set_mouse_data( self, mouse_pos: Pos, pressed_mouse_keys: list, held_mouse_keys: list ) :
        self.mouse_pos = mouse_pos
        self.pressed_mouse_keys = pressed_mouse_keys
        self.held_mouse_keys = held_mouse_keys

        counter = 0
        for i in self.asset_group_list:
            m_pos = self.mouse_pos.copy().join(self.scroll_view.scroll_rel.get_flipped())
            m_pos.y -= self.scroll_view.get_content_height(counter)
            i.set_mouse_data(m_pos, pressed_mouse_keys, held_mouse_keys)
            counter+=1

        # if self.asset_group_list.__len__()>1:
        #     print(self.asset_group_list[0].mouse_pos)


    def receive_dropped_files( self, dropped_files: list[str] ) :
        group_count = len(dropped_files) // self.asset_group_limit + 1
        self.last_dropped_files.clear()
        for i in range(group_count) :
            group_files = dropped_files[
            i * self.asset_group_limit :(i + 1) * self.asset_group_limit]
            self.last_dropped_files.append(group_files)

        self.load_assets()


    def get_events( self, event_list: list = None ) :
        if event_list is None : event_list = []

        # self.asset_group.get_events(event_list=event_list)

        if len(self.pressed_mouse_keys) : self.scroll_view.scroll_request.reset()

        for i in event_list :
            if i.type == MOUSEWHEEL :
                self.scroll_view.scroll_request.y = i.y
                self.scroll_view.scroll_timer = time.time()


    def load_assets( self ) :


        self.asset_group_list.clear()

        counter = 0
        for i in self.last_dropped_files :
            temp = [Asset(path=j) for j in i]
            for j in temp :
                j.set_max_size(self.asset_max_size)

            color = Color.randomColor().lerp(ct.BLACK, 0.7)
            self.asset_group_list.append(
                AssetGroup(Rect.fromPos(Pos(0, 0), self.scroll_view.rect.get_size())))

            self.asset_group_list[-1].background_color = color
            self.asset_group_list[-1].name = str(counter)
            self.asset_group_list[-1].set_color_data(
                ct.P1_MINT.copy().lerp(Color.randomColor(),0.25),
                ct.P1_PEACH,
                ct.P1_YELLOW)
            self.asset_group_list[-1].update_assets(temp)

            counter += 1

        self.scroll_view.content_list = [i.surface for i in self.asset_group_list]

        self.scroll_view.update_surface(True)


    def check_events( self ) :


        if self.scroll_view.scroll_request.is_origin():
            for i in self.asset_group_list :
                i.check_events()

            self.scroll_view.content_list = [i.surface for i in self.asset_group_list]
            self.scroll_view.update_surface(False)

        self.scroll_view.check_events()


    def render_debug( self, surface: pg.surface.Surface ) :
        pg.draw.line(surface, ct.WHITE, [self.screen_size.x / 2, 0],
            [self.screen_size.x / 2, self.screen_size.y])

        pg.draw.line(surface, ct.WHITE, [self.screen_size.x, self.screen_size.y / 2],
            [0, self.screen_size.y / 2])


    def render( self, surface: pg.surface.Surface ) :
        surface.fill(self.background_color)
        # self.asset_panel.render(surface)


        self.scroll_view.render(surface)

        if self.should_render_debug : self.render_debug(surface)
