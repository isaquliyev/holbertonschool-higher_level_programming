#!/usr/bin/python3

"""
    Tests for Almost a circle module - Rectangle Class
"""


import unittest
from unittest.mock import patch

import os
from models.rectangle import Rectangle
from io import StringIO


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        """
            Creating instances and checking them
        """
        # Only height and width initialization
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        # Initalization of all attributes
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 5)

        # Type error cases
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("2", 3)
        with self.assertRaises(TypeError):
            Rectangle(4, "5")
        with self.assertRaises(TypeError):
            Rectangle(6, 7, "8")
        with self.assertRaises(TypeError):
            Rectangle(9, 10, 11, "12")

        # Value error cases
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(3, -4)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(6, 0)
        with self.assertRaises(ValueError):
            Rectangle(7, 8, -9)
        with self.assertRaises(ValueError):
            Rectangle(10, 11, 12, -13)

        """ Area function testing """
        r3 = Rectangle(1, 2)
        self.assertEqual(r3.area(), 2)

        """ __str__ function testing """
        r4 = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(str(r4), "[Rectangle] (7) 5/6 - 3/4")

        """ Display Testing """
        r5 = Rectangle(1, 1)
        output = "#\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r5.display()
            self.assertEqual(out.getvalue(), output)
        r6 = Rectangle(1, 1, 1, 1, 1)
        output = "\n #\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r6.display()
            self.assertEqual(out.getvalue(), output)
