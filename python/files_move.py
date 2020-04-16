# files_move.py

'''
Créer un script qui déplace dans le dossier "not-images"
tous les fichiers du dossier "fichiers-loup" qui ne sont
pas des images

Après l'exécution du script, les fichiers loup.pdf, loup.txt
et loup.xlsx devront se retrouver dans le dossier "not-images"
'''

import os

target_dir = './fichiers-loup'
ext = ('txt', 'pdf', 'xlsx')
nb_moved_files = 0

for fi in os.listdir(target_dir):
    if fi.endswith(ext):
        os.rename(target_dir + '/' + fi, target_dir + '/not-images/' + fi)
        nb_moved_files += 1

print(nb_moved_files, "fichiers déplacés")
