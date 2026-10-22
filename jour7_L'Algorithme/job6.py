#   Luke Skywalker, un professeur de Math, fait passer un test et décide de noter
#   ses élèves sur une échelle allant de 0 à 100 inclus.
#   Si un étudiant obtient moins de 40 sur 100, il échoue au test.
#   S'il a plus de 40, il réussit le test. Luke est un professeur fort sympathique et
#   décide donc d’arrondir à la hausse les notes des étudiants ayant réussi le
#   test. Mais Luke n’est quand même pas trop gentil. Cet arrondi à la hausse ne
#   bénéficiera qu’aux étudiants remplissant certains critères, car tout de même,
#   il ne faut pas exagérer, sans blague.
#   
#   Le critère est simple : Si un étudiant a eu une note de moins de strictement 3
#   points de son prochain multiple de 5, alors sa note est arrondie à ce multiple
#   de 5. Par exemple, un 83 sera arrondi à 85 alors qu’un 82 restera un 82.
#   Pour simplifier le travail de Luke, écrivez une fonction qui prend en paramètre
#   une liste de notes et qui renvoie une liste de notes, arrondies comme il se doit,
#   quand cela est nécessaire.


#   def test(note):
#       if note > 40:
#           print("you win")
#       else :
#           print("you loose")
#   
#   def test(note2):
#       if note2 > 40:



#####################
#   CORRECTION      #
#####################


def arrondir_notes(notes):
    resultat = []

    for note in notes:
        if note >= 40:
            prochain_multiple = ((note // 5) + 1) * 5

            if prochain_multiple - note < 3:
                note = prochain_multiple

        resultat.append(note)

    return resultat


print(arrondir_notes([83, 82, 38, 57, 88, 67, 99]))
