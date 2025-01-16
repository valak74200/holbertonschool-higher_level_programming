#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Vérifie si le script est exécuté directement (non importé comme module)
if __name__ == "__main__":
   # Importe le module sys pour accéder aux arguments de la ligne de commande
   import sys

   # Initialise une variable pour stocker la somme des arguments
   result = 0
   
   # Boucle sur tous les arguments sauf le premier (nom du script)
   # range(1, len(sys.argv)) crée une séquence commençant à 1 jusqu'au nombre d'arguments
   for i in range(1, len(sys.argv)):
       # Convertit chaque argument en entier et l'ajoute à result
       # int() transforme la chaîne de caractères en nombre entier
       result += int(sys.argv[i])
       
   # Affiche la somme totale
   print(result)
