# for.py

name = "Chris"

# la boucle for est appropriée dès lors qu'on souhaite parcourir
# un type de donné dit "itérable" (ayant un début et une fin)
# une chaîne de caractères est itérable
for c in name:
    print(c)

# équivalent avec une boucle while
index = 0
while index < 5:
    print(name[index]) # affiche le caractère situé à l'indice index

    index += 1 # incrémentation de l'index

# print(name[0]) # affiche C
# print(name[1]) # affiche h

# range -> [0, 99], range produit en ENSEMBLE de valeurs itérables
# for n in range(100):
#     print(n)

for n in range(10,15):
    print(n)



 