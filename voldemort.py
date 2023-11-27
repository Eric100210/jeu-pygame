import pygame as pg
import random 

class Voldemort(pg.sprite.Sprite):

    def __init__(self, voldemort_event):
        super().__init__()
        self.image = pg.image.load("Voldemort.png")
        self.rect = self.image.get_rect()
        self.vitesse = 5
        self.attaque = 1
        self.rect.x = 900 + random.randint(0,300)
        self.rect.y = 300 + random.randint(-280,250)
        self.voldemort_event = voldemort_event

    def move(self):
        if not self.voldemort_event.jeu.collision(self, self.voldemort_event.jeu.groupe_joueur):
            self.rect.x -= self.vitesse
        else:
            self.jeu.joueur.damage(self.attaque)

