#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

def uppercase(str):
    """
    Convertit une chaîne de caractères en majuscules et l'affiche.
    
    Args:
        str: La chaîne de caractères à convertir
    """
    # Parcourt chaque caractère de la chaîne
    for c in str:
        # Vérifie si le caractère est une minuscule
        # ord('a') = 97, ord('z') = 122
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            # Conversion en majuscule :
            # 1. ord(c) - ord('a') donne la position de la lettre dans l'alphabet (0-25)
            # 2. + ord('A') décale cette position vers la plage des majuscules
            # 3. chr() convertit le code ASCII en caractère
            d = chr(ord(c) + ord('A') - ord('a'))
        else:
            # Si ce n'est pas une minuscule, garde le caractère tel quel
            d = c
        
        # Affiche le caractère sans retour à la ligne
        print(d.format(), end="")
    
    # Ajoute un retour à la ligne à la fin de la chaîne
    print("".format())
