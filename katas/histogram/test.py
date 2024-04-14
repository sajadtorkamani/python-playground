import unittest
from .solution import histogram, print_line


class SolutionTest(unittest.TestCase):
    def test_histogram(self):
        input = [7, 3, 70, 15, 0, 5]
        expected_output = "6|██ 5%\n" + \
                          "5|\n" + \
                          "4|███████ 15%\n" + \
                          "3|███████████████████████████████████ 70%\n" + \
                          "2|█ 3%\n" + \
                          "1|███ 7%\n"

        self.assertEqual(expected_output, histogram(input))

    """
    Works ok for values greater than zero
    """

    def test_print_line_value_greater_than_zero(self):
        self.assertEqual(
            "4|███████ 15%",
            print_line(num=4, numRollCount=15, totalRollCount=100)
        )

    """
    Works ok for zero values
    """

    def test_print_line_zero(self):
        self.assertEqual(
            "4|",
            print_line(num=4, numRollCount=0, totalRollCount=100)
        )


if __name__ == '__main__':
    unittest.main()
