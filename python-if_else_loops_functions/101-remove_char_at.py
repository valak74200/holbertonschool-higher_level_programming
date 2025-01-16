#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

def remove_char_at(str, n):
    """
    Supprime le caractère à la position n dans la chaîne str.
    Si n est négatif, retourne la chaîne originale sans modification.
    
    Args:
        str: La chaîne de caractères source
        n: L'index du caractère à supprimer
    
    Returns:
        La nouvelle chaîne sans le caractère à la position n
    """
    # Vérifie si l'index est positif ou nul
    if n >= 0:
        # Découpe la chaîne en deux parties et les recombine :
        # str[0:n]   : caractères du début jusqu'à n (exclus)
        # str[n + 1:]: caractères depuis n+1 jusqu'à la fin
        return str[0:n] + str[n + 1:]
    # Si index négatif, retourne la chaîne d'origine
    return str
