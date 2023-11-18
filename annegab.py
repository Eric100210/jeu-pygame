import pygame as pg
pg.init()
from jeu import Jeu 

#générer la fenêtre de notre jeu
pg.display.set_caption("Kill the dementors")
screen = pg.display.set_mode((1100,700))
background = pg.image.load('background.png')


#charger notre joueur et notre jeu
jeu=Jeu()

running = True

#Boucle tant que cette condition est vraie
while running:

    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0,0))

    #appliquer l'image du joueur
    screen.blit(jeu.joueur.image, jeu.joueur.rect)

    for sort in jeu.joueur.groupe_sortileges:
        sort.move()
    
    #appliquer l'ensemble des images du groupe de sortilèges
    jeu.joueur.groupe_sortileges.draw(screen)

    if jeu.pressed.get(pg.K_RIGHT) and jeu.joueur.rect.x + jeu.joueur.rect.width < screen.get_width():
        jeu.joueur.move_right()
    elif jeu.pressed.get(pg.K_LEFT) and jeu.joueur.rect.x > 0:
        jeu.joueur.move_left()
    elif jeu.pressed.get(pg.K_UP) and jeu.joueur.rect.y >0:
        jeu.joueur.move_up() 
    elif jeu.pressed.get(pg.K_DOWN) and jeu.joueur.rect.y + jeu.joueur.rect.height < screen.get_height():
        jeu.joueur.move_down()

    print(jeu.joueur.rect.x)

    pg.display.flip() #on met à jour

    #si le joueur veut quitter le jeu
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
    

            