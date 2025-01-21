#!/usr/bin/python3

def safe_print_integer(value):
    # Définition de la fonction qui prend un paramètre 'value'
    
    try:
        # Début du bloc try pour gérer les exceptions potentielles
        
        print("{:d}".format(value))
        # Tente d'imprimer 'value' formaté comme un entier
        # {:d} force le formatage en entier
        
        return True
        # Si l'impression réussit, retourne True
    
    except Exception:
        # Capture toute exception qui pourrait se produire
        
        return False
        # Si une exception se produit, retourne False
