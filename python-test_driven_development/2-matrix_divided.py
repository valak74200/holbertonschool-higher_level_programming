#!/usr/bin/python3
"""Fonction qui divise tous les éléments d'une matrice."""


def matrix_divided(matrix, div):
    """Divise tous les éléments d'une matrice.

    Args:
        matrix (list): matrice à diviser
        div (int, float): nombre par lequel diviser

    Raises:
        TypeError: div doit être un nombre
        ZeroDivisionError: division par zéro
        TypeError: matrix doit être une matrice (liste de listes) d'entiers/flottants
        TypeError: Chaque ligne de la matrice doit avoir la même taille

    Returns:
        list: une nouvelle matrice avec le résultat de la division
    """
    # Vérifie si div est un entier ou un flottant
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Vérifie si div est égal à zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Vérifie si matrix est une liste de listes contenant uniquement des entiers ou des flottants
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float))
                    for num in [elem for row in matrix for elem in row]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    
    # Vérifie si la matrice n'est pas vide
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    
    # Vérifie si chaque ligne de la matrice n'est pas vide
    if not all(len(row) > 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    
    # Vérifie si toutes les lignes de la matrice ont la même longueur
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Crée une copie profonde de la matrice
    matrix_cpy = [row[:] for row in matrix]
    
    # Divise chaque élément de la matrice par div et arrondit à 2 décimales
    for i in range(len(matrix_cpy)):
        for j in range(len(matrix_cpy[i])):
            matrix_cpy[i][j] = round(float(matrix_cpy[i][j]) / div, 2)
    
    # Retourne la nouvelle matrice
    return matrix_cpy
