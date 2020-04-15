# list.py

students = [] # liste vide
print(type(students)) # <class 'list'>

fruits = ['Pomme', 'Cerise', 'Fraise']

# les listes sont facilement itérables avec la boucle for
for fruit in fruits:
    print(fruit)

print("Premier fruit:", fruits[0]) # affiche Pomme