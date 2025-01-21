#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Définition de la fonction avec des paramètres par défaut
    # my_list est une liste vide par défaut, x est 0 par défaut
    
    count = 0
    # Initialisation du compteur d'entiers imprimés
    
    for i in range(x):
        # Boucle qui itère x fois
        
        try:
            # Début du bloc try pour gérer les exceptions potentielles
            
            print("{:d}".format(my_list[i]), end="")
            # Tente d'imprimer l'élément à l'index i de my_list formaté comme un entier
            # end="" empêche le saut de ligne après chaque impression
            
            count += 1
            # Incrémente le compteur si l'impression réussit
        
        except (ValueError, TypeError):
            # Capture les exceptions ValueError et TypeError
            
            pass
            # Ne fait rien si une exception est levée (continue à la prochaine itération)
    
    print()
    # Imprime un saut de ligne après avoir traité tous les éléments
    
    return count
    # Retourne le nombre d'entiers effectivement imprimés
