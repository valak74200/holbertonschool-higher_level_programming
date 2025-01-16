#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

def print_last_digit(number):
    """
    Affiche et retourne le dernier chiffre d'un nombre.
    Fonctionne avec les nombres positifs et négatifs.
    
    Args:
        number: Le nombre dont on veut extraire le dernier chiffre
    
    Returns:
        int: Le dernier chiffre du nombre (toujours positif)
    """
    # Pour un nombre positif, utilise directement le modulo 10
    if number >= 0:
        last = number % 10
    # Pour un nombre négatif, on le rend d'abord positif avec -number
    else:
        last = (-number) % 10
    
    # Affiche le dernier chiffre
    # {:d} formate le nombre en entier décimal
    print('{:d}'.format(last), end="")
    
    # Retourne le dernier chiffre
    return (last)
