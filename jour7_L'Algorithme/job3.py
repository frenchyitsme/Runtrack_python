#   Écrire une fonction qui, recevant une taille n en paramètre, 
#   affiche un tapis de n+1 ligne/n+1 colonne traversé par une diagonale.
#   Exemple pour une taille de 10 :




def draw_tapis(n):
    print("+" + "-" * (n + 1) + "+")

    for ligne in range(n + 1):
        if ligne == 0:
            interieur = "#" * (n + 1)
        else:
            interieur = "#" * (n - ligne) + " " + "#" * ligne

        print("|" + interieur + "|")

    print("+" + "-" * (n + 1) + "+")


draw_tapis(10)
