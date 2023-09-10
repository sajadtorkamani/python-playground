import unittest
from .solution import get_middle

class GetMiddleTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(get_middle("test"),"es")
        self.assertEqual(get_middle("testing"),"t")
        self.assertEqual(get_middle("middle"),"dd")
        self.assertEqual(get_middle("A"),"A")
        self.assertEqual(get_middle("of"),"of")

  
if __name__ == "__main__":
  unittest.main()
