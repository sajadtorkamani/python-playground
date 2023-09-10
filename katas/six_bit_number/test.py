import unittest
from .solution import six_bit_number


class SixBitNumberTest(unittest.TestCase):
    def test_returns_correct_result(self):
        tests = [
            ("0", True),
            ("55", True),
            ("63", True),
            ("5", True),

            ("1\n", False),
            ("64", False),
            ("-5", False),
            ("", False),
            ("00", False),
            ("-0", False),
            ("05", False),
        ]

        for s, expected in tests:
            self.assertEqual(six_bit_number(s), expected)
