#!/usr/bin/python3
"""Fonction qui imprime Mon nom est <prénom> <nom>."""


def say_my_name(first_name, last_name=""):
    """Imprime Mon nom est <prénom> <nom>."""
    # Vérifie si first_name est une chaîne de caractères
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Vérifie si last_name est une chaîne de caractères
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Imprime le nom complet
    print("My name is {} {}".format(first_name, last_name))
