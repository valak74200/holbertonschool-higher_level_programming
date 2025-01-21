#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Cette fonction prend une liste, un élément à rechercher et un élément de remplacement
    # Elle retourne une nouvelle liste où toutes les occurrences de 'search' sont remplacées par 'replace'

    # Utilisation d'une liste en compréhension pour créer la nouvelle liste
    return [replace if x == search else x for x in my_list]
    # Pour chaque élément x dans my_list :
    #   - Si x est égal à 'search', on le remplace par 'replace'
    #   - Sinon, on garde x tel quel
    # Le résultat est une nouvelle liste avec les remplacements effectués
