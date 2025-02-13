#!/usr/bin/python3
"""
Module pour la sérialisation et désérialisation de données JSON.

Ce module fournit deux fonctions principales :
- serialize_and_save_to_file : pour sérialiser des données en JSON et les sauvegarder
- load_and_deserialize : pour charger et désérialiser des données JSON depuis un fichier
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python en JSON et le sauvegarde dans un fichier.

    Args:
        data (dict): Le dictionnaire Python à sérialiser
        filename (str): Le nom du fichier de sortie JSON

    Returns:
        None
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Erreur lors de la sérialisation : {e}")


def load_and_deserialize(filename):
    """
    Charge et désérialise des données JSON depuis un fichier.

    Args:
        filename (str): Le nom du fichier JSON à lire

    Returns:
        dict: Le dictionnaire Python contenant les données désérialisées
        None: En cas d'erreur
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur lors de la désérialisation : {e}")
        return None
