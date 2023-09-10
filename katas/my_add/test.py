import unittest
from .solution import my_add


class SolutionTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(my_add(1, 3.414), 4.414)
        self.assertEqual(my_add(42, " is the answer."), None)
        self.assertEqual(my_add(10, "2"), None)
