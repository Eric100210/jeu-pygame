import pygame as pg
from random import randint

class Bonus(pg.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.vitesse = 2.3
        self.vie_supp = 50
        self.image = pg.image.load('bonus.png')
        self.image = pg.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = randint(50,1050)
        self.rect.y = -50
        self.jeu = jeu

    def collision(self):
        """gère les effets de la collision du joueur avec le bonus de vie"""
        if self.jeu.joueur.health <= 50:
            self.jeu.joueur.health += 50
        else:
            self.jeu.joueur.health = 100
        self.remove()

    def move(self):
        """gère le déplacement du bonus vers le bas, et sa suppression quand il disparaît de l'écran"""
        self.rect.y += self.vitesse
        if self.rect.y >= 800:
            self.remove()

    def remove(self):
        """suppression du bonus"""
        self.kill()
