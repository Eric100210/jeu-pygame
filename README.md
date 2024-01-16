Projet : Jeu Harry Potter - Kill the dementors

Développeurs : Eric Kabis de Saint Chamas, Anne-Gabrielle Gibeili

Comment lancer le jeu : depuis le terminal, lancez le fichier main.py (python main.py), ou exécutez directement le fichier main.py depuis VS Code.

Principe du jeu : Plongez dans le monde magique d'Harry Potter, choisissez votre sorcier préféré et luttez contre les forces du mal en éliminant les détraqueurs qui vous attaquent. Tentez de vaincre Voldemort qui fait son apparition régulièrement pour vous anéantir.

Fonctionnalités : 
- écran d'accueil, avec bouton pour lancer le jeu en choisissant son personnage
- gameplay : flèches directionnelles pour se déplacer dans les quatre directions possibles, bouton Espace pour lancer un sortilège
- le jeu s'arrête lorsque vous avez tué Voldemort (au bout d'un certain nombre de fois son apparition), ou lorsque vous n'avez plus de vie


Difficultés rencontrées : 
- gérer l'organisation du projet, qui se décompose en plusieurs fichiers qui comportent chacun une classe d'objets, donc gérer les liens entre les différents attributs de chacun des objets
- gérer les collisions : 
    - on a appris à utiliser les sprite.Group pour utiliser la fonction collision des sprites
    - s'arranger pour que notre joueur ne puisse plus bouger vers la droite s'il y a un ennemi à sa droite, ne puisse plus monter s'il y a un ennemi au-dessus...
- gestion de l'aléatoire pour l'apparition des bonus