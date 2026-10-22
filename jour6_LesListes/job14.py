
def my_long_word(nombre, phrase):
    mots = phrase.split()
    resultat = []

    for mot in mots:
        compteur = 0

        for lettre in mot:
            compteur += 1

        if compteur > nombre:
            resultat.append(mot)

    return " ".join(resultat)


phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, phrase))



#faux ! on ne doit pas utilisé de append

