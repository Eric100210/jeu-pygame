import pygame as pg

class Son:

    def __init__(self):
        self.sons = {'click': pg.mixer.Sound('click.ogg'), 'game_over': pg.mixer.Sound('game_over.ogg'), 'tir': pg.mixer.Sound('tir.ogg')}

    def play(self, name): #nom du son à jouer
        self.sons[name].play()