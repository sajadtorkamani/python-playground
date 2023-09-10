import unittest
from .solution import declare_winner, Fighter


class DeclareWinnerTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(
            declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"),
            "Lew"
        )
        self.assertEqual(
            declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry"),
            "Harry"
        )
        self.assertEqual(
            declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),
            "Harald"
        )
        self.assertEqual(
            declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),
            "Harald"
        )
        self.assertEqual(
            declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"),
            "Harald"
        )
        self.assertEqual(
            declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),
            "Harald"
        )
