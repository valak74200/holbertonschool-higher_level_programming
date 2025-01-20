#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]): # Définition de la fonction avec une liste vide comme argument par défaut
    a = len(my_list) # Calcule la longueur de my_list et stocke le résultat dans la variable a
    for i in range(1, a + 1): # Boucle for qui itère de 1 à a (inclus)
        print("{:d}".format(my_list[-i]))  # Affiche l'élément de la liste à l'index -i, formaté comme un entier
