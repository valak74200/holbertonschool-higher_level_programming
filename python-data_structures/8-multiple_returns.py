#!/usr/bin/python3
def multiple_returns(sentence):  # Définition de la fonction avec un paramètre : sentence
    a = len(sentence) # Calcule la longueur de la phrase et la stocke dans la variable a
    if a == 0: # Vérifie si la longueur de la phrase est 0
        b = None # Si la phrase est vide, b est défini comme None
    else:
        b = sentence[0] # Sinon, b est défini comme le premier caractère de la phrase
    return (a, b) # Retourne un tuple contenant la longueur et le premier caractère (ou None)
