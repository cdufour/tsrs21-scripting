# iterations.py

loops = 5
while loops > 0:
    print("Passage dans la boucle")
    #loops = loops - 1
    loops -= 1 # dérémentation d'une unité
print("Sortie de boucle")

# loops va valoir successivement: 5, 4, 3, 2, 1, 0

start = 0
while start <= 10:
    print("start vaut: ", start)
    start += 1 # incrémentation d'une unité
print("Sortie de boucle")