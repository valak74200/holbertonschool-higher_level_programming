#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

def fizzbuzz():
    """
    Implémentation du jeu FizzBuzz.
    Affiche les nombres de 1 à 100 avec les règles suivantes :
    - 'FizzBuzz' pour les multiples de 15 (3 et 5)
    - 'Fizz' pour les multiples de 3
    - 'Buzz' pour les multiples de 5
    - Le nombre lui-même dans les autres cas
    """
    # Boucle de 1 à 100 inclus
    for i in range(1, 101):
        # Vérifie d'abord les multiples de 15
        # Car 15 est multiple de 3 ET de 5
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        # Vérifie les multiples de 3
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Vérifie les multiples de 5
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # Si aucune condition n'est remplie, affiche le nombre
        else:
            print("{:d}".format(i), end=" ")
