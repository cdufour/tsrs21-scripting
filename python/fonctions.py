# fonctions.py

# definition de la fonction
def byteToKbyte(nb_bytes):
    # corps de ma fonction
    #print("Je suis une fonction")
    #print(nb_bytes / 1000.0)
    return nb_bytes / 1000.0

byteToKbyte(500) # appel de la fonction sans affichage de son retour
print(byteToKbyte(6000)) # appel de la fonction et affichage de son retour

# appel de la fonction et stockage du retour dans une variable
ko = byteToKbyte(48200) 
print(ko) # affichage de la variable