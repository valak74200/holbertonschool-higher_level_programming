#!/usr/bin/python3

def roman_to_int(roman_string):
    # Cette fonction convertit un nombre romain en entier

    # Vérification que l'entrée est une chaîne de caractères non nulle
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    # Dictionnaire des valeurs des chiffres romains
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0  # Initialisation du résultat
    for i in range(len(roman_string)):
        # Vérification des cas spéciaux (comme IV, IX, XL, etc.)
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
            # Si le chiffre actuel est plus grand que le précédent, on soustrait deux fois
            # la valeur du chiffre précédent (car on l'a déjà ajouté une fois)
            num += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i - 1]]
        else:
            # Sinon, on ajoute simplement la valeur du chiffre actuel
            num += roman_dict[roman_string[i]]
    
    return num  # Retourne le résultat final
