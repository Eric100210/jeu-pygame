import pygame as pg
from voldemort import Voldemort 

class VoldemortEvent:
    #on veut savoir si c'est le premier passage de Voldemort ou non
    first=True

    #on crée un compteur
    def __init__(self, jeu):
        self.jeu = jeu
        self.percent = 0
        self.percent_speed = 5
        self.groupe_voldemort = pg.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def vol_is_coming(self):
        if self.is_full_loaded() and self.first:
            self.percent = 0
            self.groupe_voldemort.add(Voldemort(self, 300))
            self.first = False
        if self.is_full_loaded() and not self.first:
            self.percent = 0
            life = self.groupe_voldemort.sprites()[0].vie
            self.groupe_voldemort = pg.sprite.Group()
            self.groupe_voldemort.add(Voldemort(self, life))


    def update_bar(self, surface):
        self.add_percent()

        self.vol_is_coming()

        pg.draw.rect(surface, (0,0,0), [0, surface.get_height()-20, surface.get_width(), 10])
        pg.draw.rect(surface, (187,11,11), [0, surface.get_height()-20, (surface.get_width()/100)*self.percent, 10])