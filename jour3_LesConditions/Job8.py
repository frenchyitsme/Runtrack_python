#   Créez un programme qui demande à l’utilisateur trois longueurs, a, b, c. 
#   À l’aide de ces trois longueurs, déterminez s’il est possible de construire un triangle. 
#   Déterminez ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque.
#   Attention : un triangle rectangle peut être isocèle.


a = int(input("Longueur a : "))
b = int(input("Longueur b : "))
c = int(input("Longueur c : "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Triangle impossible")

else:
    if a == b == c:
        print("Triangle équilatéral")

    if a == b or a == c or b == c:
        print("Triangle isocèle")

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Triangle rectangle")

    if a != b and a != c and b != c:
        if a**2 + b**2 != c**2 and a**2 + c**2 != b**2 and b**2 + c**2 != a**2:
            print("Triangle quelconque")
