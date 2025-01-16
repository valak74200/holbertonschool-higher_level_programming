#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

# La boucle for avec range(0, 99):
# - Commence à 0 (inclus)
# - Se termine à 98 (99 exclus)
# - i prend chaque valeur une par une
for i in range(0, 99):
    # print() affiche du texte dans la console
    # .format() remplace les {} par les valeurs entre parenthèses
    # hex(i) convertit le nombre i en hexadécimal
    # Le premier {} est remplacé par i (décimal)
    # Le deuxième {} est remplacé par hex(i) (hexadécimal)
    print("{} = {}".format(i, hex(i)))
