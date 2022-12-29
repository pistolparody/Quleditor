import pygame as pg
from pygame.locals import *

import time
from Structures.Window import Window
from Structures.Menu import Menu
from Structures.Enumerator import Enumerator
from Structures.Pos import Pos
from Structures import Constants as c
from AssetManager import AssetManager


class Editor :

    def __init__( self, screen_size: Pos ) :
        self.asset_manager = AssetManager(screen_size)
        self.held_mouse_keys = []
        self.pressed_mouse_keys = []
        self.mouse_pos = Pos(0, 0)


    def get_grabbed_files( self, grabbed_files: list ) :
        self.asset_manager.last_dropped_files = grabbed_files


    def get_events( self, event_list: list ) :
        self.mouse_pos.reset_by_tuple(pg.mouse.get_pos())
        mouse_presses = pg.mouse.get_pressed()
        self.pressed_mouse_keys.clear()

        held_mouse_keys = []
        if event_list is not None :
            for i in event_list :
                if i.type == MOUSEBUTTONDOWN :
                    for d in zip(c.MOUSE_KEYS.data, mouse_presses) :
                        if d[1] :
                            if d[0] not in held_mouse_keys :
                                held_mouse_keys.append(d[0])

                elif i.type == MOUSEBUTTONUP :
                    for d in zip(c.MOUSE_KEYS.data, mouse_presses) :
                        if not d[1] :
                            if d[0] in held_mouse_keys :
                                held_mouse_keys.remove(d[0])
                            if d[0] in self.held_mouse_keys :
                                self.held_mouse_keys.remove(d[0])

        if True :
            self.pressed_mouse_keys = [i for i in held_mouse_keys if i not in self.held_mouse_keys]

            self.held_mouse_keys = [i for i in held_mouse_keys if
                                       i not in self.held_mouse_keys] + self.held_mouse_keys

        self.asset_manager.set_mouse_data(self.mouse_pos, self.pressed_mouse_keys,
            self.held_mouse_keys)

        self.asset_manager.get_events(event_list)


    def check_events( self ) :
        self.asset_manager.check_events()


    def render( self, surface: pg.surface.Surface ) :
        self.asset_manager.render(surface)
