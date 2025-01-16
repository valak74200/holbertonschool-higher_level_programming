#!/usr/bin/python3
# Cette ligne est un "shebang" qui indique que ce script doit être exécuté avec Python3

# Vérifie si le script est exécuté directement (non importé comme module)
if __name__ == "__main__":
   # Importe la variable 'a' depuis le module variable_load_5
   from variable_load_5 import a

   # Affiche la valeur de la variable 'a' en utilisant un f-string
   # f'{a}' est une syntaxe de formatage qui permet d'insérer directement la valeur de 'a'
   print(f'{a}')
