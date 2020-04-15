# average.py
'''
Un étudiant a obtenu les notes suivantes durant l'année:
7,12,14,7,0,16,19

Créer un script affichant la moyenne des notes obtenues
par cet étudiant
'''

notes = [7,12,14,7,0,16,19]
total = 0
for note in notes:
    total += note
print("Moyenne de cet étudiant: ", total/len(notes))
