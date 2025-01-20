#!/usr/bin/python3
def element_at(my_list, idx): # Définition de la fonction avec deux paramètres : my_list et idx
    a = len(my_list) # Calcule la longueur de my_list et stocke le résultat dans la variable a
    if idx < 0: # Vérifie si l'index est négatif
        return None # Si l'index est négatif, retourne None
    if idx >= a: # Vérifie si l'index est supérieur ou égal à la longueur de la liste
        return None # Si l'index est hors limites, retourne None
    return my_list[idx] # Retourne l'élément de my_list à l'index idx
