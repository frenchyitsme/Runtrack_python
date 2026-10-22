#   Écrivez un programme qui supprime les doublons de la liste suivante : [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40].
#L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
#
#L = list(set(L))
#
#print(L)
#
#


L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

def taille(L):
    a = 0
    for i in L :
        a += 1
    return a

a = 0
doub = []

while a < taille(L):
    if L[a] not in doub:
        doub.append(L[a])
    a+=1

print(doub)