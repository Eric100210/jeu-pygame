import pygame as pg
from voldemort import Voldemort 
from random import randint
from bonus import Bonus

class VoldemortEvent:
    #on veut savoir si c'est le premier passage de Voldemort ou non
    first=True

    def __init__(self, jeu):
        self.jeu = jeu
        self.percent = 0
        self.percent_speed = 5
        self.groupe_voldemort = pg.sprite.Group()
        self.groupe_bonus = pg.sprite.Group()

    def add_percent(self):
        """Faire avancer le temps d'attente de Voldemort"""
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        """Regarde si le temps d'attente de Voldemort est écoulé"""
        return self.percent >= 100
    
    def vol_is_coming(self):
        """Entraîner l'apparition de Voldemort quand le temps est écoulé, avec la vie qu'il lui restait"""
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
        """gère l'avancée de la barre d'attente de Voldemort en bas de l'écran, et gestion de l'aléatoire du bonus de vie"""
        self.add_percent()

        self.vol_is_coming()

        rand = randint(0,1000)
        if rand ==1 : #probabilité de 1/1000 qu'il tombe un bonus de vie à chaque micro-instant
            self.groupe_bonus.add(Bonus(self.jeu))
        
        for i in self.groupe_bonus:
            i.move()

        pg.draw.rect(surface, (0,0,0), [0, surface.get_height()-20, surface.get_width(), 10])
        pg.draw.rect(surface, (187,11,11), [0, surface.get_height()-20, (surface.get_width()/100)*self.percent, 10])