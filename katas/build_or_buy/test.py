import unittest

from katas.build_or_buy.solution import array1_has_all_array2_elements, build_or_buy


class TestBuildOrBuy(unittest.TestCase):
    def test_b_has_all_a_chars(self):
        self.assertEqual(True, array1_has_all_array2_elements("bwoo", "bw"))
        self.assertEqual(False, array1_has_all_array2_elements("booo", "bw"))

    def test_basic_cases(self):
        self.assertEqual(build_or_buy("bwoo"), ["road"])
        self.assertEqual(set(build_or_buy("bwsg")), set(["road", "settlement"]))
        self.assertEqual(build_or_buy(""), [])
        self.assertEqual(build_or_buy("ogogoogogo"), ["city"])
        self.assertEqual(build_or_buy("bwbwwwbb"), ["road"])
        self.assertEqual(set(build_or_buy("wgbooboosbssgbswos")), set(["road", "development", "settlement", "city"]))


if __name__ == "__main__":
    unittest.main()
