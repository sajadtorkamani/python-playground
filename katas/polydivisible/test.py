import unittest
from .solution import polydivisible


class SolutionTest(unittest.TestCase):

    def test_polydivisible_1232(self):
        self.assertTrue(polydivisible(1232))

    def test_polydivisible_123220(self):
        self.assertFalse(polydivisible(123220))

    def test_polydivisible_0(self):
        self.assertTrue(polydivisible(0))

    def test_polydivisible_1(self):
        self.assertTrue(polydivisible(1))

    def test_polydivisible_141(self):
        self.assertTrue(polydivisible(141))

    def test_polydivisible_1234(self):
        self.assertFalse(polydivisible(1234))

    def test_polydivisible_21234(self):
        self.assertFalse(polydivisible(21234))

    def test_polydivisible_81352(self):
        self.assertFalse(polydivisible(81352))

    def test_polydivisible_987654(self):
        self.assertTrue(polydivisible(987654))

    def test_polydivisible_1020005(self):
        self.assertTrue(polydivisible(1020005))

    def test_polydivisible_9876545(self):
        self.assertTrue(polydivisible(9876545))

    def test_polydivisible_381654729(self):
        self.assertTrue(polydivisible(381654729))

    def test_polydivisible_1073741823(self):
        self.assertFalse(polydivisible(1073741823))


if __name__ == '__main__':
    unittest.main()
