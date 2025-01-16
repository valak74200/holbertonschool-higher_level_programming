#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

# Boucle de 122 ('z') à 97 ('a') en décrémentant de 1
# range(122, 96, -1) signifie:
# - Commence à 122 (inclus)
# - Termine à 96 (exclus)
# - Pas de -1 (compte à rebours)
for c in range(122, 96, -1):
    # Si le code ASCII est impair
    # On convertit en majuscule en soustrayant 32
    # (différence entre minuscules et majuscules en ASCII)
    if c % 2 != 0:
        c = c - 32
    
    # chr() convertit le code ASCII en caractère
    # end='' évite d'ajouter un retour à la ligne
    print("{}".format(chr(c)), end='')
