import pygame as pg
pg.init()
from jeu import Jeu 

#générer la fenêtre de notre jeu
pg.display.set_caption("Kill the dementors")
screen = pg.display.set_mode((1100,700))
background = pg.image.load('background.png')
banniere = pg.image.load('logo_harrypotter.tiff')
bouton_play = pg.image.load('play2.png')
bouton_play_rect = bouton_play.get_rect()
bouton_play_rect.x = bouton_play_rect.x + 400
bouton_play_rect.y = bouton_play_rect.y + 320

#charger notre joueur et notre jeu
jeu=Jeu()

running = True

#Boucle tant que cette condition est vraie
while running:

    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0,0))

    #vérifier si le jeu à commencé
    if jeu.is_playing:
        jeu.update(screen)
    else:
        screen.blit(banniere, (200, 100))
        screen.blit(bouton_play, (400, 320))
        

    pg.display.flip() #on met à jour

    #récupération des touches appuyées, pour les mettre dans le dictionnaire pressed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        elif event.type == pg.KEYDOWN:
            jeu.pressed[event.key] = True
            if event.key == pg.K_SPACE:
                jeu.joueur.launch_spell()

        elif event.type == pg.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            #savoir si on a cliqué sur le bouton play
            if bouton_play_rect.collidepoint(event.pos): #event.pos récupère la position de la souris
                jeu.start()
            