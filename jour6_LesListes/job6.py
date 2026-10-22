# Écrire un programme qui échange les valeurs de la première et de la dernière case d’une liste quelconque non vide.

#   L = [1,2,3,4,5]
#   
#   def echang(L):
#       L[0] = 5
#       L[4] = 1
#   
#   echang(L)
#   
#   print(L)






L = [1, 2, 3, 4, 5]

print(L)

temp = L[0]
L[0] = L[-1]
L[-1] = temp

print(L)
