#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Cette fonction supprime une paire clé-valeur d'un dictionnaire si la clé existe

    # Vérifie si la clé existe dans le dictionnaire
    if key in a_dictionary:
        # Si la clé existe, on la supprime du dictionnaire
        del a_dictionary[key]
    
    # Retourne le dictionnaire (modifié ou non)
    return a_dictionary
