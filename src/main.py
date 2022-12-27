import pygame as pg
import time

from Structures.Window import Window
from Structures.Pos import Pos
from Structures.Color import Color
from Structures.Menu import Menu
from Structures.TextBox import TextBox
from Structures.TextHolder import TextHolder
from Structures.Rect import Rect
from Structures.Page import Page
from Structures import Constants
from Game import Game


bg = Color(150,150,255)

pg.init()

window = Window(Pos(1000,725),Pos(800,600),"Chaotic Kung-Fu King",60,Constants.REAL_SIZE)
menu = Menu(window.get_mask_size())
textHolder = TextHolder("What's up?",pg.font.Font(None,30))
textBox = TextBox(Rect(100,100,600,50),textHolder)
textBox0 = TextBox(Rect(100,100,600,50),textHolder)
textBox1 = TextBox(Rect(100,100,600,50),textHolder)

textBox.centralize_text()
textBox.update_surface()

page = Page((400,300),height_step=100)
page.addTextBox(textBox)
page.addTextBox(textBox0)
page.addTextBox(textBox1)

page.update_page()

game = Game(window.get_window_size())


frames = 0
t = time.time()

while window.is_running:
    frames += 1
    event_list = pg.event.get()

    window.get_events(event_list)
    game.get_events(event_list)

    game.check_events()
    window.check_events()

    game.render(window.get_window())
    window.render_and_update()
    window.tick()

    if window.window_size_changed: game.surface_size = window.get_window_size()



    if frames >= 60:
        frames = 0
        t = time.time()