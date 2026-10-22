# 
# !! CORRECTION !!
# 

#--- Job2 -------------------------------------------------------------------------------


#   Imput utilisateur
#   
#   On stock l'input dans une variable pour la taille du triangle (taille = hauteur du triangle)
#   nombre de "_" = 2 * taille - 2 -> OK
#   Si c'est la dernière ligne, on affiche les symboles de la dernière ligne en utilisant la formule précédente
#   Si on est sur une ligne au milieu, on utilise la formule précédente pour afficher les espaces
#   Le nombre d'espaces avant et après est égal à la taille - la ligne actuelle 



#Cette fonction dessine un triangle de taille "size"
def draw_triangle(size):

    # On itère un nombre de fois égal à la taille, du coup pour chaque ligne
    for i in range(size):
        space_size = size - i + 1
        print(" " * (space_size - 1) + "/" + " " * (2 * i - 2) + "\\" + " " * (space_size - 1))

    print("/" + "_" * (size * 2 - 2) + "\\")

draw_triangle(5)