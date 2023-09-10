import unittest

from .solution import check_root


class CheckRootTest(unittest.TestCase):
    def test_validates_input_is_four_elements(self):
        self.assertEqual(check_root('10,11,12,13,15'), 'incorrect input')

    def test_validates_input_is_four_numbers(self):
        self.assertEqual(check_root('3,s,5,6'), 'incorrect input')

    def test_checks_if_not_consecutive(self):
        self.assertEqual(check_root('11,13,14,15'), 'not consecutive')

    def test_returns_correct_result(self):
        self.assertEqual(check_root('4,5,6,7'), '841, 29')
        self.assertEqual(check_root('10,11,12,13'), '17161, 131')
        self.assertEqual(check_root('1015,1016,1017,1018'), '1067648959441, 1033271')
        self.assertEqual(check_root('-4,-3,-2,-1'), '25, 5')

#
