inventory = [
    {"nom": "Stylo" , "prix unitaire": 2, "quantité": 6},
    {"nom": "Cahier" , "prix unitaire": 3, "quantité": 4},
    {"nom": "Sacoche" , "prix unitaire": 5, "quantité": 7},
    {"nom": "Effaceur" , "prix unitaire": 1, "quantité": 9},
    {"nom": "Gomme" , "prix unitaire": 3, "quantité": 7} ]

print (inventory)



*correction



# Création des 5 articles
articles = [
    {"nom": "Ordinateur", "prix": 800.0, "stock": 10},
    {"nom": "Téléphone", "prix": 500.0, "stock": 15},
    {"nom": "Clavier", "prix": 40.0, "stock": 20},
    {"nom": "Souris", "prix": 25.0, "stock": 30},
    {"nom": "Écran", "prix": 200.0, "stock": 8}
]

# Gestion de chaque article
for article in articles:
    print("\n---", article["nom"], "---")
    print(f"Prix unitaire : {article['prix']:.2f} €")
    print("Quantité en stock :", article["stock"])

    # Ajouter des articles au stock
    ajout = int(input("Combien d'articles souhaitez-vous ajouter ? "))
    if ajout >= 0:
        article["stock"] += ajout
    else:
        print("Quantité invalide.")

    # Acheter des articles
    achat = int(input("Combien d'articles souhaitez-vous acheter ? "))
    if 0 <= achat <= article["stock"]:
        article["stock"] -= achat
        print("Achat effectué.")
    else:
        print("Stock insuffisant ou quantité invalide.")

    # Augmentation du prix de 10 %
    article["prix"] *= 1.10

# Affichage final des 5 articles
print("\n===== INVENTAIRE FINAL =====")

for article in articles:
    print(f"\nNom : {article['nom']}")
    print(f"Prix unitaire : {article['prix']:.2f} €")
    print(f"Quantité en stock : {article['stock']}")
