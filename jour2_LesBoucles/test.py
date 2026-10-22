#n = int(input("enter :"))
#for i in range(12):
#     for n in range(1, n * 2): 
#        i = i + 1
#        result = n + 2
#         print("Tour" , i , ":" , result ")


#CORRECTION


      
#for tour in range(1, 13):
#    result = tour * 2
#    print("Tour", tour, ":" , result)


#NEW EXERCICE ------------------------------------------------------------


nom = "Stylo"
prix = 2
stock = 10

valeur_stock = prix * stock

print(f"Produit : {nom}")
print(f"Prix unitaire : {prix} euros")
print(f"Quantité en stock : {stock}")
print(f"Valeur totale du stock : {valeur_stock} euros")

prenom = input("Comment t'appelles-tu ? ")

print(f"Bonjour {prenom} !")

age = int(input("Quel âge as-tu ? "))

print(f"Super tu as {age} ! ")

age2 = float(input("Quel age à ton fils ? En nombre décimal bien sur ! "))

print(f" Ton fils à {age2} c'est cool")

#   À  retenir :
#           - input() : récupérer une réponse sous forme de texte.
#           - int() : convertir en nombre entier.
#           - float() : convertir en nombre décimal.

age = int(input("Quel âge à ta mamie ? "))
demain = age + 1

print(f"Le 25 Novembre, ta mamie aura {demain} ans.")

age = int(input("Tu souhaites acheter une bierre, quel age as-tu ?"))

if age >= 18:
    print("Tu es majeur mon ptit bichon, tiens, voici ta binouse.")
else:
    print("Tu es mineur, tu n'en auras pas face de rat.")

#   if signifie « si ».
#   age >= 18 est la condition à vérifier.
#   else signifie « sinon ».
#   Les instructions décalées vers la droite sont les actions à exécuter dans chaque cas.

#   Symbole	Signification :                   Exemple : 

#       ==	Égal à	                               age == 18
#        !=	Différent de	                       age != 18
#        >	Supérieur à	                           age > 18
#        <	Inférieur à	                           age < 18
#        >=	Supérieur ou égal à	                   age >= 18
#       <=	Inférieur ou égal à	                   age <= 18

