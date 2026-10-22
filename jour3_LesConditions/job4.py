#   Écrire un programme qui itère les nombres entiers de 1 à 100.
#   Pour les multiples de trois, affichez « Fizz » au lieu du nombre et pour les multiples de cinq, affichez « Buzz ». # 
#   Pour les nombres qui sont des multiples de trois et de cinq, affichez « FizzBuzz »

i = 1

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

    i += 1