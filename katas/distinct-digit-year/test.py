import unittest
from .solution import distinct_digit_year


class DistinctDigitYearTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(distinct_digit_year(1987), 2013)
        self.assertEqual(distinct_digit_year(2013), 2014)
