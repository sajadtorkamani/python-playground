import unittest
from .solution import greet_jedi


class SolutionTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(greet_jedi('Beyonce', 'Knowles'), 'Greetings, master KnoBe')
        self.assertEqual(greet_jedi('Chris', 'Angelico'), 'Greetings, master AngCh')
        self.assertEqual(greet_jedi('grae', 'drake'), 'Greetings, master DraGr')
