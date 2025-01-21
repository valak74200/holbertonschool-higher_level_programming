#!/usr/bin/python3

def best_score(a_dictionary):
    # Cette fonction retourne la clé avec la plus grande valeur dans le dictionnaire
    # Si le dictionnaire est vide ou None, elle retourne None

    # Vérification si le dictionnaire est None ou vide
    if a_dictionary is None or a_dictionary == {}:
        # Si c'est le cas, on retourne None
        return None
    
    # Utilisation de la fonction max() avec une fonction clé personnalisée
    return max(a_dictionary, key=a_dictionary.get)
    # max() trouve la clé avec la plus grande valeur associée
    # a_dictionary.get est utilisé comme fonction clé pour comparer les valeurs
