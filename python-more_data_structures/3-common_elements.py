#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Cette fonction prend deux ensembles en entrée et retourne un nouvel ensemble
    # contenant les éléments communs aux deux ensembles

    # Utilisation de l'opérateur & pour calculer l'intersection des deux ensembles
    return set_1 & set_2
    # L'opérateur & entre deux ensembles retourne un nouvel ensemble contenant
    # uniquement les éléments présents dans les deux ensembles d'origine
