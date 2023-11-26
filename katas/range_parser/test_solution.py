import unittest
from .solution import range_parser


class SolutionTest(unittest.TestCase):
    def test_range_parser(self):
        self.assertEqual(
            [21],
            range_parser('21-30:11'),
        )

        self.assertEqual(
            [8, 13, 18, 23, 14, 21, 1],
            range_parser('8-27:5, 14-14:2, 21-30:11, 1'),
        )

        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24],
            range_parser('1-10,14, 20-25:2'),
        )

        self.assertEqual(
            [5, 6, 7, 8, 9, 10],
            range_parser('5-10')
        )

        self.assertEqual([2], range_parser('2'))


if __name__ == "__main__":
    unittest.main()
