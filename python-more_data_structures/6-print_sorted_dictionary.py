#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Cette fonction prend un dictionnaire en entrée et imprime ses clés et valeurs
    # dans l'ordre alphabétique des clés

    # Parcours des clés du dictionnaire, triées par ordre alphabétique
    for key in sorted(a_dictionary.keys()):
        # sorted(a_dictionary.keys()) retourne une liste triée des clés du dictionnaire
        # La boucle for itère sur chaque clé dans cet ordre trié

        # Impression de la clé et de sa valeur correspondante
        print("{}: {}".format(key, a_dictionary[key]))
        # Utilisation de la méthode format() pour formater la chaîne de caractères
        # {} est remplacé par la clé, et {} par la valeur correspondante dans le dictionnaire
