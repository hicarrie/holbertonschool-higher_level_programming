#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    self.assertEqual([1, 2, 3, 4], 4)
    self.assertEqual([1, 3, 4, 2], 4)
    with self.assertRaises(TypeError):
        self.assertFalse(all(isinstance(item, int) for item in ["Hello"]))

if __name__ == '__main__':
    unittest.main()
