# file_demo.py

# f = open('files/file1.txt', 'r') # accès au fichier en lecture
# content = f.read()
# print(content)

# accès en mode écriture, création d'un nouveau fichier
# si le fichier n'existe pas
f = open('files/file2.txt', 'w') 
# la méthode write permet d'écrire dans le fichier ouvert
f.write('Python est un excellent langage de programmation')
f.close() # on libère le fichier