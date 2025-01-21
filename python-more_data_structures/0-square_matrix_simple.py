#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Cette fonction prend une matrice en entrée et retourne une nouvelle matrice
    # où chaque élément est le carré de l'élément correspondant dans la matrice d'origine

    # Utilisation d'une liste en compréhension pour créer la nouvelle matrice
    return [[i ** 2 for i in row] for row in matrix]
    # Pour chaque ligne (row) dans la matrice d'entrée :
    #   - Crée une nouvelle liste
    #   - Pour chaque élément (i) dans cette ligne :
    #     - Calcule le carré de cet élément (i ** 2)
    #     - Ajoute ce carré à la nouvelle liste
    # Le résultat est une nouvelle matrice avec les mêmes dimensions que l'originale,
    # mais avec tous les éléments élevés au carré
