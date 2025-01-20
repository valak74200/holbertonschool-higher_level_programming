#!/usr/bin/python3
def print_list_integer(my_list=[]): # Définition de la fonction avec une liste vide comme argument par défaut
    for i in range(0, 4): # Boucle for qui itère sur les indices 0, 1, 2, 3
        print("{:d}".format(my_list[i])) # Affiche l'élément de la liste à l'indice i, formaté comme un entier
