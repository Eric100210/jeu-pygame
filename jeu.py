import pygame as pg
from joueur import Joueur
from detraqueur import Detraqueur

#créer la classe du jeu

class Jeu:

    def __init__(self):
        #définir si le jeu a commencé ou non
        self.is_playing = False
        #générer le joueur
        self.groupe_joueur = pg.sprite.Group()
        self.joueur = Joueur(self)
        self.pressed = {}
        self.groupe_joueur.add(self.joueur) #créer un groupe avec le joueur, pour gérer les collisions ensuite
        #groupe de détraqueurs
        self.groupe_detraqueurs = pg.sprite.Group()

    def start(self):
        self.is_playing = True
        self.spawn_detraqueur() #génère un détraqueur dès le début du jeu

    def game_over(self):
        self.groupe_detraqueurs = pg.sprite.Group() # on écrase tous les détraqueurs en mettant un groupe vide
        self.joueur.health = self.joueur.health_max
        self.is_playing = False

    def update(self, screen):
        #appliquer l'image du joueur
        screen.blit(self.joueur.image, self.joueur.rect)

        self.joueur.update_health_bar(screen)

        for sort in self.joueur.groupe_sortileges:
            sort.move()

        for detraqueur in self.groupe_detraqueurs:
            detraqueur.move()
            detraqueur.update_health_bar(screen)
    
        #appliquer l'ensemble des images du groupe de sortilèges
        self.joueur.groupe_sortileges.draw(screen)

        #appliquer l'ensemble des images du groupe détraqueurs
        self.groupe_detraqueurs.draw(screen)

        if self.pressed.get(pg.K_RIGHT) and self.joueur.rect.x + self.joueur.rect.width < screen.get_width():
            self.joueur.move_right()
        elif self.pressed.get(pg.K_LEFT) and self.joueur.rect.x > 0:
            self.joueur.move_left()
        elif self.pressed.get(pg.K_UP) and self.joueur.rect.y > 0:
            self.joueur.move_up() 
        elif self.pressed.get(pg.K_DOWN) and self.joueur.rect.y + self.joueur.rect.height < screen.get_height():
            self.joueur.move_down()


    #gérer les collisions : on check la collision entre un objet (sprite) et un groupe d'objets
    def collision(self, sprite, groupe):
        return pg.sprite.spritecollide(sprite, groupe, False, pg.sprite.collide_mask)

    def spawn_detraqueur(self):
        detraqueur = Detraqueur(self)
        self.groupe_detraqueurs.add(detraqueur)