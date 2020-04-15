# loop.py

# name = input('Votre prénom: ')
# loops = int(input('Nombre de fois à afficher: '))
# while loops > 0:
#     print(name)
#     loops -= 1

name = input('Votre prénom: ')
loops = int(input('Nombre de fois à afficher: '))
MAX = 100 # constante (écrite en majuscule par convention)
# principe: une constante n'est utilisée qu'en lecture,
# elle ne doit pas être modifié en cours d'execution du script

if loops <= MAX:
    while loops > 0:
        print(name)
        loops -= 1
else:
    print("Ce script n'accepte pas d'itérer plus de", MAX, "fois")