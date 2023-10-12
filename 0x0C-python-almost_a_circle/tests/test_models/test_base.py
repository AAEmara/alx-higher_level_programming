#!/usr/bin/python3

"""1-base_test module that tests the Base Class"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests the Base Class"""

    @classmethod
    def setUpClass(cls):
        cls.case_1 = Base()
        cls.case_2 = Base(1)
        cls.case_3 = Base()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_id_value(self):
        """Tests if the instance got the correct id."""
        self.assertEqual(self.case_1.id, 1)
        self.assertEqual(self.case_2.id, 1)
        self.assertEqual(self.case_3.id, 2)

    def test_id_not_none(self):
        """Test instances' id are not a None value."""
        self.assertIsNotNone(self.case_1.id)
        self.assertIsNotNone(self.case_2.id)
        self.assertIsNotNone(self.case_3.id)

    def test_object_type(self):
        """Tests instance type vs Base Class"""
        self.assertIsInstance(self.case_1, Base)
        self.assertIsInstance(self.case_2, Base)
        self.assertIsInstance(self.case_3, Base)
