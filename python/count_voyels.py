# count_voyels.py

'''
Créer un script python affichant le nombre de caractères et le nombre
de voyelles trouvés dans le fichier lorem.txt.
Le script affichera également le pourcentage de voyelle que cela représente
'''

f = open('lorem.txt', 'r')
text = f.read()
voyels = ('a','e','i','o','u','y')
nb_voyels = 0
nb_char = 0

for c in text:
    nb_char += 1
    if c.lower() in voyels:
        nb_voyels += 1

print("Nombre de caractères:", nb_char)
print("Nombre de voyelles:", nb_voyels)
print("Pourcentage de voyelles:", (nb_voyels/nb_char) * 100)