import pygame as pg

class Detraqueur(pg.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.jeu = game
        self.vie=100
        self.vie_max=100
        self.vitesse=2
        self.attaque=5
        self.image=pg.image.load('detraqueur.png')
        self.image=pg.transform.scale(self.image, (200,200))
        self.rect=self.image.get_rect()
        self.rect.x=900
        self.rect.y=300

    def move(self): #le détraqueur avance vers la gauche
        if not self.jeu.collision(self, self.jeu.groupe_joueur):
            self.rect.x-=self.vitesse


        