#   Écrire un programme qui vérifie si un nombre renseigné par l’utilisateur est pair. 
#   Si le nombre est pair, afficher le message “Le nombre X est pair”.
#   Ajoutez ensuite à votre programme un message lorsque le nombre est impair.


#   CE QUE J'AI FAIS ----------------------------------------------------------------------------------



#   x = 1

#   while i <= 100 :
#   i = int(input("Ecrit un nombre pour savoir si il est pair ou impair :"))

#   if x = i % 2 == 0 : 
#        print("Le nombre " , {i} , "est pair")
#   else :
#       print("Le nombre ", {i} , "est impair")

#   i += 1


#   CORRECTION ----------------------------------------------------------------------------------------



i = int(input("Entrez un nombre : "))

if i % 2 == 0:
    print(f"Le nombre {i} est pair")
else:
    print(f"Le nombre {i} est impair")