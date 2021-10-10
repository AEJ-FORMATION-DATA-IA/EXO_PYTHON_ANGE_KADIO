"""
Programme permettant de faire la somme de deux nombres entiers saisi par l'utilisateur
"""

a = input("Veuillez saisir un nombre entier : ")

try:
    a = int(a)
except ValueError:
    print("Vous avez fait une erreur !")
else:
    b = input("Veuillez saisir un second nombre : ")
    try:
        b = int(b)
    except:
        print("Vous avez fait une erreur !")
    else:
        if a>b:
            print(f"{a} est supérieur à {b}")
        elif a<b:
            print(f"{a} est inférieur à {b}")
        else:
            print(f"{a} est égal à {b}")