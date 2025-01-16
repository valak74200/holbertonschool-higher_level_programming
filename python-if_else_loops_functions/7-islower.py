#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

def islower(c):
    """
    Vérifie si un caractère est une lettre minuscule.
    
    Args:
        c: Le caractère à vérifier
    
    Returns:
        bool: True si le caractère est une minuscule, False sinon
    """
    # ord(c) convertit le caractère en sa valeur ASCII
    # ord('a') donne la valeur ASCII de 'a' (97)
    # ord('z') donne la valeur ASCII de 'z' (122)
    # range(ord('a'), ord('z') + 1) crée une plage de 97 à 122 inclus
    if ord(c) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False
