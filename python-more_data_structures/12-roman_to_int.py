#!/usr/bin/python3
# Cette ligne indique que le script doit être exécuté avec l'interpréteur Python 3

def roman_to_int(roman_string):
    # Définition de la fonction qui convertit un nombre romain en entier

    if not roman_string or not isinstance(roman_string, str):
        # Vérifie si la chaîne est vide ou n'est pas une chaîne de caractères
        return 0
        # Si c'est le cas, retourne 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    # Dictionnaire associant chaque symbole romain à sa valeur numérique

    num = 0
    # Initialisation de la variable qui contiendra le résultat final

    for i in range(len(roman_string)):
        # Boucle sur chaque caractère de la chaîne romaine

        if i > 0 and r_dict[roman_string[i]] > r_dict[roman_string[i - 1]]:
            # Vérifie si le caractère actuel a une valeur supérieure au précédent
            # (cas spécial comme IV, IX, XL, etc.)

            num += r_dict[roman_string[i]] - 2 * r_dict[roman_string[i - 1]]
            # Ajoute la différence et soustrait deux fois la valeur précédente
            # (car elle a été ajoutée une fois de trop dans l'itération précédente)

        else:
            # Cas normal : on ajoute simplement la valeur du caractère actuel
            num += r_dict[roman_string[i]]

    return num
    # Retourne le résultat final
