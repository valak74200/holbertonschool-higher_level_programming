#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Cette fonction prend une liste en entrée et retourne la somme de tous ses éléments uniques

    # Utilisation de set() pour obtenir les éléments uniques, puis sum() pour les additionner
    return sum(set(my_list))
    # 1. set(my_list) : Crée un ensemble (set) à partir de my_list, éliminant ainsi les doublons
    # 2. sum(...) : Calcule la somme de tous les éléments de l'ensemble
    # Le résultat est la somme de tous les éléments uniques de la liste
