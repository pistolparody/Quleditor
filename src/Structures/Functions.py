import pygame as pg
def safe_image_load(path:str) -> pg.surface.Surface or None:
    try:
        return pg.image.load(path)
    except Exception:
        return None

