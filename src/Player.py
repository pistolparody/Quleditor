import pygame as pg
import pathlib

from pg_atlas import PGAtlas

from Structures.Color import *
from Structures.Rect import *
from Structures.Pos import *
from Structures.Sprite import *
from Structures.MSprite import *
from Structures import Constants as c
from Structures.Enumerator import *
from PlayerAssets import PlayerAssets

class Player(PlayerAssets) :

    def __init__( self, init_rect: Rect ) :
        super().__init__()

        self.rect = init_rect
        self.color = c.DARK_ICE

        self.direction = c.WEST
        self.state = c.IDLE
        self.walk_speed_scale = 0.015
        self.run_speed_scale = 0.032


        self.is_moving = False
        self.is_running = False
        self.is_swinging = False
        self.is_pushing = False
        self.is_climbing = False
        self.should_render_debug = False

        self.__atlas = None

        self.update_sprites()



    def update_sprites( self ) :
        x_scale = self.rect.height / self.walk_east_sprites[0].get_raw_size().y

        for x in self.atlas_table :
            for f in self.atlas_table[x]:
                i = self.atlas_table[x][f]
                i.reset_scale(Pos(x_scale, x_scale))
                i.transform_images()

    def get_center( self ) :
        return self.rect.get_pos().join(self.rect.get_size().get_transformed_pos(mult=0.5))


    def set_size( self, size: Pos ) :
        self.rect.get_size().reset(size.x, size.y)


    def move( self ) :
        speed_scale = self.walk_speed_scale
        if self.state == c.RUN: speed_scale = self.run_speed_scale

        if self.direction == c.NORTH :
            self.rect.y -= self.rect.height * speed_scale
        elif self.direction == c.SOUTH :
            self.rect.y += self.rect.height * speed_scale
        elif self.direction == c.EAST :
            self.rect.x += self.rect.width * speed_scale
        elif self.direction == c.WEST :
            self.rect.x -= self.rect.width * speed_scale

        if self.rect.x < self.rect.width :
            pass
        if self.rect.y < self.rect.height :
            pass


    def check_events( self ) :
        if self.is_swinging :
            self.state = c.SWING
        elif self.is_moving :
            self.state = c.WALK
            if self.is_running:
                self.state = c.RUN
            if self.is_pushing:
                self.state = c.PUSH
            if self.is_climbing:
                self.state = c.CLIMB
            self.move()
        else :
            self.state = c.IDLE




        target_msprite = self.atlas_table[self.state][self.direction]

        target_msprite.check_events()


    def render_debug( self, surface: pg.surface.Surface ) :
        pg.draw.rect(surface, self.color, self.rect)


    def render( self, surface: pg.surface.Surface ) :
        if self.should_render_debug : self.render_debug(surface)

        target_msprite = self.atlas_table[self.state][self.direction]

        target_msprite.render(surface, self.get_center())




