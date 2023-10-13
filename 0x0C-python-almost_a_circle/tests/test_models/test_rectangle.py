#!/usr/bin/python3
"""test_rectangle module for unit testing the Rectangle Class."""
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Unit testing Rectangle Class."""

    @classmethod
    def setUpClass(cls):
        cls.case_1 = Rectangle(1, 1)
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
        self.assertEqual(self.case_1.width, 1)
        self.assertEqual(self.case_2.width, 5)
        self.assertEqual(self.case_3.width, 10)
        self.assertEqual(self.case_4.width, 15)

    def test_height_value(self):
        """Tests height value of a Rectangle Class instance."""
        self.assertEqual(self.case_1.height, 1)
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

    def test_raises(self):
        """Tests raised exceptions in Rectangle Class."""

        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, -1, 0)
        self.assertRaises(ValueError, Rectangle, 0, -1)
        self.assertRaises(TypeError, Rectangle, "1", 1)
        self.assertRaises(TypeError, Rectangle, 5, "1")

        self.assertRaises(ValueError, Rectangle, 5, 10, -1, 5)
        self.assertRaises(ValueError, Rectangle, 5, 10, 5, -1)
        self.assertRaises(TypeError, Rectangle, 5, "1", "5", 0)
        self.assertRaises(TypeError, Rectangle, 5, "1", 5, "0")

    def test_setters(self):
        """Testing setter in Rectangle Class."""
        with self.assertRaises(TypeError):
            self.case_1.width = "1"
            self.case_2.height = "4"
            self.case_3.x = "3"
            self.case_4.y = "6"

        with self.assertRaises(ValueError):
            self.case_1.width = -1
            self.case_2.height = 0
            self.case_3.x = -3
            self.case_4.y = -6

    def test_area(self):
        """Testing the area value of Rectangle Class."""
        self.assertEqual(self.case_1.area(), 1)
        self.assertEqual(self.case_2.area(), 20)
        self.assertEqual(self.case_3.area(), 80)
        self.assertEqual(self.case_4.area(), 180)

    def test_display(self):
        """Testing the displayed Rectangle instance made of '#' character."""
        out = StringIO()
        sys.stdout = out
        self.case_1.display()
        output_1 = out.getvalue()
        self.assertEqual(output_1, "#\n")

        out = StringIO()
        sys.stdout = out
        self.case_2.display()
        output_2 = out.getvalue()
        test_2 = ((" " * self.case_2.x) + ("#" * self.case_2.width) + "\n") 
        test_2 = ("\n" * self.case_2.y + test_2 * self.case_2.height)
        self.assertEqual(output_2, test_2)

        out = StringIO()
        sys.stdout = out
        self.case_3.display()
        output_3 = out.getvalue()
        test_3 = ((" " * self.case_3.x) + ("#" * self.case_3.width) + "\n") 
        test_3 = ("\n" * self.case_3.y + test_3 * self.case_3.height)
        self.assertEqual(output_3, test_3)

        out = StringIO()
        sys.stdout = out
        self.case_4.display()
        output_4 = out.getvalue()
        test_4 = ((" " * self.case_4.x) + ("#" * self.case_4.width) + "\n") 
        test_4 = ("\n" * self.case_4.y + test_4 * self.case_4.height)
        self.assertEqual(output_4, test_4)

        sys.stdout = sys.stdout

    def test_magic_str(self):
        """Testing Rectangle's instance string representation."""
        out = StringIO()
        sys.stdout = out
        print(self.case_1)
        output_1 = out.getvalue().strip()
        test_1 = f"[Rectangle] ({self.case_1.id}) "
        test_1 += f"{self.case_1.x}/{self.case_1.y} "
        test_1 += f"- {self.case_1.width}/{self.case_1.height}"
        self.assertEqual(output_1, test_1)

        out = StringIO()
        sys.stdout = out
        print(self.case_2)
        output_2 = out.getvalue().strip()
        test_2 = f"[Rectangle] ({self.case_2.id}) "
        test_2 += f"{self.case_2.x}/{self.case_2.y} "
        test_2 += f"- {self.case_2.width}/{self.case_2.height}"
        self.assertEqual(output_2, test_2)

        out = StringIO()
        sys.stdout = out
        print(self.case_3)
        output_3 = out.getvalue().strip()
        test_3 = f"[Rectangle] ({self.case_3.id}) "
        test_3 += f"{self.case_3.x}/{self.case_3.y} "
        test_3 += f"- {self.case_3.width}/{self.case_3.height}"
        self.assertEqual(output_3, test_3)

        out = StringIO()
        sys.stdout = out
        print(self.case_4)
        output_4 = out.getvalue().strip()
        test_4 = f"[Rectangle] ({self.case_4.id}) "
        test_4 += f"{self.case_4.x}/{self.case_4.y} "
        test_4 += f"- {self.case_4.width}/{self.case_4.height}"
        self.assertEqual(output_4, test_4)
