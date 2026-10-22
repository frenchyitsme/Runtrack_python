#   Créez un programme qui affiche dans le terminal tous les nombres de 0 à 100
#       compris SAUF 26, 37, 88.

i= 0

while i <= 100:
    if i != 26 and i != 37 and i != 88:
        print(i)
    i = i + 1
