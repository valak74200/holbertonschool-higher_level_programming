#!/usr/bin/python3
"""Imprime un carré avec le caractère #."""


def print_square(size):
    """Imprime un carré avec le caractère #.

    Args:
        size (int): La taille du carré à imprimer

    Raises:
        TypeError: Si size n'est pas un entier
        ValueError: Si size est inférieur à 0
    """
    # Vérifie si size est un entier
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Vérifie si size est négatif
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Cette condition semble redondante et pourrait être supprimée
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    # Boucle pour imprimer chaque ligne du carré
    for i in range(size):
        # Imprime une ligne de '#' répétée 'size' fois
        print("#" * size)
