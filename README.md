#JEU D'ECHECS PAR ALLAN ET RIYAD


###Lancer une Partie

-Pour lancer le jeu, ouvrez un terminal (sa marche sur windows et linux) et lancez la commande 'python main.py'. Si vous recevez une erreur relative a l'UTF-8, essayez 'python3 main.py'
-Notez que les déplacements se font avec une paire de chiffres, et non avec une paire lettre,chiffre


###Code

#####-Le code se divise en 4 fichiers différents
      -Le fichier 'main.py', qui ne contient rien d'intéressant
      -Le fichier 'game.py', qui permet de gérer l'affichage dans le terminal et la GameLoop
      -Le fichier 'echiquier.py', qui permet de créer un échiquier 8×8 avec un systeme de déplacement Cartésien (c'est a dire avec (0, 4), et non e4 par exemple)
      -Le fichier 'pieces.py', qui permet de créer des pieces avec une classe parent 'piece', et de spécialiser ces pieces graces aux classes qui héritent de celle-ci
