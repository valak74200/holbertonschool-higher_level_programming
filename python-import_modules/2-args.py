#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Vérifie si le script est exécuté directement (non importé comme module)
if __name__ == "__main__":
   # Importe le module sys qui permet d'accéder aux arguments de la ligne de commande
   import sys
   
   # Calcule le nombre d'arguments en excluant le nom du script (sys.argv[0])
   number_arg = len(sys.argv) - 1
   
   # Vérifie s'il n'y a aucun argument
   if number_arg == 0:
       print("{} arguments.".format(number_arg))
   # Vérifie s'il y a exactement un argument
   elif number_arg == 1:
       print("{} argument:".format(number_arg))
   # S'exécute s'il y a plus d'un argument
   else:
       print("{} arguments:".format(number_arg))

   # Boucle qui parcourt tous les arguments à partir de l'index 1
   # range(1, number_arg + 1) crée une séquence de 1 jusqu'au nombre d'arguments
   for i in range(1, number_arg + 1):
       # Affiche chaque argument avec son numéro
       # sys.argv[i] accède à l'argument à la position i
       print("{}: {}".format(i, sys.argv[i]))
