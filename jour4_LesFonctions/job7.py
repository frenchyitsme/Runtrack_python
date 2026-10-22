#   Créez une fonction qui prend en paramètre une String nommée « langage ».

#   Si la valeur de « langage » est égale à « JavaScript » affichez : « tu es un développeur web »
#   Sinon si la valeur de « langage » est égale à « python » affichez : « tu es un développeur IA »
#   Sinon si la valeur de « langage » est égale à « java » affichez : « tu es un développeur logiciel »
#   Sinon, si la valeur de « langage » est égale à « reactjs » affichez : « tu es un développeur mobile »
#   Sinon, affichez : « un jour, je serai le meilleur développeur... »

#   Créez un fichier Python nommé job07.py, écrivez votre programme dans ce fichier, puis testez votre programme.

def lang(langage):

    if langage == "JavaScript":
        return "Tu es un dev web"

    elif langage == "python":
        return "Tu es un dev IA"

    elif langage == "java":
        return "Tu es un dev logiciel"

    elif langage == "reactjs":
        return "Tu es un dev mobile"

    else:
        return  "Un jour je serais meilleur développeur..."

print(lang("java"))
print(lang("python"))
print(lang("JavaScript"))
print(lang("nothing"))
print(lang("reactjs"))
