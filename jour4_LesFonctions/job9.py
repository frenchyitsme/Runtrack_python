#  Créez une fonction nommée « moyenne » qui prend en paramètre trois notes et retourne la moyenne de ces notes.
#       
# Demandez à l'utilisateur de saisir trois notes, puis enregistrez le résultat de la
#       fonction « moyenne » dans une variable appelée « moyenne_etudiant ».
#       Afficher ensuite la phrase suivante en fonction de la moyenne de l’étudiant :
#       
#       ➔ Très bon élève si la moyenne est comprise entre 20 et 15.
#       ➔ Bon élève si la moyenne est comprise entre 14 et 11.
#       ➔ Élève moyen si la moyenne est comprise entre 10 et 8.
#       ➔ Élève devant faire des efforts si la moyenne est comprise entre 0 et 7.


def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3


note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant >= 15:
    print("Très bon élève")
elif moyenne_etudiant >= 11:
    print("Bon élève")
elif moyenne_etudiant >= 8:
    print("Élève moyen")
elif moyenne_etudiant >= 0:
    print("Élève devant faire des efforts")
else:
    print("Moyenne invalide")
