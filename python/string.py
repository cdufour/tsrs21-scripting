# string.py

print(len("chris")) # Affiche 5
filename = "apache.log"

# Slicing, extraction de portions (tranches) de chaîne
print(filename[0:3]) # Affiche apa
print(filename[0:]) # apache.log
print(filename[4:]) # he.log

print(filename[0:-4]) # apache
print(filename[:-4]) # apache

print(filename[-3:]) # log

# utitilisation de la méthode upper() sur 
# l'ensemble ou sur une portion de la chaîne
print(filename.upper()) # APACHE.LOG
print(filename[-3:].upper()) # LOG