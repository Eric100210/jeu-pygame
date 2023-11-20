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

    def update_health_bar(self, surface):
        couleur=(255,0,0) #barre de vie rouge pour les ennemis
        couleur_arriere_barre = (60,63,60)
        position=[self.rect.x + 38,self.rect.y - 20,self.vie,5]
        position_arriere=[self.rect.x+38, self.rect.y -20, self.vie_max, 5]
        pg.draw.rect(surface, couleur_arriere_barre, position_arriere)
        pg.draw.rect(surface,couleur,position)

    def remove(self):
        self.jeu.groupe_detraqueurs.remove(self)

    def move(self): #le détraqueur avance vers la gauche
        if not self.jeu.collision(self, self.jeu.groupe_joueur):
            self.rect.x-=self.vitesse
        if self.rect.x<-200:
            self.remove()


        