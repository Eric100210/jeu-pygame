import pygame as pg

#créer la classe des joueurs
class Joueur(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie = 100
        self.max_vie = 100
        self.sort = 10
        self.vitesse = 5
        self.image = pg.image.load('harry2.png')
        self.rect = self.image.get_rect()
        self.rect.y = 100
    
    def move_right(self):
        self.rect.x = self.rect.x + self.vitesse 
    
    def move_left(self):
        self.rect.x = self.rect.x - self.vitesse 

    def move_up(self):
        self.rect.y = self.rect.y - self.vitesse 

    def move_down(self):
        self.rect.y = self.rect.y + self.vitesse 

