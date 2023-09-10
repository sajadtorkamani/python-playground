import unittest
from .solution import magic_sum


class MagicSumTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(magic_sum([3]), 3)
        self.assertEqual(magic_sum([3, 13]), 16)
        self.assertEqual(magic_sum([30, 34, 330]), 0)
        self.assertEqual(magic_sum([3, 12, 5, 8, 30, 13]), 16)
        self.assertEqual(magic_sum([]), 0)

        self.assertEqual(magic_sum(None), 0)
