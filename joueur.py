import pygame as pg
from sortilege import Sortilege

#créer la classe des joueurs
class Joueur(pg.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.jeu = game
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
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs):
            self.rect.x = self.rect.x + self.vitesse 
        else:
            for d in self.jeu.groupe_detraqueurs:
                groupe=pg.sprite.Group()
                groupe.add(d)
                if self.jeu.collision(self, groupe) and self.rect.x > d.rect.x:
                    self.rect.x = self.rect.x + self.vitesse

    
    def move_left(self):
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs):
            self.rect.x = self.rect.x - self.vitesse 
        else:
            for d in self.jeu.groupe_detraqueurs:
                groupe=pg.sprite.Group()
                groupe.add(d)
                if self.jeu.collision(self, groupe) and self.rect.x < d.rect.x:
                    self.rect.x = self.rect.x - self.vitesse

    def move_up(self):
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs):
            self.rect.y = self.rect.y - self.vitesse 
        else:
            for d in self.jeu.groupe_detraqueurs:
                groupe=pg.sprite.Group()
                groupe.add(d)
                if self.jeu.collision(self, groupe) and self.rect.y < d.rect.y:
                    self.rect.y = self.rect.y - self.vitesse

    def move_down(self):
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs):
            self.rect.y = self.rect.y + self.vitesse 
        else:
            for d in self.jeu.groupe_detraqueurs:
                groupe=pg.sprite.Group()
                groupe.add(d)
                if self.jeu.collision(self, groupe) and self.rect.y > d.rect.y:
                    self.rect.y = self.rect.y + self.vitesse


