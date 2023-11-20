import pygame as pg
from joueur import Joueur
from detraqueur import Detraqueur

#créer la classe du jeu


class Jeu:

    def __init__(self):
        self.groupe_joueur=pg.sprite.Group()
        self.joueur = Joueur(self)
        self.groupe_joueur.add(self.joueur) #créer un groupe avec le joueur, pour gérer les collisions ensuite
        #groupe de détraqueurs
        self.groupe_detraqueurs=pg.sprite.Group()
        self.pressed = {}
        self.spawn_detraqueur()

    #gérer les collisions : on check la collision entre un objet (sprite) et un groupe d'objets
    def collision(self, sprite, groupe):
        return pg.sprite.spritecollide(sprite, groupe, False, pg.sprite.collide_mask)

    def spawn_detraqueur(self):
        detraqueur = Detraqueur(self)
        self.groupe_detraqueurs.add(detraqueur)