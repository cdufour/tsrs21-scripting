# generate_files.py

students = ['Gabriele', 'Alessandro', 'Anca', 'Chris']
for student in students:
    filename = 'students/' + student + '.txt'
    f = open(filename, 'w')
    print("Le fichier", filename, "a été créé")
    f.close()
print(len(students), "fichiers ont été crées")