import pygame as pg
from pygame.locals import *
import time

from Structures.Pos import Pos
from Structures.Color import Color
from Structures.Rect import Rect
from Structures import Constants as c
from Structures.Constants import ColorTemplate as ct
from Structures.Functions import get_percent


class ScrollView :

    def __init__( self, surface_rect: Rect, scroll_pane_width: float, wheel_height: float ) :
        self.scroll_rel = Pos(0, 0)
        self.scroll_request = Pos(0, 0)
        self.scroll_timer = 0
        self.scroll_interval = 1

        self.scroll_pane_width = scroll_pane_width
        self.scroll_wheel_color = ct.WOODEN

        self.surface_rect = surface_rect
        self.background_color: Color = ct.WOODEN.copy().lerp(ct.BLACK, 0.3)
        self.surface: pg.surface.Surface = pg.surface.Surface(
            surface_rect.get_size().join(Pos(self.scroll_pane_width, 0))).convert_alpha()

        self.scroll_wheel_rect = Rect(self.surface_rect.width, self.surface_rect.y,
            self.scroll_pane_width, wheel_height)

        self.pressed_mouse_keys = []
        self.held_mouse_keys = []
        self.mouse_pos = Pos(0, 0)
        self.mouse_rel = Pos(0, 0)

        self.content_list: list[pg.surface.Surface] = []

        self.content_height = 0
        self.surface.fill(self.background_color)
        self.update_surface(True)


    def set_mouse_data( self, mouse_pos: Pos, pressed_mouse_keys: list, held_mouse_keys: list ) :
        self.mouse_pos = mouse_pos
        self.pressed_mouse_keys = pressed_mouse_keys
        self.held_mouse_keys = held_mouse_keys


    def get_scroll_scale( self ) :
        max_ = self.content_height - self.surface_rect.height
        return get_percent(max_, abs(self.scroll_rel.y)) / 100


    def get_scroll_wheel_pos_y( self ) :
        scale = self.get_scroll_scale()

        return (self.surface_rect.height - self.scroll_wheel_rect.height) * scale


    def get_content_height( self, number: int ) :
        return sum([i.get_height() for i in self.content_list[:number]])


    def update_surface( self, initial_update: bool = False ) :
        if initial_update : self.scroll_rel.reset()

        self.surface.fill(self.background_color)
        blit_point = Pos(0, 0).join(self.scroll_rel)
        rendered_content_height = 0

        for i in self.content_list :
            if blit_point.y + i.get_height() <= self.surface_rect.height :
                self.surface.blit(i, blit_point)
                rendered_content_height += i.get_height()
            else :
                self.surface.blit(i, blit_point,
                    [0, 0, i.get_width(), self.surface_rect.height - blit_point.y])
                rendered_content_height += self.surface_rect.height - blit_point.y
                if not initial_update : break

            blit_point.y += i.get_height()

        wheel_rect = self.scroll_wheel_rect
        wheel_rect.y = self.get_scroll_wheel_pos_y()

        pg.draw.rect(self.surface, self.scroll_wheel_color, wheel_rect)

        if initial_update :
            self.content_height = blit_point.y
            print("content_height", blit_point.y - self.scroll_rel.y, "rendered_content_height",
                rendered_content_height - self.scroll_rel.y)


    def get_events( self , event_list:list ):

        for i in event_list:
            if i.type == MOUSEMOTION:
                self.mouse_rel.reset_by_tuple(i.rel)

    def check_events( self ) :
        if c.MOUSE_LEFT in self.held_mouse_keys :
            if self.scroll_wheel_rect.collidepoint(self.mouse_pos) :
                pg.mouse.set_pos(self.scroll_wheel_rect.get_center())
                self.mouse_pos = self.scroll_wheel_rect.get_center().join(self.mouse_rel)

                mouse_pos = self.mouse_pos.copy()
                mouse_pos.y -= self.scroll_wheel_rect.height / 2

                A = self.content_height - self.surface_rect.height
                B = self.surface_rect.height - self.scroll_wheel_rect.height
                C = get_percent(B, mouse_pos.y)
                if C < 0: C = 0
                if C > 100: C = 100
                D = A * C / 100
                print([round(i, 2) for i in
                    [A, B, C, D, self.content_height, self.surface_rect.height, self.scroll_rel.y]])

                self.scroll_rel.y = - D
                self.update_surface(False)

        # self.mouse_rel.reset()


        if self.scroll_request.y != 0 :
            # print(self.get_scroll_scale())
            self.scroll_rel.y += self.scroll_request.y
            if self.scroll_rel.y > self.surface_rect.y :
                self.scroll_rel.y = 0
                self.scroll_request.reset()

            if self.content_height + self.scroll_rel.y < self.surface_rect.height :
                self.scroll_rel.y -= self.scroll_request.y
                self.scroll_request.reset()

            self.update_surface()
            current_time = time.time()
            if self.scroll_timer + self.scroll_interval < current_time :
                self.scroll_request.reset()


    def render( self, surface: pg.surface.Surface ) :
        surface.blit(self.surface, self.surface_rect.get_pos())
