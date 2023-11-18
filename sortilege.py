import pygame as pg

class Sortilege(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vitesse = 5
        self.image = pg.image.load('projectile.png')