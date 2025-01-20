#!/usr/bin/python3
def new_in_list(my_list, idx, element): # Définition de la fonction avec trois paramètres : my_list, idx et element
    a = len(my_list) # Calcule la longueur de my_list et stocke le résultat dans la variable a
    b = my_list.copy() # Crée une copie de my_list et la stocke dans la variable b
    if idx < 0: # Vérifie si l'index est négatif
        return b # Si l'index est négatif, retourne la copie de la liste sans modification
    if idx >= a: # Vérifie si l'index est supérieur ou égal à la longueur de la liste
        return b # Si l'index est hors limites, retourne la copie de la liste sans modification
    b[idx] = element # Remplace l'élément à l'index idx dans la copie de la liste par le nouvel élément 
    return b # Retourne la copie modifiée de la liste
