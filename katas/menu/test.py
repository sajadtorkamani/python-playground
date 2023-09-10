import unittest

from .solution import Menu


class MenuTest(unittest.TestCase):
    def test_returns_correct_result(self):
        menu = Menu(['1', '2', '3'])
        menu2 = Menu(["a", "b", "c"])

        self.assertEqual("[['1'], '2', '3']", menu.display())

        menu.to_the_right()
        self.assertEqual("['1', ['2'], '3']", menu.display())

        menu.to_the_right()
        self.assertEqual("['1', '2', ['3']]", menu.display())

        menu.to_the_right()
        self.assertEqual("[['1'], '2', '3']", menu.display())

        menu2.to_the_left()
        self.assertEqual("['a', 'b', ['c']]", menu2.display(), )

        menu2.to_the_left()
        self.assertEqual("['a', ['b'], 'c']", menu2.display())

        menu2.to_the_left()
        self.assertEqual("[['a'], 'b', 'c']", menu2.display())


if __name__ == "__main__":
    unittest.main()
