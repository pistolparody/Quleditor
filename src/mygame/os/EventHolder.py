import pygame as pg
from pygame.locals import *

from ..structures.Pos import Pos
from ..structures.Enumerator import Enumerator

class EventHolder:
    class Constants:
        Enumerator.reset("EventHolder.Constants")

        MOUSE_POS = Enumerator.next("MOUSE_POS")
        MOUSE_KEYS = Enumerator.next("MOUSE_KEYS")
        KEYBOARD_KEYS = Enumerator.next("KEYBOARD_KEYS")

        WINDOW = Enumerator.next("WINDOW")

        @staticmethod
        def ALL_EVENTS():
            f = EventHolder.Constants
            return [f.MOUSE_POS, f.MOUSE_KEYS,f.KEYBOARD_KEYS,f.WINDOW]


    def __init__( self ,super_args=None):

        self.mouse_moved:bool = False
        self.mouse_rel:Pos = Pos(0,0)

        self.mouse_pos:Pos = Pos(-1,-1)
        self.mouse_held_keys:list = []
        self.mouse_pressed_keys:list = []
        self.mouse_released_keys:list = []

        self.keyboard_held_keys:list = []
        self.keyboard_pressed_keys:list = []
        self.keyboard_released_keys:list = []

        self.should_quit:bool = False

        self.window_size_changed:bool = False
        self.window_contains_mouse:bool = False

        self.window_has_focus:bool = False

        self.__listen_list:list[EventHolder.Constants] = []

        if super_args is not None:
            super(EventHolder, self).__init__(super_args)

    @property
    def listen_list( self):
        return self.__listen_list

    @listen_list.setter
    def listen_list( self,listen_list:list ):
        self.__listen_list = listen_list


    def get_events( self,event_list:list[pg.event.Event] ):
        if EventHolder.Constants.MOUSE_POS in self.__listen_list:
            self.mouse_pos.reset(as_tuple=pg.mouse.get_pos())

        self.mouse_pressed_keys.clear()
        self.mouse_released_keys.clear()
        self.keyboard_pressed_keys.clear()
        self.keyboard_released_keys.clear()

        for i in event_list:
            if EventHolder.Constants.MOUSE_POS:
                if i.type == MOUSEMOTION:
                    self.mouse_rel.reset(as_tuple=pg.mouse.get_rel())

            if EventHolder.Constants.WINDOW in self.__listen_list:
                if i.type == QUIT:
                    self.should_quit = True
                elif i.type == WINDOWSIZECHANGED:
                    self.window_size_changed = True
                elif i.type == WINDOWENTER:
                    self.window_contains_mouse = True
                elif i.type == WINDOWLEAVE:
                    self.window_contains_mouse = False
                elif i.type == WINDOWFOCUSGAINED:
                    self.window_has_focus = True
                elif i.type == WINDOWFOCUSLOST:
                    self.window_has_focus = False

            if EventHolder.Constants.MOUSE_KEYS:
                if i.type == MOUSEBUTTONDOWN:
                    if i.button not in self.mouse_held_keys:
                        self.mouse_held_keys.append(i.button)
                        self.mouse_pressed_keys.append(i.button)

                if i.type == MOUSEBUTTONDOWN:
                    if i.button in self.mouse_held_keys:
                        self.mouse_held_keys.remove(i.button)
                        self.mouse_released_keys.append(i.button)

            if EventHolder.Constants.KEYBOARD_KEYS:
                if i.type == KEYDOWN:
                    if i.key not in self.keyboard_held_keys:
                        self.keyboard_held_keys.append(i.key)
                        self.keyboard_pressed_keys.append(i.key)

                if i.type == KEYUP:
                    if i.key in self.keyboard_held_keys:
                        self.keyboard_held_keys.remove(i.key)
                        self.keyboard_released_keys.append(i.key)