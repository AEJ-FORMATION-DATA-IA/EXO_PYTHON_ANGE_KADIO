"""
Programme permettant de faire la somme de deux nombres entiers saisi par l'utilisateur
"""

nombre1 = input("Veuillez saisir un nombre entier : ")

try:
    nombre1 = int(nombre1)
except ValueError:
    print("Vous avez fait une erreur !")
else:
    nombre2 = input("Veuillez saisir un second nombre : ")
    try:
        nombre2 = int(nombre2)
    except:
        print("Vous avez fait une erreur !")
    else:
        print(f"{nombre1} + {nombre2} = {nombre1+nombre2}")