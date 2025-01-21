#!/usr/bin/python3

def safe_print_division(a, b):
    # Définition de la fonction qui prend deux paramètres 'a' et 'b'
    
    try:
        # Début du bloc try pour gérer les exceptions potentielles
        
        result = a / b
        # Tente de diviser 'a' par 'b' et stocke le résultat dans 'result'
    
    except ZeroDivisionError:
        # Capture l'exception spécifique de division par zéro
        
        result = None
        # Si une division par zéro se produit, 'result' est défini à None
    
    finally:
        # Le bloc finally s'exécute toujours, qu'une exception soit levée ou non
        
        print("Inside result: {}".format(result))
        # Imprime le résultat, qu'il soit un nombre ou None
    
    return result
    # Retourne la valeur de 'result'
