# Exercice de python

# Déclaration de a et b
a = 15
b = 4

# Calculs de a et b
c = a+b
print(f'Le résultat de {a} + {b} = {c}')
d = a*b
print(f'Le résultat de {a} x {b} = {d}')
e = a**b
print(f'Le résultat de {a} puissance {b} = {e}')
f = a/b
print(f'Le résultat de {a} / {b} = {f}')
g = a//b
print(f'Le résultat entier de {a} / {b} = {g}')
h = a%b
print(f'Le reste de {a} / {b} = {h}')

# Les dictionnaires
dictionnaire = {'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g}
dictionnaire['h'] = h
del dictionnaire['c']
#Affichage de la liste des clés
print("Liste des clés du dictionnaire : ")
for key in dictionnaire.keys():
    print(key)

# Affichage de la liste des valeurs
print("Liste des valeurs du dictionnaire : ")
for value in dictionnaire.values():
    print(value)

# Affichage de la liste clé/valeur du dictionnaire
print("Liste clé/valeur du dictionnaire : ")
for key,value in dictionnaire.items():
    print(f'{key} : {value}')

# Création de tuple
mon_tuple = (a,b,c)
mon_tuple = list(mon_tuple)
mon_tuple.append(d)
index_a = mon_tuple.index(a)
mon_tuple[index_a] = 16
mon_tuple.remove(b)
mon_tuple = tuple(mon_tuple)

# Création de litse
liste1 = ['A','B','C','D']
liste2 = [a,b,c,d]
liste3 = [liste1, liste2]
liste1.append('E')
liste1.append('F')
liste1.remove('B')
position = liste1.index('A')
liste1[position] = 'G'