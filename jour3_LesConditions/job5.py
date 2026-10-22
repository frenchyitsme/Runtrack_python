# Écrire un programme qui affiche les nombres premiers jusqu’à 1000.

i = 2

while i <= 1000:
    x = 2
    y = True

    while x < i :
        if i % x == 0:
            y = False
            break
        x += 1

    if y:
        print(i)

    i += 1
