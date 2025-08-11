from unittest import TestCase
from src.module_math import add

class TestAdd(TestCase):
    def test_add_all_positive(self):
        actual: int = add(1, 2)
        expected: int = 3
        self.assertEqual(actual, expected)
    
    def test_add_all_negative(self):
        actual: int = add(-1, -2)
        expected: int = -3
        self.assertEqual(actual, expected)

    def test_add_positive_negative(self):
        actual: int = add(1, -2)
        expected: int = -1
        self.assertEqual(actual, expected)
