import pygame as pg
from joueur import Joueur
from detraqueur import Detraqueur
from voldemort_event import VoldemortEvent
from son import Son


#créer la classe du jeu

class Jeu:

    def __init__(self):
        #définir si le jeu a commencé ou non
        self.is_playing_harry = False
        self.is_playing_hermione = False
        self.is_playing_drago = False
        self.choose_character = False
        self.defaite = False
        self.victoire = False
        self.character = pg.image.load('harry2.png')
        #générer le joueur
        self.groupe_joueur = pg.sprite.Group()
        self.joueur = Joueur(self)
        self.pressed = {}
        self.groupe_joueur.add(self.joueur) #créer un groupe avec le joueur, pour gérer les collisions ensuite
        #groupe de détraqueurs
        self.groupe_detraqueurs = pg.sprite.Group()
        self.voldemort_event =VoldemortEvent(self)
        #score
        self.score = 0
        self.font = pg.font.SysFont("Comic sans MS", 35) # on crée la police
        #on met du son
        self.son = Son()

    def start_harry(self):
        """démarre le jeu avec Harry, et fait apparaître directement 2 détraqueurs"""
        self.is_playing_harry = True
        self.spawn_detraqueur()
        self.spawn_detraqueur() 

    def start_hermione(self):
        """démarre le jeu avec Hermione, et fait apparaître directement 2 détraqueurs"""
        self.is_playing_hermione = True
        self.spawn_detraqueur()
        self.spawn_detraqueur()
    
    def start_drago(self):
        """démarre le jeu avec Drago, et fait apparaître directement 2 détraqueurs"""
        self.is_playing_drago = True
        self.spawn_detraqueur()
        self.spawn_detraqueur()

    def game_over(self):
        """gère l'apparition de la fenêtre de game over et la disparition des éléments du jeu"""
        self.groupe_detraqueurs = pg.sprite.Group() # on écrase tous les détraqueurs en mettant un groupe vide
        self.voldemort_event.groupe_voldemort = pg.sprite.Group() 
        self.joueur.groupe_sortileges = pg.sprite.Group()
        self.voldemort_event.first = True
        self.joueur.health = self.joueur.health_max
        self.is_playing_harry = False
        self.is_playing_hermione = False
        self.is_playing_drago = False
        self.score = 0
        self.voldemort_event.percent = 0
        self.son.play('game_over')
        self.defaite = True

    def victory(self):
        """gère l'apparition de la fenêtre de victoire et la disparition des éléments du jeu"""
        self.groupe_detraqueurs = pg.sprite.Group() 
        self.voldemort_event.groupe_voldemort = pg.sprite.Group() 
        self.joueur.groupe_sortileges = pg.sprite.Group()
        self.voldemort_event.first = True
        self.joueur.health = self.joueur.health_max
        self.is_playing_harry = False
        self.is_playing_hermione = False
        self.is_playing_drago = False
        self.score = 0
        self.voldemort_event.percent = 0
        self.victoire = True



    def update(self, screen, perso):
        """boucle du jeu qu'on exécute à chaque instant"""
        #afficher le score
        score_text = self.font.render(f"Score : {self.score}", 1, (255,255,255))
        screen.blit(score_text, (20,20))

        #appliquer l'image du joueur
        screen.blit(perso, self.joueur.rect)

        self.joueur.update_health_bar(screen)

        self.voldemort_event.update_bar(screen)

        for sort in self.joueur.groupe_sortileges:
            sort.move()

        for detraqueur in self.groupe_detraqueurs:
            detraqueur.move()
            detraqueur.update_health_bar(screen)
        
        for voldemort in self.voldemort_event.groupe_voldemort:
            voldemort.move()
            voldemort.update_health_bar(screen)
    

        #appliquer l'ensemble des images du groupe de sortilèges
        self.joueur.groupe_sortileges.draw(screen)

        #appliquer l'ensemble des images du groupe détraqueurs
        self.groupe_detraqueurs.draw(screen)

        #appliquer l'image de Voldemort
        self.voldemort_event.groupe_voldemort.draw(screen)

        #appliquer l'image des bonus
        self.voldemort_event.groupe_bonus.draw(screen)

        if self.pressed.get(pg.K_RIGHT) and self.joueur.rect.x + self.joueur.rect.width < screen.get_width():
            self.joueur.move_right()
        elif self.pressed.get(pg.K_LEFT) and self.joueur.rect.x > 0:
            self.joueur.move_left()
        elif self.pressed.get(pg.K_UP) and self.joueur.rect.y > 0:
            self.joueur.move_up() 
        elif self.pressed.get(pg.K_DOWN) and self.joueur.rect.y + self.joueur.rect.height < screen.get_height():
            self.joueur.move_down()


    
    def collision(self, sprite, groupe):
        """renvoie True s'il y a collision entre un sprite et un groupe de sprites"""
        return pg.sprite.spritecollide(sprite, groupe, False, pg.sprite.collide_mask)

    def spawn_detraqueur(self):
        """provoque l'apparition d'un détraqueur sur la fenêtre"""
        detraqueur = Detraqueur(self)
        self.groupe_detraqueurs.add(detraqueur)