# min_max.py

notes = [11,7,19,14,4,10,16,12]

# Déterminer la valeur maximale
note_max = 0
for note in notes:
    # si la note itérée est supérieure à la valeur maximale
    # précente, cette note devient la nouvelle valeur maximale
    if note > note_max:
        note_max = note
print("Note maximale:", note_max)

# Déterminer la valeur minimale
note_min = note_max
for note in notes:
    if note < note_min:
        note_min = note
print("Note minimale:", note_min)   