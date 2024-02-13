#!/usr/bin/python3

"""
    Tests for Almost a circle module - Square Class
"""


import unittest
from unittest.mock import patch

import os
from models.square import Square
from io import StringIO

class TestSquare(unittest.TestCase):

    def setUp(self):
        """ Creating instances for testing """
        self.s1 = Square(1)
        self.s2 = Square(1, 2)
        self.s3 = Square(1, 2, 3)
        self.s4 = Square(1, 2, 3, 4)

    def test_square(self):
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s3.y, 3)
        self.assertEqual(self.s4.id, 4)

        # Type Error cases
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        # Value Error cases
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    """ Method testing: __str__ """
    def test_str(self):
        self.assertEqual(str(self.s4), "[Square] (4) 2/3 - 1")

    """ Method testing: to_dictionary """
    def  test_to_dictionary(self):
        self.assertEqual(self.s4.to_dictionary(), {"id": 4, "size": 1, "x": 2, "y": 3})

    """ Method testing: update """
    def test_update(self):
        self.s4.update(2, 3, 4, 5)
        self.assertEqual(str(self.s4), "[Square] (2) 4/5 - 3")
