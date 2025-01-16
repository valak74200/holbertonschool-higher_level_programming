#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Boucle qui parcourt les valeurs ASCII de 'a' à 'z'
# ord('a') = 97, ord('z') = 122
for i in range(ord('a'), ord('z') + 1):
   # Vérifie si la valeur ASCII correspond à 'e' ou 'q'
   if i == ord('e') or i == ord('q'):
       # continue passe à l'itération suivante de la boucle
       # ce qui permet de sauter les lettres 'e' et 'q'
       continue
   else:
       # Pour toutes les autres lettres :
       # chr(i) convertit la valeur ASCII en caractère
       # end="" empêche le saut de ligne
       print('{}'.format(chr(i)), end="")
