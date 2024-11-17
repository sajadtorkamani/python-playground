import unittest
from .solution import order_by_domain


class SolutionTest(unittest.TestCase):
    def test_order_by_domain_1(self):
        input_list = [
            "http://www.google.en/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
            "http://www.google.govt/?x=jsdfkj",
            "http://www.google.comgov/?x=jsdfkj",
            "http://www.google.aorg/?x=jsdfkj",
        ]

        expected = [
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.aorg/?x=jsdfkj",
            "http://www.google.comgov/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.en/?x=jsdfkj",
            "http://www.google.govt/?x=jsdfkj",
        ]

        self.assertEqual(order_by_domain(input_list), expected)

    def test_order_by_domain_2(self):
        input_list = [
            'http://www.iimcq.mtb.com/?xwst=zctqw',
            'http://www.nsdnt.skz.xubp/?zvcdp=ajwu',
            'http://www.hvjx.bow.rtug/?wih=ldneo',
            'http://www.wsjd.rtug',
            'http://www.rmqg.org',
            'http://www.betlj.eig.kbhhg.com/?ofp=kpltw',
            'http://www.vxg.mvywc/?gedox=erqjz',
            'http://www.odb.vzzlf.yyjb.org/?tutrx=kkyjs'
        ]

        expected = [
            'http://www.betlj.eig.kbhhg.com/?ofp=kpltw',
            'http://www.iimcq.mtb.com/?xwst=zctqw',
            'http://www.odb.vzzlf.yyjb.org/?tutrx=kkyjs',
            'http://www.rmqg.org',

            'http://www.vxg.mvywc/?gedox=erqjz',
            'http://www.hvjx.bow.rtug/?wih=ldneo',
            'http://www.wsjd.rtug',
            'http://www.nsdnt.skz.xubp/?zvcdp=ajwu'
        ]

        self.assertEqual(order_by_domain(input_list), expected)


if __name__ == '__main__':
    unittest.main()
