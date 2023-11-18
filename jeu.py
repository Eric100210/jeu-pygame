import pygame as pg
from joueur import Joueur

#créer la classe du jeu


class Jeu:

    def __init__(self):
        self.joueur = Joueur()
        self.pressed = {}