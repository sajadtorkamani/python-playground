import unittest
from .solution import remove_letter


class RemoveLetterTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(remove_letter('abracadabra', 1), 'bracadabra')
        self.assertEqual(remove_letter('abracadabra', 2), 'brcadabra')
        self.assertEqual(remove_letter('abracadabra', 6), 'rcdbr')
        self.assertEqual(remove_letter('abracadabra', 8), 'rdr')
        self.assertEqual(remove_letter('abracadabra', 50), '')
