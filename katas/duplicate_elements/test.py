import unittest
from .solution import duplicate_elements


class DuplicateElementTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(duplicate_elements([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True)
        self.assertEqual(duplicate_elements([9, 8, 7], [8, 1, 3]), True)

        self.assertEqual(duplicate_elements([2, 4, 6], [8, 10, 12]), False)
