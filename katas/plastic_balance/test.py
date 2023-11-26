import unittest
from .solution import plastic_balance


class SolutionTest(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(plastic_balance([1, 2, 3, 4, 5]), [])

    def test_case_2(self):
        self.assertEqual(plastic_balance([0, 104, 3, 101, 0, 111]), [104, 3, 101, 0])

    def test_case_3(self):
        self.assertEqual(plastic_balance([1, -1]), [1, -1])

    def test_case_4(self):
        self.assertEqual(plastic_balance([0]), [0])

    def test_case_5(self):
        self.assertEqual(plastic_balance([100, 0, -100]), [100, 0, -100])

    def test_case_6(self):
        self.assertEqual(plastic_balance([4, 4]), [])


if __name__ == '__main__':
    unittest.main()
