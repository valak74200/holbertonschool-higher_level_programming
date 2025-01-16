#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Importe le module random qui permet de générer des nombres aléatoires
import random

# Génère un nombre aléatoire entre -10 et 10 inclus
# randint(a,b) renvoie un nombre entier N tel que a <= N <= b
number = random.randint(-10, 10)

# Vérifie si le nombre est positif (supérieur à 0)
if number > 0:
   # Affiche que le nombre est positif
   # {:d} est un format qui spécifie que number doit être affiché comme un entier décimal
   print("{:d} is positive".format(number))
# Vérifie si le nombre est négatif (inférieur à 0)
elif number < 0:
   # Affiche que le nombre est négatif
   print("{:d} is negative".format(number))
# S'exécute si le nombre n'est ni positif ni négatif (donc égal à 0)
else:
   # Affiche que le nombre est zéro
   print("{:d} is zero".format(number))
