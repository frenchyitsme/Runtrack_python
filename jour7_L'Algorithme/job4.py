#   Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses messages. 
#   Sa méthode était assez simple : il décalait les lettres de trois rangs dans l'alphabet.
#   
#   Créer une fonction à laquelle on donne un message et un décalage, et la fonction renvoie alors le message décalé dans l'alphabet. 
#   Il faudra gérer le dépassement (« z » décalé vers la droite revient sur « a », et « a » décalé vers la gauche revient sur « z »).


def cesar(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""

    for lettre in message:
        if lettre in alphabet:
            position = alphabet.index(lettre)
            nouvelle_position = (position + decalage) % 26
            resultat = resultat + alphabet[nouvelle_position]
        else:
            resultat = resultat + lettre

    return resultat


print(cesar("bonjour", 3))
print(cesar("xyz", 3))
print(cesar("abc", -1))
