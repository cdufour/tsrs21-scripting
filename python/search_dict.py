# search_dict.py

# liste de dictionnaires, chaque dico représente un étudiant
students = [
    {"name": "Melvin", "group":"TSRS21"},
    {"name": "Franck", "group":"TSRS21"},
    {"name": "Toto", "group":"TSRS19"},
    {"name": "Machin", "group":"TSRS19"},
    {"name": "Emilie", "group":"TSRS21"}
]

# on récupère la saisie utilisateur
num_group = input("Numéro du groupe TSRS: ")
found = False

for student in students:
    if student["group"] == "TSRS" + num_group:
        print(student["name"])
        found = True # un étudiant a été trouvé pour le groupe fourni

if found == False:
    print("Aucun étudiant trouvé pour le groupe indiqué")