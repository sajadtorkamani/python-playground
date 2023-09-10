import unittest
from .solution import even_or_odd


class EvenOrOddTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual("Even", even_or_odd(4))


if __name__ == '__main__':
    unittest.main()
