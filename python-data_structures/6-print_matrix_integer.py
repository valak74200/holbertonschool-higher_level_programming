#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]): # Définition de la fonction avec une matrice vide comme argument par défaut
    for i in range(len(matrix)): # Boucle sur les lignes de la matrice
        for j in range(len(matrix[i])): # Boucle sur les colonnes de chaque ligne
            if j == len(matrix[i]) - 1: # Vérifie si c'est le dernier élément de la ligne
                print("{:d}".format(matrix[i][j]), end="") # Affiche l'élément sans espace à la fin
            else:
                print("{:d}".format(matrix[i][j]), end=" ") # Affiche l'élément avec un espace à la fin
        print() # Passe à la ligne suivante après avoir affiché tous les éléments d'une ligne
