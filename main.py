import pygame as pg
pg.init()
from jeu import Jeu 

#générer la fenêtre de notre jeu
pg.display.set_caption("Kill the dementors")
screen = pg.display.set_mode((1100,700))
background = pg.image.load('background.png')

#générer les graphiques à ajouter par-dessus la fenêtre
banniere = pg.image.load('logo_harrypotter.tiff')
bouton_character = pg.image.load('choose_character.png')
bouton_character = pg.transform.scale(bouton_character,(425,205))
bouton_character_rect = bouton_character.get_rect()
bouton_character_rect.x = bouton_character_rect.x + 350
bouton_character_rect.y = bouton_character_rect.y + 325

harry = pg.image.load('harry2.png')
harry_rect = harry.get_rect()
harry_rect.x = harry_rect.x+100
harry_rect.y = harry_rect.y+100
hermione = pg.image.load('hermione2.png')
hermione_rect = hermione.get_rect()
hermione_rect.x = hermione_rect.x+410
hermione_rect.y = hermione_rect.y+100
drago = pg.image.load('drago2.png')
drago_rect = drago.get_rect()
drago_rect.x = drago_rect.x + 720
drago_rect.y = drago_rect.y + 100

victoire = pg.image.load('victory.png')
defaite = pg.image.load('defeat.png')


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
        txt = pg.font.SysFont("Comic sans MS", 40)
        harry_txt = txt.render(f"Harry", 1, (255,255,255))
        screen.blit(harry_txt, (150,300))
        hermione_txt = txt.render(f"Hermione", 1, (255,255,255))
        screen.blit(hermione_txt, (450,300))
        drago_txt = txt.render(f"Drago", 1, (255,255,255))
        screen.blit(drago_txt, (800,300))
    elif jeu.defaite:
        screen.blit(defaite, (290,0))
        screen.blit(bouton_character, bouton_character_rect)
    elif jeu.victoire:
        screen.blit(victoire, (290,0))
        screen.blit(bouton_character, bouton_character_rect)
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
                if jeu.is_playing_drago or jeu.is_playing_harry or jeu.is_playing_hermione:
                    jeu.joueur.launch_spell()
                     

        elif event.type == pg.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            #savoir si on a cliqué sur le bouton play
            #if bouton_play_rect.collidepoint(event.pos): #event.pos récupère la position de la souris
                #jeu.start()
            if not (jeu.is_playing_drago or jeu.is_playing_harry or jeu.is_playing_hermione):
                if bouton_character_rect.collidepoint(event.pos):
                    jeu.choose_character = True
                    jeu.son.play('click')
                if jeu.choose_character :
                    if harry_rect.collidepoint(event.pos):
                        jeu.choose_character = False
                        jeu.start_harry()
                        jeu.son.play('click')
                    elif hermione_rect.collidepoint(event.pos):
                        jeu.choose_character = False
                        jeu.character = pg.image.load('hermione2.png')
                        jeu.start_hermione()
                        jeu.son.play('click')
                    elif drago_rect.collidepoint(event.pos):
                        jeu.choose_character = False
                        jeu.character = pg.image.load('drago2.png')
                        jeu.start_drago()
                        jeu.son.play('click')
                       


            