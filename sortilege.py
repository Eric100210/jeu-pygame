import pygame as pg

class Sortilege(pg.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.vitesse = 5
        self.joueur = joueur
        self.image = pg.image.load('projectile.png')
        self.image = pg.transform.scale(self.image, (50,50))
        self.image = pg.transform.rotate(self.image, 290) #pour orienter l'image de départ du sortilège
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 145
        self.rect.y = joueur.rect.y + 100
        self.origine_image = self.image
        self.angle=0

    
    def rotate(self):
        self.angle+=12
        self.image=pg.transform.rotozoom(self.origine_image,self.angle,1)
        self.rect=self.image.get_rect(center=self.rect.center) #pour que la rotation se fasse par rapport au centre du rect
        
    def remove(self):
        self.joueur.groupe_sortileges.remove(self)

    def move(self):
        self.rect.x+=self.vitesse
        self.rotate()

        #vérifier si le sortilège entre en collision avec un détraqueur
        if self.joueur.jeu.collision(self, self.joueur.jeu.groupe_detraqueurs):
            self.remove()

        if self.rect.x > 1100:
            self.remove()