# script python

# firewall est une variable de type str
firewall = "192.168.0.17"

nom = "Chris"  # type str
age = 120 # type int
tva = 5.5 # type float
contaminé = False # type bool

# Affichage
print(nom) # affiche le contenu de la variable
print("Formation Scripting") # affiche la chaîne de caractères

# Récupérer des saisies utilisateur
# saisie = input() # exemple: blabla

# Attention, la fonction input renvoie toujours un str
# il faut convertir la valeur en int si l'on souhaite faire des calculs
# avec la valeur saisie
saisie = int(input()) # conversion en int de la chaîne saisie
print("Valeur saisie: ", saisie) # affichage de la valeur saisie => blabla
print(type(saisie))
