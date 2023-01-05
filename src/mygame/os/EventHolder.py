import pygame as pg
from pygame.locals import *

from ..structures.Pos import Pos
from ..structures.Enumerator import Enumerator


class EventConstants :
    Enumerator.reset("EventHolder.Constants")

    MOUSE_POS = Enumerator.next("MOUSE_POS")
    MOUSE_KEYS = Enumerator.next("MOUSE_KEYS")
    KEYBOARD_KEYS = Enumerator.next("KEYBOARD_KEYS")

    WINDOW = Enumerator.next("WINDOW")


    @staticmethod
    def ALL_EVENTS() :
        f = EventConstants
        return [f.MOUSE_POS, f.MOUSE_KEYS, f.KEYBOARD_KEYS, f.WINDOW]

class EventHolder:
    def __init__( self ,super_args=None):

        self.__mouse_moved:bool = False
        self.__mouse_rel:Pos = Pos(0,0)

        self.__mouse_pos:Pos = Pos(-1,-1)
        self.__mouse_held_keys:list = []
        self.__mouse_pressed_keys:list = []
        self.__mouse_released_keys:list = []

        self.__keyboard_held_keys:list = []
        self.__keyboard_pressed_keys:list = []
        self.__keyboard_released_keys:list = []

        self.should_quit:bool = False

        self.__window_size_changed:bool = False
        self.__window_contains_mouse:bool = False
        self.__window_size:Pos = Pos(-1,-1)
        self.__window_has_focus:bool = False

        self.__listen_list:list[EventConstants] = []

        if super_args is not None:
            super(EventHolder, self).__init__(super_args)

    @property
    def mouse_pos( self ):
        return self.__mouse_pos

    @property
    def mouse_rel( self ):
        return self.__mouse_rel

    @property
    def window_size( self ):
        return self.__window_size

    @window_size.setter
    def window_size( self,new_size:Pos ):
        self.__window_size.reset(pos=new_size)

    @property
    def window_size_changed( self ):
        return self.__window_size_changed

    @property
    def keyboard_held_keys( self ):
        return self.__keyboard_held_keys

    @property
    def keyboard_pressed_keys( self ) :
        return self.__keyboard_pressed_keys

    @property
    def keyboard_released_keys( self ) :
        return self.__keyboard_released_keys

    @property
    def mouse_held_keys( self ) :
        return self.__keyboard_held_keys

    @property
    def mouse_pressed_keys( self ) :
        return self.__keyboard_pressed_keys

    @property
    def mouse_released_keys( self ) :
        return self.__keyboard_released_keys


    @property
    def listen_list( self):
        return self.__listen_list

    @listen_list.setter
    def listen_list( self,listen_list:list ):
        self.__listen_list = listen_list

    @property
    def fetched_events( self ):
        text = "EventHolder {\n"
        L = vars(self)
        for i in L :
            text += "\t" + str(i) + " = " + str(L[i]) + "\n"
        text += "}"
        return text

    def get_events( self,event_list:list[pg.event.Event] ):
        if EventConstants.MOUSE_POS in self.__listen_list:
            self.__mouse_pos.reset(as_tuple=pg.mouse.get_pos())

        self.__mouse_pressed_keys.clear()
        self.__mouse_released_keys.clear()
        self.__keyboard_pressed_keys.clear()
        self.__keyboard_released_keys.clear()

        self.__window_size_changed = False

        for i in event_list:
            if EventConstants.MOUSE_POS:
                if i.type == MOUSEMOTION:
                    self.__mouse_rel.reset(as_tuple=pg.mouse.get_rel())

            if EventConstants.WINDOW in self.__listen_list:
                if i.type == QUIT:
                    self.should_quit = True
                elif i.type == WINDOWSIZECHANGED:
                    self.__window_size.reset(i.x,i.y)
                    self.__window_size_changed = True
                elif i.type == WINDOWENTER:
                    self.__window_contains_mouse = True
                elif i.type == WINDOWLEAVE:
                    self.__window_contains_mouse = False
                elif i.type == WINDOWFOCUSGAINED:
                    self.__window_has_focus = True
                elif i.type == WINDOWFOCUSLOST:
                    self.__window_has_focus = False

            if EventConstants.MOUSE_KEYS:
                if i.type == MOUSEBUTTONDOWN:
                    if i.button not in self.__mouse_held_keys:
                        self.__mouse_held_keys.append(i.button)
                        self.__mouse_pressed_keys.append(i.button)

                if i.type == MOUSEBUTTONDOWN:
                    if i.button in self.__mouse_held_keys:
                        self.__mouse_held_keys.remove(i.button)
                        self.__mouse_released_keys.append(i.button)

            if EventConstants.KEYBOARD_KEYS:
                if i.type == KEYDOWN:
                    if i.key not in self.__keyboard_held_keys:
                        self.__keyboard_held_keys.append(i.key)
                        self.__keyboard_pressed_keys.append(i.key)

                if i.type == KEYUP:
                    if i.key in self.__keyboard_held_keys:
                        self.__keyboard_held_keys.remove(i.key)
                        self.__keyboard_released_keys.append(i.key)