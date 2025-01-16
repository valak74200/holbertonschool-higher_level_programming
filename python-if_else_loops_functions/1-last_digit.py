#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Importe le module random pour générer des nombres aléatoires
import random

# Génère un nombre aléatoire entre -10000 et 10000 inclus
number = random.randint(-10000, 10000)

# Initialise la variable qui stockera le dernier chiffre
last = 0

# Pour les nombres positifs
if number > 0:
   # Obtient le dernier chiffre avec l'opérateur modulo 10
   last = number % 10
# Pour les nombres négatifs
elif number < 0:
   # Obtient le dernier chiffre avec l'opérateur modulo -10
   # Nécessaire pour gérer correctement les nombres négatifs
   last = number % -10

# Affiche la première partie du message
# end=" " empêche le saut de ligne automatique après le print
print("Last digit of {:d} is {:d} and is".format(number, last), end=" ")

# Vérifie si le dernier chiffre est supérieur à 5
if last > 5:
   print("greater than 5")
# Vérifie si le dernier chiffre est égal à 0
elif last == 0:
   print("0")
# S'exécute si le dernier chiffre n'est ni supérieur à 5 ni égal à 0
else:
   print("less than 6 and not 0")
