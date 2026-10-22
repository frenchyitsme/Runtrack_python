#   Dans un premier temps, créer un dossier jour7-8, afin d’y mettre l’ensemble des fichiers du jour 6 de la runtrack Python.
#   
#   Écrire un programme qui affiche dans la console un rectangle avec des « - » et des « | » en fonction des paramètres d’entrées, (width, height), par
#   exemple :
#   draw_rectangle(10, 3) :


#   FONCTION draw_rectangle(width, height)
#   
#       POUR chaque ligne de 0 à height - 1
#   
#           SI ligne est égale à 0 OU ligne est égale à height - 1 ALORS
#               AFFICHER width tirets
#           SINON
#               AFFICHER une barre verticale,
#               puis des espaces,
#               puis une barre verticale
#           FIN SI
#   
#       FIN POUR
#   
#   FIN FONCTION


def draw_rectangle(width, height):
    for ligne in range(height):
        if ligne == 0 or ligne == height - 1:
            print("-" * width)
        else:
            print("|" + " " * (width - 2) + "|")

draw_rectangle(10, 3)
