
def my_sort(liste):
    
    coups = 0

    
    for i in range(len(liste)):
       
        for j in range(len(liste) - 1):
            if liste[j] > liste[j + 1]:
               
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

               
                coups += 1

   
    print("Nombre total de coups nécessaires pour trier la liste :", coups)

   
    return liste


nombres = [64, 34, 25, 12, 22, 11, 90]

print("Liste triée :", my_sort(nombres))
