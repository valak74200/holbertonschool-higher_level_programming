#!/usr/bin/python3
"""
Fonction qui additionne 2 entiers.

Retourne:
    int: la somme de a et b
"""


def add_integer(a, b=98):
    """
    Additionne 2 entiers.
    Calcule la somme de a et b.
    """
    # Vérifie si 'a' est un entier ou un flottant
    if isinstance(a, (int, float)) is False:
        # Lève une exception si 'a' n'est pas un entier ou un flottant
        raise TypeError("a must be an integer")
    
    # Vérifie si 'b' est un entier ou un flottant
    if isinstance(b, (int, float)) is False:
        # Lève une exception si 'b' n'est pas un entier ou un flottant
        raise TypeError("b must be an integer")
    
    # Retourne la somme de 'a' et 'b' convertie en entier
    return int(a + b)
