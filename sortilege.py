import pygame as pg

class Sortilege(pg.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.vitesse = 6
        self.joueur = joueur
        self.image = pg.image.load('projectile.png')
        self.image = pg.transform.scale(self.image, (50,50))
        self.image = pg.transform.rotate(self.image, 290) #pour orienter l'image de départ du sortilège
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 145
        self.rect.y = joueur.rect.y + 100
        self.origine_image = self.image
        self.angle = 0

    
    def rotate(self):
        """gère la rotation du sortilège lorsqu'il se déplace"""
        self.angle += 12
        self.image = pg.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center) #pour que la rotation se fasse par rapport au centre du rect
        
    def remove(self):
        """gère la suppression du sortilège"""
        self.joueur.groupe_sortileges.remove(self)

    def move(self):
        """gère le déplacement vers la droite du sortilege et les cas de suppression"""
        self.rect.x += self.vitesse
        self.rotate()

        #vérifier si le sortilège entre en collision avec un détraqueur
        for d in self.joueur.jeu.collision(self, self.joueur.jeu.groupe_detraqueurs):
            self.remove()
            d.damage(self.joueur.sort)
        
        #vérifier si le sortilège entre en collision avec un Voldemort
        for v in self.joueur.jeu.collision(self, self.joueur.jeu.voldemort_event.groupe_voldemort):
            self.remove()
            v.damage(self.joueur.sort)

        #on supprime le sortilège qui sort de l'écran
        if self.rect.x > 1100:
            self.remove()