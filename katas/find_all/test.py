import unittest
from .solution import find_all


class FindAllTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(find_all([6, 9, 3, 4, 3, 82, 11], 3), [2, 4])
        self.assertEqual(find_all([10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16), [1, 9])
        self.assertEqual(
            find_all([20, 20, 10, 13, 15, 2, 7, 2, 20, 3, 18, 2, 3, 2, 16, 10, 9, 9, 7, 5, 15, 5],
                     20), [0, 1, 8])


if __name__ == '__main__':
    unittest.main()
