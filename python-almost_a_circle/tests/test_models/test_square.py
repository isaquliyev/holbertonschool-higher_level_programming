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

    def test_square(self):
        self.assertEqual(self.s1.size, 1)

        self.assertEqual(self.s2.size, 1)
        self.assertEqual(self.s2.x, 2)

        self.assertEqual(self.s3.size, 1)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s3.y, 3)
