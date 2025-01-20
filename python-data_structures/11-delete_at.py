#!/usr/bin/python3
def delete_at(my_list=[], idx=0): # Définition de la fonction avec une liste vide et un index 0 comme arguments par défaut
    if idx < 0 or idx >= len(my_list): # Vérifie si l'index est négatif ou hors de la plage de la liste
        return my_list # Si l'index est invalide, retourne la liste sans modification
    del my_list[idx] # Supprime l'élément à l'index spécifié de la liste
    return my_list # Retourne la liste modifiée
