import unittest

from .solution import rev_sub


class RevSubTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(rev_sub([2, 4, 3]), [4, 2, 3])
        self.assertEqual(rev_sub([4, 2]), [2, 4])
        self.assertEqual(rev_sub([]), [])
        self.assertEqual(rev_sub([2, 4, 3, 10, 2]), [4, 2, 3, 2, 10])


if __name__ == "__main__":
    unittest.main()
