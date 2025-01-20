#!/usr/bin/python3
def no_c(my_string): # Définition de la fonction avec un paramètre : my_string
    new_string = '' # Initialise une nouvelle chaîne vide pour stocker les caractères filtrés
    for char in my_string: # Boucle pour parcourir chaque caractère dans my_string
        if char != 'c' and char != 'C': # Vérifie si le caractère n'est pas 'c' ou 'C'
            new_string += char # Ajoute le caractère à new_string s'il ne s'agit pas de 'c' ou 'C'
    return new_string # Retourne la nouvelle chaîne sans les caractères 'c' et 'C'
