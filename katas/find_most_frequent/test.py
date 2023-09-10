import unittest
from .solution import find_most_frequent


class SolutionTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(find_most_frequent([1, 1, 2, 3]), {1})
        self.assertEqual(find_most_frequent([1, 1, 2, 2, 3]), {1, 2})
        self.assertEqual(find_most_frequent([]), set([]))
