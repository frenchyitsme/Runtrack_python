# Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.

L= ["pomme","cassis","pêche","poire","grenade","melon","pasteque"]


def trier_liste(L):
    L.sort()
    return L

nombres = [7, 2, 10, 4, 1]

print(trier_liste(nombres))
