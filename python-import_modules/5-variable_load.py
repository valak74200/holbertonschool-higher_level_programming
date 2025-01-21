#!/usr/bin/python3
# Cette ligne indique que le script doit être exécuté avec l'interpréteur Python 3

if __name__ == "__main__":
    # Cette condition vérifie si le script est exécuté directement (et non importé comme module)

    from variable_load_5 import a
    # Importe la variable 'a' depuis le fichier 'variable_load_5.py'

    print("{}".format(a))
    # Affiche la valeur de la variable 'a' importée
