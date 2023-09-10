import unittest
from .solution import vowel_count

class SolutionTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(2, vowel_count("sajad"))
        self.assertEqual(1, vowel_count("python"))
        self.assertEqual(0, vowel_count("zzz"))


if __name__ == '__main__':
    unittest.main()