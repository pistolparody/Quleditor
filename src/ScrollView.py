import pygame as pg

import time

from Structures.Pos import Pos
from Structures.Color import Color
from Structures.Rect import Rect
from Structures import Constants as c


class ScrollView :

    def __init__( self, surface_rect: Rect ) :
        self.scroll_rel = Pos(0,0)
        self.scroll_request = Pos(0,0)
        self.scroll_timer = 0
        self.scroll_interval = 1


        self.rect = surface_rect
        self.background_color: Color = c.WOODEN.copy().lerp(c.BLACK,0.3)
        self.surface: pg.surface.Surface = pg.surface.Surface(
            surface_rect.get_size()).convert_alpha()
        self.content_list: list[pg.surface.Surface] = []


        self.content_height = 0
        self.surface.fill(self.background_color)
        self.update_surface(True)

    def get_content_height( self , number:int ):
        return sum([i.get_height() for i in self.content_list[:number]])

    def update_surface( self , initial_update:bool=False) :
        if initial_update: self.scroll_rel.reset()

        self.surface.fill(self.background_color)
        blit_point = Pos(0, 0).join(self.scroll_rel)
        rendered_content_height = 0
        for i in self.content_list :
            if blit_point.y + i.get_height() <= self.rect.height:
                self.surface.blit(i, blit_point)
                rendered_content_height += i.get_height()
            else:
                self.surface.blit(i, blit_point,
                    [0,0,i.get_width(),self.rect.height - blit_point.y]
                )
                rendered_content_height += self.rect.height - blit_point.y
                if not initial_update: break

            blit_point.y += i.get_height()

        if initial_update:
            self.content_height = blit_point.y
            print("content_height",blit_point.y - self.scroll_rel.y,
                    "rendered_content_height",rendered_content_height - self.scroll_rel.y)


    def check_events( self ) :
        if self.scroll_request.y!=0:
            self.scroll_rel.y += self.scroll_request.y
            if self.scroll_rel.y > self.rect.y:
                self.scroll_rel.y = 0
                self.scroll_request.reset()

            if self.content_height + self.scroll_rel.y < self.rect.height:
                self.scroll_rel.y -= self.scroll_request.y
                self.scroll_request.reset()


            self.update_surface()
            current_time = time.time()
            if self.scroll_timer + self.scroll_interval < current_time:
                self.scroll_request.reset()



    def render( self, surface: pg.surface.Surface ) :
        surface.blit(self.surface,self.rect.get_pos())

