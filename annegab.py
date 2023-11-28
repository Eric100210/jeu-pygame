import pygame as pg
pg.init()
from jeu import Jeu 

#générer la fenêtre de notre jeu
pg.display.set_caption("Kill the dementors")
screen = pg.display.set_mode((1100,700))
background = pg.image.load('background.png')
banniere = pg.image.load('logo_harrypotter.tiff')
#bouton_play = pg.image.load('play2.png')
#bouton_play_rect = bouton_play.get_rect()
#bouton_play_rect.x = bouton_play_rect.x + 400
#bouton_play_rect.y = bouton_play_rect.y + 320
bouton_character = pg.image.load('choose_character.png')
bouton_character = pg.transform.scale(bouton_character,(425,205))
bouton_character_rect = bouton_character.get_rect()
bouton_character_rect.x = bouton_character_rect.x + 350
bouton_character_rect.y = bouton_character_rect.y + 325

harry = pg.image.load('harry2.png')
harry_rect = harry.get_rect()
harry_rect.x = harry_rect.x+100
harry_rect.y = harry_rect.y+200
hermione = pg.image.load('hermione2.png')
hermione_rect = hermione.get_rect()
hermione_rect.x = hermione_rect.x+410
hermione_rect.y = hermione_rect.y+200
drago = pg.image.load('drago2.png')
drago_rect = drago.get_rect()
drago_rect.x = drago_rect.x + 720
drago_rect.y = drago_rect.y + 200


#charger notre joueur et notre jeu
jeu = Jeu()

running = True
clock = pg.time.Clock()

#Boucle tant que cette condition est vraie
while running:

    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0,0))

    #vérifier si le jeu à commencé
    if jeu.is_playing_harry:
        jeu.update(screen, harry)
    elif jeu.is_playing_hermione:
         jeu.update(screen, hermione)
    elif jeu.is_playing_drago:
         jeu.update(screen, drago)
    elif jeu.choose_character:
        screen.blit(harry, harry_rect)
        screen.blit(hermione, hermione_rect)
        screen.blit(drago, drago_rect)
    else:
        screen.blit(banniere, (200, 100))
        #screen.blit(bouton_play, bouton_play_rect)
        screen.blit(bouton_character, bouton_character_rect)
        

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
            #if bouton_play_rect.collidepoint(event.pos): #event.pos récupère la position de la souris
                #jeu.start()
            if bouton_character_rect.collidepoint(event.pos):
                jeu.choose_character = True
            if harry_rect.collidepoint(event.pos):
                    jeu.choose_character = False
                    jeu.start_harry()
            elif hermione_rect.collidepoint(event.pos):
                    jeu.choose_character = False
                    jeu.character = pg.image.load('hermione2.png')
                    jeu.start_hermione()
            elif drago_rect.collidepoint(event.pos):
                    jeu.choose_character = False
                    jeu.character = pg.image.load('drago2.png')
                    jeu.start_drago()
                       


            