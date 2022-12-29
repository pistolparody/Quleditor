import pygame as pg
from pygame.locals import *

import time

from Asset import Asset
from Structures.Rect import Rect
from Structures.Pos import Pos
from Structures import Constants as c
from Structures.Enumerator import Enumerator

class AssetGroup :

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
        self.mouse_pos = Pos(0, 0)

        self.padded_size = self.asset_max_size.copy().join(
            Pos(self.asset_padding_left + self.asset_padding_right,
                self.asset_padding_bottom + self.asset_padding_top))

        self.was_updated = False

        self.last_hovering_data = []
        self.selected_index = None
        self.held_keys = []


    def update_assets( self, asset_list: list[Asset] ) :
        self.assets = asset_list

        self.update_surface()


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


    def get_events( self, event_list: list = None, mouse_pos: Pos = None ) :
        if mouse_pos is not None : self.mouse_pos.reset(mouse_pos.x, mouse_pos.y)
        mouse_presses = pg.mouse.get_pressed()
        self.held_keys.clear()

        if event_list is not None :

            for i in event_list :

                if i.type == MOUSEBUTTONDOWN :
                    for d in zip(c.MOUSE_KEYS.data, mouse_presses) :
                        if d[1] :
                            if d[0] not in self.held_keys :
                                self.held_keys.append(d[0])

                elif i.type == MOUSEBUTTONUP :
                    for d in zip(c.MOUSE_KEYS.data, mouse_presses) :
                        if not d[1] :
                            if d[0] in self.held_keys :
                                self.held_keys.remove(d[0])


    def check_events( self ) :
        hovering_data = []
        self.was_updated = False

        if self.selected_index is not None and c.MOUSE_LEFT in self.held_keys:
            print(self.assets[self.selected_index].name,time.time())

        if self.surface_rect.collidepoint(self.mouse_pos) :
            counter = 0
            for i in self.assets :
                i.is_hovering = i.rect.collidepoint(self.mouse_pos)
                if i.is_hovering:
                    self.selected_index = counter
                hovering_data.append(i.is_hovering)
                counter += 1

            if hovering_data != self.last_hovering_data :
                self.update_surface()
                self.was_updated = True

            self.last_hovering_data = hovering_data

        else :
            for i in self.assets :
                i.is_hovering = False

            if hovering_data != self.last_hovering_data :
                self.last_hovering_data = hovering_data
                self.update_surface()
                self.was_updated = True


    def render( self, surface: pg.surface.Surface ) :
        surface.blit(self.surface, self.surface_rect.get_pos())
