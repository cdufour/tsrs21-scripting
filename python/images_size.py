# images_size.py

'''
Créer un script qui affiche le nom et la taille des images
du dossier fichiers-loup
'''

import os

target_dir = 'fichiers-loup'

for fi in os.listdir(target_dir):
    filesize = os.path.getsize(target_dir + '/' + fi)
    #print(fi, " => ", filesize, 'octets')
    print(fi, " => ", round(filesize/1000), 'ko')