#   Écrire un programme qui calcule le produit de toutes les valeurs de la liste
#   comprises dans l’intervalle [25, 90].
#   
#   L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

#   L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
#   i = 0
#   
#   for i in L:
#   
#   if i <= 90 and i >= 25:
#   
#   print(i)


#if i > 25 :
#    print(L)
#
#elif i < 90:
#    print(L)
#
#else :
#    print("no")



L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

val = 1

for nbr in L:
    if nbr >= 25 and nbr <= 90:
        val = val * nbr

print("Le produit est", val)
