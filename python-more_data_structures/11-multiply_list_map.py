#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    # Cette fonction multiplie chaque élément d'une liste par un nombre donné
    # en utilisant la fonction map() et une fonction lambda

    # Utilisation de map() avec une fonction lambda pour multiplier chaque élément
    return list(map(lambda x: x * number, my_list))
    # map() applique la fonction lambda à chaque élément de my_list
    # La fonction lambda x: x * number multiplie chaque élément x par number
    # list() convertit le résultat de map() (qui est un itérateur) en une liste
