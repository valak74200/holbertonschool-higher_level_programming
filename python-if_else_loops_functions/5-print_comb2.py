#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

# Boucle for qui va de 0 à 98 inclus
# Les nombres seront affichés avec un format spécial
for i in range(0, 99):
    # {:02d} est un code de formatage qui signifie:
    # - d : format décimal
    # - 2 : utiliser 2 positions
    # - 0 : remplir avec des zéros à gauche
    # end=", " : ajoute une virgule et un espace après chaque nombre au lieu d'un retour à la ligne
    print('{:02d}'.format(i), end=", ")

# Affiche le dernier nombre (99) sans virgule à la fin
print('99')
