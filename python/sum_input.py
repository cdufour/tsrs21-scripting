# sum_input.py

'''
Créer un script demandant à l'utilisateur de saisir
un chiffre tant que la somme des chiffres précédemment saisis
est inférieure à 100

exemple:
10
60
10
30 => 10 + 60 + 10 + 30 = 110 > 100 => sortie de boucle
'''

sum = 0 # variable de cumul initialisée à 0
while sum < 100:
    nb = int(input("Saisir un entier positif: "))
    sum = sum + nb # accumulation
print("Cumul des valeurs saisies:", sum)