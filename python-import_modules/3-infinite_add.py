#!/usr/bin/python3
# Cette ligne indique que le script doit être exécuté avec l'interpréteur Python 3

if __name__ == "__main__":
    # Cette condition vérifie si le script est exécuté directement (et non importé comme module)

    from sys import argv
    # Importe le module 'argv' de la bibliothèque système pour accéder aux arguments de ligne de commande

    result = 0
    # Initialise la variable 'result' à 0, qui servira à stocker la somme des arguments

    argument = len(argv) - 1
    # Calcule le nombre d'arguments passés en ligne de commande (en excluant le nom du script)

    if argument > 0:
        # Vérifie s'il y a au moins un argument passé

        for i in range(1, len(argv)):
            # Boucle sur tous les arguments, en commençant par l'index 1 (le premier argument réel)

            result += int(argv[i])
            # Convertit chaque argument en entier et l'ajoute à la somme totale

        print("{}".format(result))
        # Affiche le résultat de la somme

    else:
        # Si aucun argument n'a été passé

        print("{}".format(result))
        # Affiche 0 (la valeur initiale de 'result')
