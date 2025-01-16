#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Boucle qui parcourt une plage de valeurs ASCII de 'a' à 'z'
# ord('a') convertit le caractère 'a' en sa valeur ASCII (97)
# ord('z') convertit le caractère 'z' en sa valeur ASCII (122)
# Le +1 est nécessaire car range s'arrête avant la dernière valeur
for i in range(ord('a'), ord('z') + 1):
   # chr(i) reconvertit le nombre ASCII en caractère
   # format() insère ce caractère dans la chaîne
   # end="" empêche le saut de ligne après chaque caractère
   print('{}'.format(chr(i)), end="")
