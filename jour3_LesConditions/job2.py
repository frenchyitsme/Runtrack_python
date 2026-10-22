#   Initialiser une variable contenant un chiffre entier représentant l'âge d’une personne. 
# Si la personne à au moins 18 ans, afficher “Tu peux voter” sinon “Tu ne peux pas voter”.

age = int(input("Quel est ton âge ?"))

if age >= 18:
    print("Tu peux voter")
else :
    print("Tu ne peux pas voter")

