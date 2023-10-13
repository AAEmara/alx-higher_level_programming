#!/usr/bin/python3
"""test_rectangle module for unit testing the Rectangle Class."""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Unit testing Rectangle Class."""

    @classmethod
    def setUpClass(cls):
        cls.case_1 = Rectangle(0, 0)
        cls.case_2 = Rectangle(5, 4, id=12)
        cls.case_3 = Rectangle(10, 8, 3, 3)
        cls.case_4 = Rectangle(15, 12, 6, 6, 3)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_id_value(self):
        """Tests id value of a Rectangle Class instance."""
        self.assertEqual(self.case_1.id, 1)
        self.assertEqual(self.case_2.id, 12)
        self.assertEqual(self.case_3.id, 2)
        self.assertEqual(self.case_4.id, 3)

    def test_width_value(self):
        """Tests width value of a Rectangle Class instance."""
        self.assertEqual(self.case_1.width, 0)
        self.assertEqual(self.case_2.width, 5)
        self.assertEqual(self.case_3.width, 10)
        self.assertEqual(self.case_4.width, 15)

    def test_height_value(self):
        """Tests height value of a Rectangle Class instance."""
        self.assertEqual(self.case_1.height, 0)
        self.assertEqual(self.case_2.height, 4)
        self.assertEqual(self.case_3.height, 8)
        self.assertEqual(self.case_4.height, 12)

    def test_x_y_value(self):
        """Tests x, and y values of a Rectangle Class instance."""
        self.assertEqual(self.case_1.x, 0)
        self.assertEqual(self.case_1.y, 0)

        self.assertEqual(self.case_2.x, 0)
        self.assertEqual(self.case_2.y, 0)

        self.assertEqual(self.case_3.x, 3)
        self.assertEqual(self.case_3.y, 3)

        self.assertEqual(self.case_4.x, 6)
        self.assertEqual(self.case_4.y, 6)

    def test_obj_type(self):
        """Tests instance type vs. Rectangle Class."""
        self.assertIsInstance(self.case_1, Rectangle)
        self.assertIsInstance(self.case_2, Rectangle)
        self.assertIsInstance(self.case_3, Rectangle)
        self.assertIsInstance(self.case_4, Rectangle)
