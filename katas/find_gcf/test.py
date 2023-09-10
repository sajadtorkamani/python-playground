import unittest

from .solution import find_GCF


class FindGCFTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(find_GCF(8,20), 4);
        self.assertEqual(find_GCF(2, 4), 2)
        self.assertEqual(find_GCF(5,13), 1);
        self.assertEqual(find_GCF(100,100), 100);

