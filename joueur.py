import pygame as pg
from sortilege import Sortilege

#créer la classe des joueurs
class Joueur(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie = 100
        self.max_vie = 100
        self.sort = 10
        self.vitesse = 5
        self.groupe_sortileges=pg.sprite.Group() #groupe de sortileges pour pouvoir lancer plusieurs sorts
        self.image = pg.image.load('harry2.png')
        self.rect = self.image.get_rect()
        self.rect.y = 100

    def launch_spell(self):
        #créer un nouvel objet de la classe Sortilege
        self.groupe_sortileges.add(Sortilege(self)) #on place self en argument pour avoir accès aux coordonnées du joueur au moment de lancer un sortilège
    
    def move_right(self):
        self.rect.x = self.rect.x + self.vitesse 
    
    def move_left(self):
        self.rect.x = self.rect.x - self.vitesse 

    def move_up(self):
        self.rect.y = self.rect.y - self.vitesse 

    def move_down(self):
        self.rect.y = self.rect.y + self.vitesse 

