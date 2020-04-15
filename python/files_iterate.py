# files_iterate.py
import os # importation du module os

# os.listdir renvoie la liste des noms de fichiers trouvés
# dans le dossier ciblde
files = os.listdir('files')

# on parcourt tous les fichiers situés dans le dossier cible
for filename in files:
    # a(ppend) écrit dans le fichier sans écraser l'ancien contenu
    # pour chaque fichier on ajoute la chaîne *** THE END *** à la fin
    # f = open('files/' + filename, '') 
    # f.write('\n*** THE END ***')
    # f.close()

    # Renommage du fichier, on change son extension
    new_name = filename[0:-4] + '.log'
    os.rename('files/' + filename, 'files/' + new_name)

