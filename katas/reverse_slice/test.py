import unittest

from .solution import reverse_slice


class ReverseSliceTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(reverse_slice('abcde'), ['edcba', 'dcba', 'cba', 'ba', 'a'])
        self.assertEqual(reverse_slice('123'), ['321', '21', '1'])

