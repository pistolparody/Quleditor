import pygame as pg
from pygame.locals import *

from Player import Player

from Structures.Color import *
from Structures.Rect import *
from Structures.Pos import *
from Structures.Sprite import *
from Structures.MSprite import *
from Structures import Constants as c
from Structures.Enumerator import *


class Game:
    def __init__( self , surface_size:Pos):
        self.surface_size = surface_size
        self.background_color = c.DEEP_DARK_RED
        self.should_render_debug = False

        self.held_keys = []

        self.player = Player(
            Rect.fromPos(self.surface_size.get_transformed_pos(mult=0.5),
                         Pos(self.surface_size.x*0.1,self.surface_size.x*0.1)))




    def get_events( self, event_list:list = None):
        if event_list is None: event_list = pg.event.get()

        for i in event_list:

            if i.type == KEYDOWN and i.key not in self.held_keys:
                self.held_keys.append(i.key)
            elif i.type == KEYUP and i.key in self.held_keys:
                self.held_keys.remove(i.key)

            if i.type == KEYDOWN:
                if i.key == K_RIGHT: self.player.direction = c.EAST
                if i.key == K_LEFT: self.player.direction = c.WEST
                if i.key == K_UP: self.player.direction = c.NORTH
                if i.key == K_DOWN: self.player.direction = c.SOUTH


    def check_events( self ):
        self.player.check_events()
        self.player.is_moving = any([i in self.held_keys for i in [K_RIGHT,K_LEFT,K_UP,K_DOWN]])
        self.player.is_running = any([i in self.held_keys for i in [K_RSHIFT,K_LSHIFT]])
        self.player.is_swinging = any([i in self.held_keys for i in [K_x]])
        self.player.is_pushing = any([i in self.held_keys for i in [K_RALT,K_LALT]])
        self.player.is_climbing = any([i in self.held_keys for i in [K_LCTRL,K_RCTRL]])



    def render_debug( self , surface:pg.surface.Surface ):
        pg.draw.line( surface, [180, 180, 180], [self.surface_size.x / 2, 0],
            [self.surface_size.x / 2, self.surface_size.y] )

        pg.draw.line( surface, [180, 180, 180], [0, self.surface_size.y / 2],
            [self.surface_size.x, self.surface_size.y / 2] )

    def render( self , surface:pg.surface.Surface):
        surface.fill(self.background_color)

        self.player.render(surface)


        if self.should_render_debug: self.render_debug(surface)


