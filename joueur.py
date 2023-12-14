import pygame as pg
from sortilege import Sortilege

#créer la classe des joueurs
class Joueur(pg.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.health_max = 100
        self.sort = 10
        self.vitesse = 5
        self.groupe_sortileges = pg.sprite.Group() #groupe de sortileges pour pouvoir lancer plusieurs sorts
        self.image = jeu.character
        self.rect = self.image.get_rect()
        self.rect.y = 100

    def update_health_bar(self, surface):
        """gère la barre de vie du joueur"""
        pg.draw.rect(surface, (60,63,60), [self.rect.x + 93, self.rect.y - 10, self.health_max, 7])
        pg.draw.rect(surface,(0,255,0),[self.rect.x + 93, self.rect.y - 10, self.health, 7])

    def damage(self, degats):
        """gère l'encaissement de dégâts de notre joueur, et sa mort le cas échéant"""
        if self.health-degats >= degats:
            self.health -= degats
        else:
            self.jeu.game_over()

    def launch_spell(self):
        """créer un nouvel objet de la classe Sortilege"""
        self.groupe_sortileges.add(Sortilege(self)) #on place self en argument pour avoir accès aux coordonnées du joueur au moment de lancer un sortilège
        self.jeu.son.play('tir')
    

    def move_right(self):
        """gère le déplacement vers la droite, selon s'il y a des collisions ou non"""
        # si pas de collision, on peut avancer
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs) and not self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort):
            self.rect.x = self.rect.x + self.vitesse 
        #s'il y a collision, on ne peut avancer que dans la direction opposée au détraqueur
        else:
            if self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort) and self.rect.x > self.jeu.voldemort_event.groupe_voldemort.sprites()[0].rect.x:
                self.rect.x = self.rect.x + self.vitesse
            else:
                for d in self.jeu.groupe_detraqueurs:
                    groupe = pg.sprite.Group()
                    groupe.add(d)
                    if self.jeu.collision(self, groupe) and self.rect.x > d.rect.x:
                        self.rect.x = self.rect.x + self.vitesse

    
    def move_left(self):
        """gère le déplacement vers la gauche, selon s'il y a des collisions ou non"""
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs) and not self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort):
            self.rect.x = self.rect.x - self.vitesse 
        else:
            if self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort) and self.rect.x < self.jeu.voldemort_event.groupe_voldemort.sprites()[0].rect.x:
                self.rect.x = self.rect.x - self.vitesse
            else:
                for d in self.jeu.groupe_detraqueurs:
                    groupe=pg.sprite.Group()
                    groupe.add(d)
                    if self.jeu.collision(self, groupe) and self.rect.x < d.rect.x:
                        self.rect.x = self.rect.x - self.vitesse

    def move_up(self):
        """gère le déplacement vers le haut, selon s'il y a des collisions ou non"""
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs) and not self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort):
            self.rect.y = self.rect.y - self.vitesse 
        else:
            if self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort) and self.rect.y < self.jeu.voldemort_event.groupe_voldemort.sprites()[0].rect.y:
                self.rect.y = self.rect.y - self.vitesse
            else:
                for d in self.jeu.groupe_detraqueurs:
                    groupe = pg.sprite.Group()
                    groupe.add(d)
                    if self.jeu.collision(self, groupe) and self.rect.y < d.rect.y:
                        self.rect.y = self.rect.y - self.vitesse

    def move_down(self):
        """gère le déplacement vers le bas, selon s'il y a des collisions ou non"""
        if not self.jeu.collision(self, self.jeu.groupe_detraqueurs) and not self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort):
            self.rect.y = self.rect.y + self.vitesse 
        else:
            if self.jeu.collision(self, self.jeu.voldemort_event.groupe_voldemort) and self.rect.y > self.jeu.voldemort_event.groupe_voldemort.sprites()[0].rect.y:
                self.rect.y = self.rect.y + self.vitesse
            else:
                for d in self.jeu.groupe_detraqueurs:
                    groupe=pg.sprite.Group()
                    groupe.add(d)
                    if self.jeu.collision(self, groupe) and self.rect.y > d.rect.y:
                        self.rect.y = self.rect.y + self.vitesse


