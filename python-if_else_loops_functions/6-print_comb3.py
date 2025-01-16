#!/usr/bin/python3
# Cette ligne indique au système que c'est un script Python3 (shebang)

# Boucle externe qui parcourt les nombres de 0 à 9
for i in range(0, 10):
    # Boucle interne qui commence à i et va jusqu'à 9
    # Cela évite les doublons comme (1,0) si on a déjà eu (0,1)
    for j in range(i, 10):
        # Si i est égal à j, on saute cette itération
        # Pour éviter d'avoir des paires comme (1,1), (2,2), etc.
        if i == j:
            continue
        else:
            # Affiche la paire de nombres sans espace entre eux
            print('{}{}'.format(i, j), end="")
            
            # Gestion du formatage:
            # - Si i < 8: ajoute une virgule et un espace après la paire
            # - Si i >= 8: ajoute un retour à la ligne
            if i < 8:
                print('', end=", ")
            else:
                print('')
