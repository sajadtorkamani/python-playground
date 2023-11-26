import unittest
from .solution import esthetic, is_esthetic


class EstheticTest(unittest.TestCase):
    def test_is_esthetic_returns_true_if_num_is_esthetic(self):
        self.assertEqual(True, is_esthetic(101))
        self.assertEqual(True, is_esthetic(21))
        self.assertEqual(True, is_esthetic(10101))


    def test_is_esthetic_returns_false_if_num_is_not_esthetic(self):
        self.assertEqual(False, is_esthetic(1010011010))
        self.assertEqual(False, is_esthetic(124))
        self.assertEqual(False, is_esthetic(11))


    def test_returns_correct_result(self):
        # self.assertEqual([8], esthetic(666))
        # self.assertEqual(esthetic(10), [2, 3, 8, 10])
        # self.assertEqual(esthetic(23), [3, 5, 7, 10])
        # self.assertEqual(esthetic(666), [8])
        # self.assertEqual(esthetic(13), [5, 6])
        self.assertEqual(esthetic(1), [2, 3, 4, 5, 6, 7, 8, 9, 10])
        # self.assertEqual(esthetic(9), [4, 7, 9, 10])
        # self.assertEqual(esthetic(74), [])
        # self.assertEqual(esthetic(740), [4, 6, 9])
        # self.assertEqual(esthetic(928), [])
        # self.assertEqual(esthetic(259259), [9])
        # self.assertEqual(esthetic(883271), [])
        # self.assertEqual(esthetic(1080898), [7])
        # self.assertEqual(esthetic(1080899), [])


if __name__ == "__main__":
    unittest.main()
