
def calcul_distance(marches, hauteur):
    distance = marches * hauteur * 2 * 5 * 7 / 100
    print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance:.2f} m par semaine.")


calcul_distance(50, 20)
