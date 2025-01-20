#!/usr/bin/python3
def replace_in_list(my_list, idx, element): # Définition de la fonction avec trois paramètres : my_list, idx et element
    a = len(my_list) # Calcule la longueur de my_list et stocke le résultat dans la variable a
    if idx < 0: # Vérifie si l'index est négatif
        return my_list # Si l'index est négatif, retourne la liste originale sans modification
    if idx >= a: # Vérifie si l'index est supérieur ou égal à la longueur de la liste
        return my_list # Si l'index est hors limites, retourne la liste originale sans modification
    my_list[idx] = element # Remplace l'élément à l'index idx par le nouvel élément
    return my_list # Retourne la liste modifiée
