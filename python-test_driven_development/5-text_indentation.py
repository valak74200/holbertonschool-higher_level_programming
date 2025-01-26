#!/usr/bin/python3
"""Ce module contient une fonction
    qui imprime un texte avec 2 nouvelles lignes après.
"""


def text_indentation(text):
    """Imprime un texte avec 2 nouvelles lignes après.

    Args:
        text (str): Le texte à imprimer

    Raises:
        TypeError: Si le texte n'est pas une chaîne de caractères

    Returns:
        str: Le texte avec 2 nouvelles lignes après
    """
    # Vérifie si le texte est une chaîne de caractères
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    # Initialise une nouvelle chaîne de caractères vide
    new_text = ""
    
    # Parcourt chaque caractère du texte
    for i in text:
        # Ignore les espaces au début du texte
        if i == " " and len(new_text) == 0:
            continue
        # Ignore les espaces après une nouvelle ligne
        elif i == " " and new_text[-1] in "\n":
            continue
        # Ajoute le caractère au nouveau texte
        new_text += i
        # Ajoute deux nouvelles lignes après '.', '?', ':' ou '!'
        if i in ".?:!":
            new_text += "\n\n"
    
    # Imprime le nouveau texte sans ajouter de nouvelle ligne à la fin
    print(new_text, end="")
