#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Cette fonction prend deux ensembles en entrée et retourne un nouvel ensemble
    # contenant les éléments qui sont présents dans l'un des ensembles mais pas dans les deux

    # Utilisation de l'opérateur ^ pour calculer la différence symétrique entre les deux ensembles
    return set_1 ^ set_2
    # L'opérateur ^ (différence symétrique) entre deux ensembles retourne un nouvel ensemble
    # contenant tous les éléments qui sont dans set_1 ou set_2, mais pas dans les deux à la fois.
