import unittest
from .solution import possibly_perfect


class SolutionTest(unittest.TestCase):
    def test_simple_cases(self):
        self.assertTrue(possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B']))
        self.assertFalse(possibly_perfect(['B', '_', 'B'], ['B', 'D', 'C']))
        self.assertTrue(possibly_perfect(['T', '_', 'F', 'F', 'F'], ['F', 'F', 'T', 'T', 'T']))
        self.assertTrue(possibly_perfect(['B', 'A', '_', '_'], ['B', 'A', 'C', 'C']))
        self.assertTrue(possibly_perfect(['A', 'B', 'A', '_'], ['B', 'A', 'C', 'C']))
        self.assertFalse(possibly_perfect(['A', 'B', 'C', '_'], ['B', 'A', 'C', 'C']))
        self.assertTrue(possibly_perfect(['B', '_'], ['C', 'A']))
        self.assertFalse(possibly_perfect(['B', 'A'], ['C', 'A']))
        self.assertTrue(possibly_perfect(['B'], ['B']))
        self.assertTrue(possibly_perfect(['_', 'T', '_', '_'], ['T', 'F', 'F', 'F']))
        self.assertTrue(possibly_perfect(['_', 'T', '_', '_'], ['T', 'T', 'F', 'T']))
        self.assertFalse(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'F', 'T']))
        self.assertTrue(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'T', 'T']))
        self.assertTrue(possibly_perfect(['_', 'T', 'T', 'T'], ['F', 'F', 'F', 'F']))
        self.assertTrue(possibly_perfect(['_', '_', '_', '_'], ['F', 'F', 'F', 'F']))


if __name__ == '__main__':
    unittest.main()
