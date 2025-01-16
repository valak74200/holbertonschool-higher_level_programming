#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Vérifie si le script est exécuté directement (non importé comme module)
if __name__ == "__main__":
   # Importe les 4 fonctions (add, sub, mul, div) depuis le module calculator_1
   from calculator_1 import add, sub, mul, div
   
   # Définit la première variable à 10
   a = 10
   
   # Définit la deuxième variable à 5  
   b = 5
   
   # Affiche le résultat de l'addition en utilisant la fonction add()
   # format() remplace les {} par les valeurs a, b et le résultat de add(a,b)
   print("{} + {} = {}".format(a, b, add(a, b)))
   
   # Affiche le résultat de la soustraction en utilisant la fonction sub()
   print("{} - {} = {}".format(a, b, sub(a, b)))
   
   # Affiche le résultat de la multiplication en utilisant la fonction mul()
   print("{} * {} = {}".format(a, b, mul(a, b)))
   
   # Affiche le résultat de la division en utilisant la fonction div()
   print("{} / {} = {}".format(a, b, div(a, b)))
