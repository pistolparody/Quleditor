import pygame as pg

import time
from Structures.Window import Window
from Structures.Menu import Menu
from Structures.Pos import Pos
from Structures import Constants as c
from AssetManager import AssetManager

class Editor:
    def __init__(self,screen_size:Pos):
        self.asset_manager = AssetManager(screen_size)

    def get_grabbed_files( self , grabbed_files:list ):
        self.asset_manager.last_dropped_files = grabbed_files

    def get_events( self , event_list:list ):
        self.asset_manager.get_events(event_list,Pos.fromTuple(pg.mouse.get_pos()))

    def check_events( self ):
        self.asset_manager.check_events()

    def render( self,surface:pg.surface.Surface ):
        self.asset_manager.render(surface)