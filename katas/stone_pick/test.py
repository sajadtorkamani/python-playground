import unittest
from .solution import stone_pick


class SolutionTest(unittest.TestCase):
    def test_example_tests(self):
        self.assertEqual(2, stone_pick(["Sticks"] * 4 + ["Cobblestone"] * 6))
        self.assertEqual(0, stone_pick(["Sticks"] * 2 + ["Cobblestone"] * 1))
        self.assertEqual(0, stone_pick(
            ["Sticks"] * 4 + ["Wool"] * 3 + ["Dirt"] * 6))
        self.assertEqual(4, stone_pick(["Wood"] * 2 + ["Cobblestone"] * 12))

    def test_more_equal_than(self):
        self.assertEqual(1, stone_pick(["Sticks"] * 4 + ["Cobblestone"] * 3))
        self.assertEqual(8, stone_pick(["Sticks"] * 31 + ["Cobblestone"] * 25))
        self.assertEqual(21, stone_pick(["Sticks"] * 64 + ["Cobblestone"] * 64))

    #
    def test_mixed_junk(self):
        self.assertEqual(1, stone_pick(
            ["Sticks", "Wool", "Dirt", "Diamond",
             "Stone", "Cobblestone",
             "Sticks", "Cobblestone", "Cobblestone"]))
        self.assertEqual(0, stone_pick(
            ["Wool", "Dirt", "Diamond", "Sticks", "Cobblestone",
             "Cobblestone"]))
        self.assertEqual(5, stone_pick(
            ["Wool"] * 21 + ["Sticks"] * 11 + [
                "Stone"] * 31 + [
                "Cobblestone"] * 41 + ["Diamond"] * 8))

    def test_no_picks(self):
        self.assertEqual(0, stone_pick(["Wool", "Dirt", "Diamond", "Sticks"]))
        self.assertEqual(0,
                         stone_pick(["Wood", "Dirt", "Cobblestone", "Sticks"]))
        self.assertEqual(0, stone_pick(
            ["Dirt"] * 51 + ["Cobblestone"] * 21 + [
                "Sticks"] + [
                "Wool"] * 41 + ["Diamond"] * 12))

    def test_wood_only(self):
        self.assertEqual(30, stone_pick(["Wood"] * 51 + ["Cobblestone"] * 91))
        self.assertEqual(24, stone_pick(["Wood"] * 12 + ["Cobblestone"] * 120))
        self.assertEqual(16, stone_pick(["Wood"] * 33 + ["Cobblestone"] * 50))

    def test_none(self):
        self.assertEqual(0, stone_pick([]))

    def test_stone_picktest_(self):
        self.assertEqual(0, stone_pick())


if __name__ == "__main__":
    unittest.main()
