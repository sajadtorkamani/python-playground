import unittest
from .solution import nothing_special


class NothingSpecialTest(unittest.TestCase):
    def test_strips_special_chars(self):
        self.assertEqual(nothing_special("Hello World!"), "Hello World")
        self.assertEqual(nothing_special("%^Take le$ft ##quad%r&a&nt"), "Take left quadrant")
        self.assertEqual(nothing_special("M$$$$$$$y ally!!!!!"), "My ally")

        self.assertEqual(nothing_special(25), "Not a string!")
