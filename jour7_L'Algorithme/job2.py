def draw_triangle(height):
    for ligne in range(height):
        if ligne == height - 1:
            interieur = "_" * (2 * ligne)
        else:
            interieur = " " * (2 * ligne)

        print(" " * (height - ligne - 1) + "/" + interieur + "\\") 

draw_triangle(5)