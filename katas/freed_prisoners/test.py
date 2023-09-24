import unittest

from .solution import freed_prisoners


class FreedPrisonersTest(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(
            4,
            freed_prisoners([True, True, False, False, False, True, False])
        )

        self.assertEqual(
            2,
            freed_prisoners([True, False, False, False, False, False, False])
        )

        self.assertEqual(
            2,
            freed_prisoners([True, True, True, False, False, False])

        )
        self.assertEqual(
            6,
            freed_prisoners([True, False, True, False, True, False])
        )

        self.assertEqual(
            1,
            freed_prisoners([True, True, True])
        )

        self.assertEqual(
            0,
            freed_prisoners([False, False, False]),
            0
        )

        self.assertEqual(
            0,
            freed_prisoners([False, True, True, True]),
            0
        )


if __name__ == "__main__":
    unittest.main()
