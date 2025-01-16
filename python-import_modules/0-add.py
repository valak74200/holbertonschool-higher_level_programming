#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique au système que ce script doit être exécuté avec Python3

# La condition vérifie si ce fichier est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    # Importe la fonction 'add' depuis le module 'add_0'
    from add_0 import add
    
    # Définit la première variable avec la valeur 1
    a = 1
    
    # Définit la deuxième variable avec la valeur 2
    b = 2
    
    # Appelle la fonction add avec les paramètres a et b, et stocke le résultat dans la variable 'add'
    add = add(a, b)
    
    # Affiche le résultat avec format() pour insérer les valeurs dans la chaîne
    # {} sont des emplacements qui seront remplacés par les valeurs a, b et add dans l'ordre
    print("{} + {} = {}".format(a, b, add))
