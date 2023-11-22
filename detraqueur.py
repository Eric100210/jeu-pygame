import pygame as pg
import random

class Detraqueur(pg.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.vie=100
        self.vie_max=100
        self.vitesse=2 + random.uniform(-0.5,1.5)
        self.attaque=0.3
        self.image=pg.image.load('detraqueur.png')
        self.image=pg.transform.scale(self.image, (200,200))
        self.rect=self.image.get_rect()
        self.rect.x=900 + random.randint(0,300)
        self.rect.y=300 + random.randint(-280,250)

    def damage(self, degats):
        self.vie -= degats
        if self.vie <= 0:
            self.rect.x=900 + random.randint(0,300)
            self.rect.y=300 + random.randint(-280,250)
            self.vitesse=2 + random.uniform(-0.5,1.5)
            self.vie = self.vie_max

    def update_health_bar(self, surface):
        pg.draw.rect(surface, (60,63,60), [self.rect.x+38, self.rect.y -20, self.vie_max, 5])
        pg.draw.rect(surface,(255,0,0),[self.rect.x + 38,self.rect.y - 20,self.vie,5])

    def remove(self):
        self.jeu.groupe_detraqueurs.remove(self)

    def move(self): #le détraqueur avance vers la gauche
        if not self.jeu.collision(self, self.jeu.groupe_joueur):
            self.rect.x -= self.vitesse
        else:
            self.jeu.joueur.damage(self.attaque)
        if self.rect.x<-200:
            self.remove()


        