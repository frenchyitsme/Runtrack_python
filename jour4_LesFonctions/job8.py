#   Créer une fonction qui prend 2 paramètres :

#       ➔ Le premier reçoit un String nommé « type »
#       ➔ Le second reçoit un String nommé « saison »

#   Si la valeur de « type » est égale à « fruits » et que celle de saison est égale à «hiver », affichez « orange, mandarine et kiwi »
#   Si la valeur de « type » est égale à « fruits » et que celle de saison est égale à «été », affichez « Poire, fraise, cassis »
#   Si la valeur de « type » est égale à « légume » et que celle de saison est égale à « hiver », affichez « carotte, topinambour, endive »
#   Si la valeur de « type » est égale à « légume » et que celle de saison est égale à « été », affichez « artichaut, aubergine,navet ».

def market(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")

    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")

    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")


market("fruits", "hiver")
market("fruits", "été")
market("légume", "hiver")
market("légume", "été")