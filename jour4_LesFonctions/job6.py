#   Créer une fonction qui prend en paramètre un nombre nommé « nombre ».
#   Afficher « positif » si le nombre est supérieur à 0.
#   Afficher « négatif » si le nombre est inférieur à 0.
#   Appeler cette fonction plusieurs fois en y passant des paramètres différents pour afficher ces résultats.

#def nombre(nombre):
#
#    if nombre < 0:
#    print "Positif"
#
#    else nombre > 0:
#    print "Negatif"
#    
#   nombre= 5

# CORRECTION ----------------------------------------------

def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")


verifier_nombre(5)
verifier_nombre(-3)
verifier_nombre(12)
verifier_nombre(-8)

