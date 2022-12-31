import pygame as pg

def safe_image_load(path:str) -> pg.surface.Surface or None:
    try:
        return pg.image.load(path)
    except OSError:
        return None

def get_percent(All:float,part:float):
    return part * ( 100 / All )

print(get_percent(1000,320))