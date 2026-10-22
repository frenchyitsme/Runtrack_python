#   Créer une fonction nommée « calcule » qui prend 3 paramètres :
#       ➔ Le premier, « num1 », est un nombre,
#       ➔ Le deuxième, « operator », est un caractère (string) contenant le type d’opération(+, -, *, /, %),
#       ➔ Le troisième, « num2 », est un nombre.
#   La fonction doit retourner le résultat de l’opération.


#   --------------------------------------------------------------------------------------

#               def calcule(num1,operator,num2):
#                   print("numéro 1", num1)
#                   print("+, -, *, /, %",operator)
#                   print("numéro 2", num2)
#               
#                   calcule(2+8)
#               
#               result = calcule()
#               
#               print(result)
#
#
#   CORRECTION --------------------------------------------------------------------


def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2


print(calcule(10, "+", 5))
print(calcule(10, "-", 5))
print(calcule(10, "*", 5))
print(calcule(10, "/", 5))
print(calcule(10, "%", 3))
