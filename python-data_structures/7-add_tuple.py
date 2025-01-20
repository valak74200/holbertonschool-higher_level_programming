#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()): # Définition de la fonction avec deux tuples vides comme arguments par défaut
    tuple_a = tuple_a + (0, 0)[:2] # Ajoute (0, 0) à tuple_a et prend les 2 premiers éléments pour assurer au moins 2 éléments
    tuple_b = tuple_b + (0, 0)[:2] # Ajoute (0, 0) à tuple_b et prend les 2 premiers éléments pour assurer au moins 2 éléments
    a = tuple_a[0] + tuple_b[0] # Additionne les premiers éléments de tuple_a et tuple_b
    b = tuple_a[1] + tuple_b[1] # Additionne les deuxièmes éléments de tuple_a et tuple_b
    new = (a, b) # Crée un nouveau tuple avec les résultats des additions
    return new # Retourne le nouveau tuple
