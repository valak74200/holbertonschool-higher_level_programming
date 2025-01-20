#!/usr/bin/python3
a = 89 # Initialise la variable a avec la valeur 89
b = 10 # Initialise la variable b avec la valeur 10
a, b = b, a # Échange les valeurs de a et b : a devient 10, b devient 89
print("a={:d} - b={:d}".format(a, b)) # Affiche les nouvelles valeurs de a et b
