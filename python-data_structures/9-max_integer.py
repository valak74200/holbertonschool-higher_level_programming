#!/usr/bin/python3
def max_integer(my_list=[]): # Définition de la fonction avec une liste vide comme argument par défaut
    if my_list: # Vérifie si la liste n'est pas vide
        max_int = my_list[0] # Initialise max_int avec le premier élément de la liste
        for i in my_list: # Parcourt chaque élément de la liste
            if i > max_int: # Compare l'élément actuel avec max_int
                max_int = i # Si l'élément est plus grand, met à jour max_int
        return max_int # Retourne la valeur maximale trouvée
    return None # Si la liste est vide, retourne None
