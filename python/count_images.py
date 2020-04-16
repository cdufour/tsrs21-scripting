# count_images.py

''' Créer un script comptant les images situées dans un dossier cible '''

# 1. Importer le module os
import os


# 2. Créer une variable qui permettra de compter le nombre d'images trouvées
nb_images = 0

# création d'un tuple contant les extensions de type image
img_extensions = ('png', 'jpg', 'jpeg', 'gif')


# 3.  Récupérer dans une variable la liste des fichiers du dossier cible. Utiliser os.listdir
files = os.listdir('fichiers-loup')

# 4. Parcourir les fichiers récupérés. Lorsque le nom du fichier se termine par :
# jpeg ou jpg ou gif ou png, augmenter d'une unité la variable créée à l'étape 2.
# Astuce: utiliser la méthode .endswith disponible pour toute chaîne de caractères python
# afin déterminer récupérer l'extension du fichier.
# exemple: "loup1.png".endswith("txt") renvoie False mais "loup1.pdf".endswith("png") renvoie True
for fi in files:
    #if fi.endswith('png') or fi.endswith('jpg') or fi.endswith('jpeg') or fi.endswith('gif'):
    # variante, en utilisant un tuple de valeurs:
    if fi.endswith(img_extensions): # endswith comparera la fin du nom avec chaque valeur du tuple  
        nb_images += 1


# 5. En sortie de boucle, afficher le nombre d'images trouvées
print(nb_images, "images trouvées")