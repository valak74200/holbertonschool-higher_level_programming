#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Cette fonction prend un dictionnaire en entrée et retourne un nouveau dictionnaire
    # où toutes les valeurs sont multipliées par 2

    # Utilisation d'une compréhension de dictionnaire pour créer un nouveau dictionnaire
    return {k: v * 2 for k, v in a_dictionary.items()}
    # Pour chaque paire clé-valeur (k, v) dans le dictionnaire d'origine :
    #   - La clé (k) reste inchangée
    #   - La valeur (v) est multipliée par 2
    # Le résultat est un nouveau dictionnaire avec les mêmes clés et les valeurs doublées
