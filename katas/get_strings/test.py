import unittest
from .solution import get_strings


class SolutionTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(get_strings("Chicago"), "c:**,h:*,i:*,a:*,g:*,o:*")
        self.assertEqual(get_strings("Bangkok"), "b:*,a:*,n:*,g:*,k:**,o:*")
        self.assertEqual(get_strings("Las Vegas"), "l:*,a:**,s:**,v:*,e:*,g:*")
