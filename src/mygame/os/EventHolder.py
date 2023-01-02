import pygame as pg
from pygame.locals import *

from ..structures.Pos import Pos
from ..structures.Enumerator import Enumerator

class EventHolder:
    class Constants:
        Enumerator.reset("EventHolder.Constants")

        ALL_EVENTS = Enumerator.next("ALL_EVENTS")

        MOUSE_POS = Enumerator.next("MOUSE_POS")
        MOUSE_KEYS = Enumerator.next("MOUSE_KEYS")
        KEYBOARD_KEYS = Enumerator.next("KEYBOARD_KEYS")

        WINDOW = Enumerator.next("WINDOW")


    def __init__( self ):

        self.mouse_moved:bool = False
        self.mouse_rel:Pos = Pos(0,0)

        self.mouse_pos:Pos = Pos(-1,-1)
        self.mouse_held_keys:list = []
        self.mouse_pressed_keys:list = []

        self.keyboard_held_keys:list = []
        self.keyboard_pressed_keys:list = []


        self.should_quit:bool = False

        self.window_size_changed:bool = False
        self.window_contains_mouse:bool = False

        self.window_has_focus:bool = False

        self.__listen_list:list[EventHolder.Constants] = []


    def set_listen_list( self,listen_list:list ):
        self.__listen_list = listen_list

    def get_listen_list( self ):
        return self.__listen_list


    def get_events( self,event_list:list[pg.event.Event] ):
        if EventHolder.Constants.MOUSE_POS in self.__listen_list:
            self.mouse_pos = pg.mouse.get_pos()

        for i in event_list:
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
