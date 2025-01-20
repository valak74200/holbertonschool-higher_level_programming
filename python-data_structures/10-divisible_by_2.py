#!/usr/bin/python3
def divisible_by_2(my_list=[]): # Définition de la fonction avec une liste vide comme argument par défaut
    new_list = [] # Initialise une nouvelle liste vide pour stocker les résultats
    for i in my_list: # Parcourt chaque élément de la liste d'entrée
        if i % 2 == 0: # Vérifie si l'élément est divisible par 2 (pair)
            new_list.append(True) # Si pair, ajoute True à la nouvelle liste
        else:
            new_list.append(False) # Si impair, ajoute False à la nouvelle liste
    return new_list # Retourne la nouvelle liste contenant les résultats
