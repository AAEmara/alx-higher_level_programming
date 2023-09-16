#!/usr/bin/python3

"""6-max_integer_test Unittest module for max_integr(list=[]) function"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class test_max_integer(unittest.TestCase):
    """Tests the max_integer(list=[]) function"""

    def test_max(self):
        """Tests the right output of the max_integer function"""

        result_1 = max_integer([1, 2, 3])
        self.assertEqual(result_1, 3)

        result_2 = max_integer([-1, -2, -3])
        self.assertEqual(result_2, -1)

        result_3 = max_integer([-1, -2, -3, 0])
        self.assertEqual(result_3, 0)

        result_4 = max_integer([7, 8, 6])
        self.assertEqual(result_4, 8)

        result_5 = max_integer([1])
        self.assertEqual(result_5, 1)

    def test_input(self):
        """Tests the input of the max_integer function"""

        result_1 = max_integer()
        self.assertEqual(result_1, None)
