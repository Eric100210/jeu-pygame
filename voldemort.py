import pygame as pg
import random 

class Voldemort(pg.sprite.Sprite):

    def __init__(self, voldemort_event):
        super().__init__()
        self.image = pg.image.load("Voldemort.png")
        self.rect = self.image.get_rect()
        self.vitesse = 3
        self.attaque = 1
        self.rect.x = 900 + random.randint(0,300)
        self.rect.y = 300 + random.randint(-280,250)
        self.vie = 150
        self.vie_max = 150
        self.voldemort_event = voldemort_event

    def move(self):
        if not self.voldemort_event.jeu.collision(self, self.voldemort_event.jeu.groupe_joueur):
            self.rect.x -= self.vitesse
        else:
            self.voldemort_event.jeu.joueur.damage(self.attaque)

    def update_health_bar(self, surface):
        pg.draw.rect(surface, (60,63,60), [self.rect.x + 35, self.rect.y -20, self.vie_max, 5])
        pg.draw.rect(surface,(255,0,0),[self.rect.x + 35,self.rect.y - 20, self.vie, 5])

    def damage(self, degats):
        self.vie -= degats
        if self.vie <= 0:
            self.voldemort_event.jeu.game_over()


