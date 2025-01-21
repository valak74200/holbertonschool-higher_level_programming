#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Cette fonction met à jour un dictionnaire avec une nouvelle paire clé-valeur
    # ou met à jour la valeur si la clé existe déjà

    # Mise à jour ou ajout de la paire clé-valeur dans le dictionnaire
    a_dictionary[key] = value
    # Si la clé existe déjà, sa valeur est mise à jour
    # Si la clé n'existe pas, une nouvelle paire clé-valeur est ajoutée

    # Retourne le dictionnaire mis à jour
    return a_dictionary
