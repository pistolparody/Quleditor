import pygame as pg
from pygame.locals import *

import time

from Asset import Asset
from Structures.Rect import Rect
from Structures.Pos import Pos
from Structures import Constants as c
from Structures.Constants import ColorTemplate as ct

from Structures.Enumerator import Enumerator


class AssetGroup :

    def __init__( self, surface_rect: Rect ) :
        self.name = "Default"
        self.surface_rect = surface_rect
        self.assets: list[Asset] = []
        self.surface = pg.surface.Surface(surface_rect.get_size()).convert_alpha()
        self.background_color = ct.DARK_BLUE.copy().set_alpha(int(0.5 * 255))

        self.asset_background_color = ct.GRAY
        self.asset_background_hover_color = ct.P1_YELLOW
        self.asset_selection_color = ct.WOODEN

        self.asset_max_size = Pos(100, 100)
        self.asset_padding_left = 10
        self.asset_padding_right = 10
        self.asset_padding_top = 10
        self.asset_padding_bottom = 10
        self.mouse_pos = Pos(-1, -1)

        self.pressed_mouse_keys = []
        self.held_mouse_keys = []

        self.padded_size = self.asset_max_size.copy().join(
            Pos(self.asset_padding_left + self.asset_padding_right,
                self.asset_padding_bottom + self.asset_padding_top))

        self.hover_action_updated = False
        self.new_selection = False

        self.last_hovering_data = []
        self.hovered_index = None
        self.selected_index = None
        self.selected_asset: Asset = None


    def update_assets( self, asset_list: list[Asset] ) :
        self.assets = asset_list
        self.update_surface()


    def unselect( self ) :
        if self.selected_asset is not None :
            self.selected_asset.is_selected = False


    def update_surface( self ) :
        max_height = self.padded_size.y
        blit_point = Pos(0, 0)
        for _ in self.assets :
            if blit_point.x + self.padded_size.x > self.surface_rect.width :
                blit_point.reset(0, blit_point.y + self.padded_size.y)

            blit_point.x += self.padded_size.x

        self.surface_rect.height = max_height + blit_point.y

        self.surface = pg.surface.Surface(self.surface_rect.get_size()).convert_alpha()

        self.surface.fill(self.background_color)
        blit_point = Pos(0, 0)
        for i in self.assets :
            i.background_color = self.asset_background_color
            i.background_hover_color = self.asset_background_hover_color
            i.background_selection_color = self.asset_selection_color

            i.should_render_debug = True
            i.set_max_size(self.asset_max_size.copy())
            i.set_padding(self.asset_padding_left, self.asset_padding_right,
                self.asset_padding_bottom, self.asset_padding_top)
            i.transform_sprite()
            padded_size = i.get_padded_size()

            if blit_point.x + padded_size.x > self.surface_rect.width :
                blit_point.reset(0, blit_point.y + padded_size.y)

            i.rect.reset_pos(blit_point.x, blit_point.y)

            i.render(self.surface)
            blit_point.x += padded_size.x


    def set_color_data( self, bg_color: Color, asset_bg_color: Color, asset_hover_color: Color,
            selection_color: Color ) :

        self.background_color = bg_color
        self.asset_background_color = asset_bg_color
        self.asset_background_hover_color = asset_hover_color
        self.asset_selection_color = selection_color

    def set_mouse_data( self, mouse_pos: Pos, pressed_mouse_keys: list, held_mouse_keys: list ) :
        self.mouse_pos = mouse_pos
        self.pressed_mouse_keys = pressed_mouse_keys
        self.held_mouse_keys = held_mouse_keys


    def get_events( self, event_list: list = None ) :
        pass


    def check_events( self ) :
        hovering_data = []
        self.hover_action_updated = False

        self.new_selection = False
        if self.surface_rect.collidepoint(self.mouse_pos) :
            counter = 0
            for i in self.assets :
                i.is_hovering = i.rect.collidepoint(self.mouse_pos)
                if i.is_hovering :
                    self.hovered_index = counter
                hovering_data.append(i.is_hovering)
                counter += 1

            if hovering_data != self.last_hovering_data :
                self.update_surface()
                self.hover_action_updated = True

            self.last_hovering_data = hovering_data

            if self.hovered_index is not None and c.MOUSE_LEFT in self.pressed_mouse_keys :
                if self.selected_asset is not None :
                    self.selected_asset.is_selected = False
                self.selected_index = self.hovered_index
                self.selected_asset = self.assets[self.selected_index]
                self.new_selection = True
                self.selected_asset.is_selected = True  # print(self.name, self.assets[self.selected_index].name, time.time())

        else :
            for i in self.assets :
                i.is_hovering = False

            if hovering_data != self.last_hovering_data :
                self.last_hovering_data = hovering_data
                self.update_surface()
                self.hover_action_updated = True


    def render( self, surface: pg.surface.Surface ) :
        surface.blit(self.surface, self.surface_rect.get_pos())
