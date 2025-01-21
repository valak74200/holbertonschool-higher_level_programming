#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Définition de la fonction avec des paramètres par défaut
    # my_list est une liste vide par défaut, x est 0 par défaut
    
    try:
        # Début du bloc try pour gérer les exceptions potentielles
        
        for i in range(x):
            # Boucle qui itère x fois
            print(my_list[i], end="")
            # Imprime l'élément à l'index i de my_list sans saut de ligne
        
        print()
        # Imprime un saut de ligne après avoir affiché tous les éléments
        
        return x
        # Retourne le nombre d'éléments qu'on a essayé d'imprimer
    
    except IndexError:
        # Gère l'exception si on essaie d'accéder à un index hors de la liste
        
        print()
        # Imprime un saut de ligne
        
        return i
        # Retourne le nombre d'éléments effectivement imprimés avant l'erreur
