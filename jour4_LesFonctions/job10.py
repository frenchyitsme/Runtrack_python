
def pair_ou_impair(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        print("Erreur : entrez un nombre entier positif.")
    elif nombre % 2 == 0:
        print("Le nombre est pair")
    else:
        print("Le nombre est impair")


pair_ou_impair(4)
pair_ou_impair(7)
pair_ou_impair(0)
pair_ou_impair(-3)
pair_ou_impair(5.5)
