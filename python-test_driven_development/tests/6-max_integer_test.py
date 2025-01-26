#!/usr/bin/python3
"""Test unitaire pour max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Classe de test unitaire pour la fonction max_integer"""
    def test_max_integer(self):
        # Test avec une liste croissante
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        
        # Test avec une liste non ordonnée
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        
        # Test avec une liste décroissante
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        
        # Test avec une liste de valeurs identiques
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        
        # Test avec des nombres positifs et négatifs
        self.assertEqual(max_integer([2, 3, -1]), 3)
        
        # Test avec uniquement des nombres négatifs
        self.assertEqual(max_integer([-2, -3, -1]), -1)
        
        # Test avec une liste contenant un seul élément
        self.assertEqual(max_integer([1]), 1)
        
        # Test avec une liste vide
        self.assertEqual(max_integer([]), None)
        
        # Test sans argument (liste par défaut None)
        self.assertEqual(max_integer(), None)
