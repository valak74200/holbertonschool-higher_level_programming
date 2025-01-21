#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Définition de la fonction qui prend trois paramètres :
    # my_list_1 et my_list_2 sont les listes à diviser, list_length est la longueur de la nouvelle liste
    
    new_list = []
    # Initialisation d'une nouvelle liste vide pour stocker les résultats
    
    for i in range(list_length):
        # Boucle qui itère 'list_length' fois
        
        try:
            # Début du bloc try pour gérer les exceptions potentielles
            
            result = my_list_1[i] / my_list_2[i]
            # Tente de diviser l'élément i de my_list_1 par l'élément i de my_list_2
        
        except ZeroDivisionError:
            # Capture l'exception de division par zéro
            
            print("division by 0")
            # Affiche un message d'erreur
            
            result = 0
            # Définit le résultat à 0 en cas de division par zéro
        
        except TypeError:
            # Capture l'exception de type incorrect (par exemple, division de chaînes)
            
            print("wrong type")
            # Affiche un message d'erreur
            
            result = 0
            # Définit le résultat à 0 en cas de type incorrect
        
        except IndexError:
            # Capture l'exception d'index hors limites
            
            print("out of range")
            # Affiche un message d'erreur
            
            result = 0
            # Définit le résultat à 0 si l'index est hors limites
        
        finally:
            # Le bloc finally s'exécute toujours, qu'une exception soit levée ou non
            
            new_list.append(result)
            # Ajoute le résultat (qu'il soit calculé ou 0) à la nouvelle liste
    
    return new_list
    # Retourne la nouvelle liste contenant tous les résultats
