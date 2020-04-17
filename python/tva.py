# tva.py
def calculeTTC(ht):
    # TVA = montant HT multiplie par taux de tva
    # TTC = TVA + montant HT
    return (ht * 0.2) + ht

def ask_input():
    try:
        ht = float(input("Montant HT: "))
        ttc = calculeTTC(ht)
        print(ttc)
    except:
        print('Saisie incorrecte, impossible de calculer le montant TTC')
        ask_input()

ask_input()

# prix_ht = [100.0, 78.2, 40.9, 560.0, 14.25]
# for prix in prix_ht:
#     ttc = calculeTTC(prix)
#     #print("Prix HT", prix, "=> prix TTC", ttc)
#     # variante syntaxique de la fonction print
#     print(f"Prix HT: {prix} => prix TTC: {ttc}")