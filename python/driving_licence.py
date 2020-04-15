# driving_licence.py

age = int(input("Donne ton âge: "))

if age >= 18:
    print("Tu passer le permis")
else:
    if age < 16: # si strictement inférieur à 16
        print("Tu ne peux pas passer le permis")
    else: # supérieur ou égal à 16 mais inférieur à 18 (16 ou 17)
        print("Tu peux passer la conduite accompagnée")
    