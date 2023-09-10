import unittest

from .solution import best_friend


class BestFriendTest(unittest.TestCase):
    def test_returns_correct_result(self):
        # self.assertEqual(best_friend('he headed to the store', 'h', 'e'), True)
        # self.assertEqual(
        #     best_friend('i found an ounce with my hound', 'o', 'u'), True)
        # self.assertEqual(
        #     best_friend('those were their thorns they said', 't', 'h'), True)
        self.assertEqual(best_friend('we found your dynamite', 'd', 'y'), False)
        # self.assertEqual(best_friend('look they took the cookies', 'o', 'o'),
        #                  False)
        # self.assertEqual(best_friend('a test', 't', 'e'), False)
        # self.assertEqual(best_friend('abcdee', 'e', 'e'), False)
        # self.assertEqual(best_friend('abcde', 'e', 'e'), False)


if __name__ == "__main__":
    unittest.main()
