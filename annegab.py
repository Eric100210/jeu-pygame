import pygame as pg
pg.init()

#générer la fenêtre de notre jeu
pg.display.set_caption("Kill the dementors")
screen = pg.display.set_mode((1200,900))
background = pg.image.load('background.png')

running = True

#Boucle tant que cette condition est vraie
while running:

    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0,0))
    pg.display.flip() #on met à jour

    #si le joueur veut quitter le jeu
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()