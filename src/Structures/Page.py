import pygame as pg

from .TextBox import TextBox
from .Pos import Pos

class Page:
    def __init__(self,center:tuple[float,float],height_step=50):
        self.textBoxList:list[TextBox] = []
        self.height_step = height_step
        self.all_height = 0
        self.center = center

    def addTextBox(self,textBox:TextBox):
        self.textBoxList.append(textBox)
        self.all_height = self.height_step * len(self.textBoxList)\


    def insertTextBox( self, textBox: TextBox ,index:int) :
        self.textBoxList.insert( index, textBox )
        self.all_height = self.height_step * len( self.textBoxList )

    def update_page(self):
        counter = 0
        for i in self.textBoxList:
            i.set_pos(Pos(self.center[0] - i.get_width() / 2
                      , self.center[1] + counter * self.height_step - self.all_height // 2))
            counter+=1

    def render(self,surface:pg.surface.Surface):

        counter = 0
        for i in self.textBoxList:

            i.render(surface)
            counter += 1